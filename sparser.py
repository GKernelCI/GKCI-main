#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import re
import os
import secrets
import string
from random import randint


def generate_password(password_length):
    alphabet = string.ascii_letters +string.digits
    characters = [secrets.choice(alphabet) for i in range(password_length)]
    password = ''.join(characters)
    return password

def secrets_file():
    if os.path.isfile('./secrets.yml'):
        with open("secrets.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile)
        return cfg
    else:
        with open("secrets.yml.example", "r") as ymlfile:
            cfg = yaml.load(ymlfile)
        return cfg

def input_file():
    with open("docker-compose.yml", "r") as inputfile:
        inf = inputfile.read()
    return inf
    
def output_file(output):
    with open("docker-compose.yml", "w+") as outputfile:
        outputfile.write(output)

if __name__ == '__main__':
    secret_list = secrets_file()
    document = input_file()
    for category in secret_list['secrets']:
        for namekey in secret_list['secrets'][category]:
            print(namekey)
            if str(secret_list['secrets'][category][namekey]) == "GENERATE_PASS":
                password = generate_password(8)
                document=document.replace(namekey, generate_password(8))
            elif str(secret_list['secrets'][category][namekey]) == "GENERATE_NICK":
                document=document.replace(namekey, "gkci_"+ str(randint(1, 100)))
            else:
                document=document.replace(namekey, str(secret_list['secrets'][category][namekey]))
    output_file(document)
