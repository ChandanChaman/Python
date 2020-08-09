""" Read & extract rewuired data from a json file """

import json
import urllib.request

url = input('Enter Location: ')
if len(url)<1:
    url ='http://py4e-data.dr-chuck.net/comments_42.json'

print ('Retrieving: ', url)
data =urllib.request.urlopen(url)

json_data=json.loads(data.read())

#print (json.dumps(json_data,indent=6))

count_lst = [c['count'] for c in json_data['comments']]

print ('Count :',len(count_lst))
print ('Sum :',sum(count_lst))