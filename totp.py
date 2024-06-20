#!/usr/bin/env python3
"""
Generates a TOTP code.

Based on MinTOTP by Susam Pal.
"""
# Forked from <https://github.com/susam/mintotp>.


import base64
import binascii
import getpass
import hmac
import struct
import sys
import time


def hotp(key, counter, digits=6, digest="sha1"):
    key = base64.b32decode(key.upper() + "=" * ((8 - len(key)) % 8))
    counter = struct.pack(">Q", counter)
    mac = hmac.new(key, counter, digest).digest()
    offset = mac[-1] & 0x0F
    binary = struct.unpack(">L", mac[offset:offset + 4])[0] & 0x7FFFFFFF
    return str(binary)[-digits:].zfill(digits)


def totp(key, time_step=30, digits=6, digest="sha1"):
    """
    Returns a tuple of the TOTP code and the number of seconds remaining for
    its lifetime.
    """
    now = int(time.time())
    return (hotp(key, now // time_step, digits, digest),
            time_step - now % time_step)


def normalize_key(key):
    return "".join((c for c in key if not c.isspace()))


def main():
    key = ""
    while not key:
        key = getpass.getpass(prompt="TOTP key: ").strip()
    (code, seconds_left) = totp(normalize_key(key))
    print(f"{code} ({seconds_left}s remaining)")


if __name__ == "__main__":
    try:
        main()
    except binascii.Error as e:
        print(e, file=sys.stderr)
    except KeyboardInterrupt:
        sys.exit(1)
