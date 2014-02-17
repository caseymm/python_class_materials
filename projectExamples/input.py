print ("Enter your query:")

query = raw_input ("> ")
print query
words = query.split()


fin = open("goods.txt","r")
inv = {}
linenum=0
for line in fin:
    linenum += 1
    (dept, item, num) = line.strip().split()
    inv.setdefault(dept,{}).setdefault(item,[]).append(linenum)
    
for word in words:
    print inv.get(word)