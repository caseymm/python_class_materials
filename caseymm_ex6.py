import string 
 
def process_file(filename): 
    hist = dict() 
    fp = open(filename) 
    for line in fp:
        
        key, value = line.strip().split()
        hist[key] = value
        #need set default or check something to see if this is in the dictionary
        #hist[row[0]] should be referring to a list -> and run .append on the list
        t = []
        for key, value in hist.items():
            t.append((value, key))
        
        return t 

hist = process_file("courses1.txt")
print hist


