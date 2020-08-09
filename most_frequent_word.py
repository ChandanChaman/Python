"""Find the most frequent word in given file and its count"""

fh = open ('file.txt')
dict={}
count =None
bigWord=None
for line in fh:
    words= line.split()
    for word in words:
        dict[word]=dict.get(word,0) +1
#print (dict)

for k,v in dict.items():
    if bigWord == None or count < v:
        count = v
        bigWord =k

print ('Most frequent word -\t' , bigWord , '\n' 'Count is - \t', count)
