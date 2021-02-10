#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml, re

def secrets():
    with open("secrets.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
    return cfg

def input_file():
    with open("docker-compose.yml", "r") as inputfile:
        inf = inputfile.read()
    return inf
    
def output_file(output):
    with open("docker-compose.yml", "w+") as outputfile:
        outputfile.write(output)

secret_list = secrets()
document = input_file()
for category in secret_list['secrets']:
    for string in secret_list['secrets'][category]:
        print(string)
        document=document.replace(string, str(secret_list['secrets'][category][string]))

output_file(document)
