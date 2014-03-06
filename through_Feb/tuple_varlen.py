def printall(*args): #gather
    print args
printall(1, 2, 3)
t = (7, 3)
#print divmod(t) #error
print divmod(*t) #scatter