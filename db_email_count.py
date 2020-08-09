"""Count email ids from file and store in db"""

import sqlite3
import re

file = 'file/mbox.txt'
sql_create= 'CREATE TABLE Counts (org TEXT, count INTEGER)'
sql_drop= 'DROP TABLE IF EXISTS Counts'
sql_check = 'select count(*) from Counts where org = ?'
sql_insert = 'insert into Counts (org , count) values(? ,1)'
sql_update = 'update Counts set count = count+1 where org = ?'
sql_res= 'select * from Counts order by count desc'

conn = sqlite3.connect('/Users/chandan/sqlite/emailCount.sqlite')
cur = conn.cursor()

cur.execute(sql_drop)
cur.execute(sql_create)

fh=open(file)
for line in fh:
    if not line.startswith('From:'):
        continue
    else:
        org = re.findall('@(.+)', line)[0]
        cur.execute(sql_check, (org,))
        row = cur.fetchone()

        if row[0] == 0:
            cur.execute(sql_insert,(org,) )
        else :
            cur.execute(sql_update,(org,))
conn.commit()
for row in cur.execute(sql_res):
    print (row[0],row[1])

cur.close()