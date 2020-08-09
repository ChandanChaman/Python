"""Post dict data to web"""

import os
import requests

dict = {}
url = 'http://35.238.84.0/feedback/'

for f in os.listdir('/data/feedback/'):
    with open('/data/feedback/' + f) as fh:
        line = fh.readlines()
        dict['title'] = line[0].strip()
        dict['name'] = line[1].strip()
        dict['date'] = line[2].strip()
        dict['feedback'] = line[3].strip()

    res = requests.get(url)
    if res.ok:
        res = requests.post(url, data=dict)
        if res.status_code == 201:
            print('Feedback Uploded')

print('All Done')