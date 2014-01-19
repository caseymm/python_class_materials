def sqroot_newton(a):
    x = a/2
    y = (x+(a/x))/2

    while x != y:
        x = y
        y = (x+(a/x))/2
    
    return x

print sqroot_newton(17.0)