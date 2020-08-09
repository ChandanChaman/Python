"""Search in log file(s) for match & ignore save the consolidated result in  a file"""

import re
import json
from _datetime import datetime

now = datetime.now().strftime("%Y-%m-%d_%H:%M")


def read_json():
    with open('key.json', 'r') as js:
        data = json.load(js)
    keyword = data['match_string']
    ignore = data['ignore_string']
    return (keyword, ignore)


def write(op):
    with open('out'+ now +'.txt','a') as oh:
        oh.writelines(op)
        print (oh)


def search(file):
    keywords,ignore = read_json()
    keyword = '|'.join(keywords)
    ignore = '|'.join(ignore)
    print (keyword)
    print (ignore)
    with open(file) as fh:
        for line in fh:
            match = re.findall(keyword, line)
            ummatch = re.findall(ignore, line)
            #print (match)
            print (ummatch)
            if match and not ummatch:
                op = (line)
                write(op)


search('file1.txt')
