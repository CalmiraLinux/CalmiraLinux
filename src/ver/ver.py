#!/usr/bin/python3

import os
import sys
import toml
import getpass

FILE = "/etc/calm-release"
PARAMS = (
    "name",
    "version",
    "codename",
    "description",
    "arch",
    "build",
    "build_date",
    "edition"
)

if not os.path.isfile(FILE):
    print("\033[1m\033[31mFile '{FILE}' not found!\033[0m", file=sys.stderr)
    exit(1)

data = toml.load(FILE)
system = data["system"]

for param in PARAMS:
    print("\033[1m{0:11}:\033[0m {1}".format(param, system[param]))
print("\033[1m{0:11}:\033[0m {1}".format("username", getpass.getuser()))
print("\033[1m{0:11}:\033[0m {1}".format("work dir", os.getcwd()))

print("\nCopyright (C) 2021, 2022 Michail Krasnov <linuxoid85@gmail.com>")
print("Copyright (C) 2022, Aristarh Bahirev <github.com/AristarhBahirev>")
