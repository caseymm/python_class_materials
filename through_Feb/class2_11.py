def fac(n):
    if n == 0:
        return 1
    else:
        tmp = n * fac(n-1)
        return tmp

print fac(4)

#explanation of recursion
#fac(3)
#    tmp = 3 * fac(2)
#        tmp = 2 * fac(1)
#            tmp = 1 * fac(1)
#            1
#        2
#    6

def fib(n):
    #print "time"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib (n-2)
    
print fib(4)

t = [1, 3, 5, 7, 9]

def listsum(t):
    sum = 0
    for i in t:
        sum = i + sum
    return sum

print listsum(t)

def listsum2(t):
    if len(t) == 1:
        return t[0]
    else:
        tmp = t[0] + listsum2(t[1:])
        return tmp

print listsum2(t)

print "Example 5:"

word = "python"

def str_reverse(word):
    #backwards = ""
    if len(word) == 1:
        return word
    else:
        backwards = word[-1] + str_reverse(word[:-1])
        return backwards
print str_reverse(word)

palindrome = "racecar"
#check to see if the reverse of the word is the same as the original

    
    