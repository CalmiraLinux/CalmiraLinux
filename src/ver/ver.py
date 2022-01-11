#!/usr/bin/python3
# Script for print information about Calmira
# (C) 2021 Michail Krasnov <linuxoid85@gmail.com>
# For Calmira LX4 1.1 GNU/Linux

import os
import json
import gettext

gettext.bindtextdomain('ver', '/usr/share/locale')
gettext.textdomain('ver')
_ = gettext.gettext

SYSTEM_INFO = "/etc/calm-release"

if os.path.isfile(SYSTEM_INFO):
    pass
else:
    print(_("Error: file {} doesn't exists!").format(SYSTEM_INFO))
    exit(1)

f = open(SYSTEM_INFO)

sys_data = json.load(f)

print(_("\n\tSystem name: {}").format(sys_data["distroName"]))
print(_("\tSystem version: {}").format(sys_data["distroVersion"]))
print(_("\tSystem codename: {}").format(sys_data["distroCodename"]))
print(_("\tSystem build: {}\n").format(sys_data["distroBuild"]))
print(_("(C) 2021 Michail Krasnov <linuxoid85@gmail.com> for {0} {1}\n").format(sys_data["distroName"], sys_data["distroVersion"]))

f.close()
