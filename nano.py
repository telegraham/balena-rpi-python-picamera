#!/usr/bin/python

import requests
import os

palette_host = os.environ.get('PALETTE_HOST') # virtual-window-293.herokuapp.com
animation_name = os.environ.get('ANIMATION_NAME') # "Virtual Window"
aurora_host = os.environ.get('AURORA_HOST') # 10.0.0.3
aurora_port = os.environ.get('AURORA_PORT')
aurora_api_key = os.environ.get('AURORA_API_KEY') 

response = requests.get('https://{host}/pallettes/current'.format(host=palette_host))

colors = response.json()['pallette']['colors']

payload = {
  "write" : {
    "command" : "add",
    "version": "2.0",
    "animType": "random",
    "animName" : animation_name,
    "loop": True,
    "colorType": "HSB",
    "palette": colors
  }
}

aurora_url = "http://{host}:{port}/api/v1/{api_key}/effects".format(host=aurora_host, port=aurora_port, api_key=aurora_api_key)

resp = requests.put(aurora_url, json=payload)
