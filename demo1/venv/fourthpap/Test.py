# coding=utf-8
import json
filename = 'user.json'
with open(filename) as file_objec:
    text = json.load(file_objec)
    print(text[0]['username'])

