#__author__ = 'saravana'

import json

with open("../Assignment.json","r") as fp:
    input = json.load(fp)
for item in input['opsworks']:
    print(item , '=' ,input['opsworks'][item])