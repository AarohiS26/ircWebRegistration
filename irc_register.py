import irctokens
import socket
import os

webircpass = os.getenv("WEBIRC_PASS")

def ircregister(userip, username, password, email="*"):
    d = irctokens.StatefulDecoder()
    e = irctokens.StatefulEncoder()
    s = socket.socket()

    
    # Here we assume using this only on localhost i.e. loopback
    s.connect(("127.0.0.1", 6667))

    def _send(line):
        print(f"> {line.format()}")
        e.push(line)
        while e.pending():
            e.pop(s.send(e.pending()))
    _send(irctokens.build("WEBIRC", [ webircpass, "WebregGateway", userip, userip, "secure"]))
    lines = d.push(s.recv(1024))
    if lines == None:
        print("!disconnected")
        return "disconnected"
    elif lines.command == "ERROR" and lines.params == "Invalid WebIRC password":
        return "WebIRC bad password"
    _send(irctokens.build("CAP", ["LS", "302"]))
    while True:
        lines = d.push(s.recv(1024))
        if lines == None:
            print("! disconnected")
            break        
        for line in lines:
            print(f"< {line.format()}")
            # REGISTER can be attempted before-connect if server supports
            # but if the server responds with the corresponding FAIL we
            # need to try again. We can also handle email-required using
            # the same keys. How to access these key-value pairs?
            # reference: https://ircv3.net/specs/extensions/account-registration.html
            # do we handle if email-req but not before-connect
            # also how about when `custom-account-name` may be a value
            if 'draft/account-registration=before-connect' in line.params:
                _send(irctokens.build("CAP", ["REQ", "draft/account-registration"]))
            if line.command == "CAP" and ("NAK" in line.params):
                return "CAP_REFUSED"
            elif line.command == "CAP" and ("ACK" in line.params):
                _send(irctokens.build("CAP", ["END"]))
                _send(irctokens.build("USER", ["u", "0", "*", username]))
                _send(irctokens.build("NICK", [username]))
                if line.command == "432":
                    return "ERR_ERRONEUSNICKNAME"
                if line.command == "433":
                    return "ERR_NICKNAMEINUSE"
                _send(irctokens.build("REGISTER", [username, "*", password]))
            if line.command == "REGISTER" and ("SUCCESS" in line.params):
                _send(irctokens.build("QUIT"))
                return "SUCCESS"
	