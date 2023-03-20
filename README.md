# IRC Web Registration

## Version 1
The v1 of this concept can be referenced in the [old and *not updated* README](https://git.com.de/LibertaCasa/webreg/src/branch/master/README.old.md)

The v1.1 enhancements added by [Georg Pfuetzenreuter](https://git.com.de/Georg) implements support for additional SSO integration to our KeyCloak setup.
It also works-in SSL support.

This webform available [here](https://liberta.casa/register) is purely demonstrative and does not successfully `POST` user data

## Introduction

This is a basic still WIP overhaul framework for registering an account on an ircd using a webform that is referenced above.


## Features

- It relies on the draft IRCv3 spec [draft/account-registration](https://ircv3.net/specs/extensions/account-registration.html)
- It utilizes the flask framework and `WEBIRC` to relay remote host ip address.
- Can be tweaked to allow registration attempts from exit-nodes and other unsavory hosts allowing them to securely work with the `require-sasl` constraint if needed.

## Requirements

This will work with python3.6 and above.

It is recommended to work within a virtual environment.

1. `mkdir ircwebreg && cd ircwebreg`
2. Clone this repository.
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`

## Installation and Setup

Todo! Refer to the issues and the __Milestones__ and __Projects__
for more


### Note

Only works with setups not requiring verification at this moment as stated in #4 
