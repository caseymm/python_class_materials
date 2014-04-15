from re import compile
l=compile("([\w,.'\x92]*\w)").findall(open(raw_input('Input file: '),'r').read().lower())
f=open(raw_input('Output file: '),'w')
for word in set(l):
    print>>f, word, '\t', l.count(word)
f.close()