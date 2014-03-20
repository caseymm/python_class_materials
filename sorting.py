from operator import itemgetter
t = [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print sorted(t, key=itemgetter(0))
print
print sorted(t, key=itemgetter(1))
print
print sorted(t, key=itemgetter(2))
print