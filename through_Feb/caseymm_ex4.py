a = ["unc", "duke", "ncstate"]
b = ["ncstate", "duke", "unc"]
c = ["unc", "duke", "vt"]
d = ["unc", "unc", "unc"]

a.sort()
b.sort()
c.sort()
d.sort()

def has_same_elements(x,y):
    return x == y

print has_same_elements(a,b)  # True
print has_same_elements(a,c)  # False
print has_same_elements(a,d)  # False

print has_same_elements(b,a)  # True
print has_same_elements(b,c)  # False
print has_same_elements(b,d)  # False

print has_same_elements(c,a)  # False
print has_same_elements(c,b)  # False
print has_same_elements(c,d)  # False

print has_same_elements(d,a)  # False
print has_same_elements(d,b)  # False
print has_same_elements(d,c)  # False
