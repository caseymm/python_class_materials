from operator import itemgetter
t = [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print sorted(t, key=itemgetter(0))
print
print sorted(t, key=itemgetter(1))
sorted_by_letter = sorted(t, key=itemgetter(1))
print sorted(sorted_by_letter, key=itemgetter(0))
print
print sorted(t, key=itemgetter(2))
print

s = "This this IS is UNC unc"
print s.split()
print
print sorted(s.split())
def tolower(i):
    return str.lower(i)
print
for w in s.split():
    print tolower(w)
print
print sorted(s.split(), key=tolower)