#!/usr/bin/python3

import os
import toml

class Config(object):

    @staticmethod
    def get() -> dict:
        return toml.load('./config.toml')

class Checker(object):

    def files(self, _case: str, mode: str, _type: str) -> list:
        """
        Modes:
        - 'dir'
        - 'file'

        Types:
        - 'required'
        - 'optional'
        """

        conf = Config.get()
        data = conf[_case]

        match mode:
            case "dir":
                return data.get(f'{_type}_d')
            case "file":
                return data.get(f'{_type}_f')
            case _:
                return []

    def check(self, files: list, head: str, mode: str) -> bool:
        """
        Work modes:
        - 'dir'
        - 'file'
        """

        data = True
        
        print(f"checking dirs in '{head}'...")

        match mode:
            case "dir":
                check = os.path.isdir
            case "file":
                check = os.path.isfile
            case _:
                return False

        for file in files:
            print(f"\t{file}...", end = " ")
            if check(f"/{file}"):
                print("ok")
            else:
                print("FAIL")
                data = False

        return data
