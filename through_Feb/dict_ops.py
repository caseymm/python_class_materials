inv = {'apples': 430, 'bananas':312, 'oranges': 523, 'pears':217}
for akey in inv.keys():
    print "The key", akey, "maps to value", inv[akey]
tmp = list(inv.keys())
print tmp
for akey in inv:
    print akey, inv[akey]
print
print "2"
print
#inv = {'apples': 430, 'bananas':312,'oranges': 523, 'pears':217}
print(list(inv.values()))
# items() returns k-v pairs as tuples print(list(inv.items()))
for (k,v) in inv.items():
    print k,v
for k in inv:
    print k, inv[k]