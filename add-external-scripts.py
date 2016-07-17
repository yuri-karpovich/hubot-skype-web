#!/usr/bin/env python

import json
import requests
import os
from subprocess import call

if os.getenv('HUBOT_PACKAGE_URL'):
    package_url = os.getenv('HUBOT_PACKAGE_URL')
    r = requests.get(package_url)
    for item in r.json():
        call( ["npm", "install", item, "--save"])

    e = open('/opt/hubot/external-scripts.json', 'w')
    e.write(r.text)
    e.close()
