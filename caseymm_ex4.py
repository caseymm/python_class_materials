#Due Sunday by 12:15

a = ["unc", "duke", "ncstate"]
b = ["ncstate", "duke", "unc"]
c = ["unc", "duke", "vt"]
d = ["unc", "unc", "unc"]

a.sort()
b.sort()
c.sort()
d.sort()

#need to check and see if the sorted lists match each other
def sort_list(t):
    result = []
    for s in t:
        #sorted_ans = s.sort()
        result.append(s)
    return result

print sort_list(a)
print sort_list(b)
print sort_list(c)
print sort_list(d)

#print has_same_elements(a,b)  # True
#print has_same_elements(a,c)  # False
#print has_same_elements(a,d)  # False