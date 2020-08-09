""" """

fh = open ('file.txt')
dict={}
count =None
bigWord=None
for line in fh:
    words= line.split()
    for word in words:
        dict[word]=dict.get(word,0) +1

#using list comprehension -
#print( sorted([(v,k) for k,v in dict.items() ],reverse=True))

list = []
for k,v in dict.items():
    list.append((v,k))

new=sorted(list,reverse=True)
for i in (new[:10]):
    print (i[1], '\t', i[0])
