#!/usr/bin/python3

import libcheck

check = libcheck.Checker()
r_root_dirs = check.files("root_fs", "dir", "required")
r_usr_dirs = check.files("usr_fs", "dir", "required")
o_usr_dirs = check.files("usr_fs", "dir", "optional")

r_root_bin = check.files("root_bin", "file", "required")
o_root_bin = check.files("root_bin", "file", "optional")

r_root_sbin = check.files("root_sbin", "file", "required")
o_root_sbin = check.files("root_sbin", "file", "optional")

r_root_var = check.files("root_var", "dir", "required")
o_root_var = check.files("root_var", "dir", "optional")

data = []
o_data = []

data.append(check.check(r_root_dirs, "/", "dir"))
data.append(check.check(r_usr_dirs, "/usr", "dir"))
o_data.append(check.check(o_usr_dirs, "/usr (optional)", "dir"))
data.append(check.check(r_root_bin, "/bin", "file"))
o_data.append(check.check(o_root_bin, "/bin (optional)", "file"))
data.append(check.check(r_root_var, "/var", "dir"))
o_data.append(check.check(o_root_var, "/var (optional)", "dir"))

if all(o_data):
    print("Были найдены опциональные компоненты, одобренные FHS")

if all(data):
    print("Система совместима с FHS!")
    exit(0)
else:
    print("Система НЕ совместима с FHS!")
    exit(1)
