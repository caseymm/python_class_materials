print "Example 1 \n gets the numbers of the items"

fin = open("goods.txt","r")
inv = {}
for line in fin:
    (dept, item, num) = line.strip().split()
    print dept, item, num
    inv.setdefault(dept,{}).setdefault(item,0)
    inv[dept][item] += int(num)
print inv

print "Example 2 \n Gets the line numbers of the words"

fin = open("goods.txt","r")
inv = {}
linenum=0
for line in fin:
    linenum += 1
    (dept, item, num) = line.strip().split()
    print dept, item, num, linenum
    inv.setdefault(dept,{}).setdefault(item,[]).append(linenum)
print inv