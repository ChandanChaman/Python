""" Read user log file to extract  INFO/ERROR count for each user and store the data in csv format """

import re
import operator
import csv

error ={}
user_info={}
user_error={}
user={}

with open('syslog.log') as file:
    for line in file:
        search=re.search(r'ticky: ([A-Z]+) ([\w\s\'\[\]\#]*) \(([\w\.]+)\)',line)
        un = search[3]
        user_info[un] = user_info.get(un, 0)
        user_error[un] = user_error.get(un, 0)
        if 'INFO' in search[1]:
            user_info[un]=user_info.get(un,0)+1

        elif 'ERROR' in search[1]:
            user_error[un]=user_error.get(un,0)+1
            err=search[2]
            error[err] = error.get(err,0) +1

for k in user_info.keys():
    user[k]=[user_info[k],user_error[k]]

user_s=sorted(user.items(),key=operator.itemgetter(0))
error_s=sorted(error.items(),key=operator.itemgetter(1),reverse=True)

with open('error_message.csv','w') as cf:
    writer=csv.writer(cf)
    writer.writerow(['Error','Count'])
    writer.writerows(error_s)

with open('user_statistics.csv','w') as cf:
    writer=csv.writer(cf)
    writer.writerow(['Username', 'INFO', 'ERROR'])
    for i in user_s:
        writer.writerow([i[0],i[1][0],i[1][1]])