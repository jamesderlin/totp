#  totp

A less minimal TOTP generator based on [MinTOTP](https://github.com/susam/mintotp).


## Differences with MinTOTP

* Prompts for the TOTP key.
* Uses Python's `getpass` to read the TOTP key without echoing it.
* Ignores all spaces in the TOTP key.
* Reads only one TOTP key at a time.
* Avoids printing Python backtraces if interrupted with Ctrl+C or if an invalid
  base32 character is entered for the TOTP key.

Auxiliary files such as build and test files also have been removed.
