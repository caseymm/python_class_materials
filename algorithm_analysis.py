#shows linear relationship
#as n gets increasingly larger, takes longer to run

import time
def sumofn(n):
    start = time.time()
    s=0
    for i in range(1,n+1):
        s=s+i
    end = time.time()
    return (s,end-start)
print "1000000"
for i in range(5):
    print " Sum is %d; time = %10.7f seconds." % sumofn(1000000)
print "10000000"
for i in range(5):
    print " Sum is %d; time = %10.7f seconds." % sumofn(10000000)
print

#uses sum forumla to avoid needing to iterate through for loops and the number
#of operations that we need to run
print "using sum formula"
def sumofn2(n):
    start = time.time()
    s = (n*(n+1))/2
    end = time.time()
    return (s,end-start)
print sumofn2(4)
print "1000000"
for i in range(5):
    print " Sum is %d; time = %10.7f seconds." % sumofn2(1000000)
print "10000000"
for i in range(5):
    print " Sum is %d; time = %10.7f seconds." % sumofn2(10000000)
    
#Count steps instead of "wall clock" time
#O() is the "order of magnitude" - takes biggest factor

print
print "other cases"

a = range(1,10000000)
start = time.time()
for b in a:
    #if b == 1:
    #if b == 5000000:
    if b == 500:
        break
end = time.time()
print end-start