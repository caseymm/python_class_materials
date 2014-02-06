import string 
 
def process_file(filename): 
    hist = dict() 
    fp = open(filename) 
    for line in fp:
        #line = line.strip()
        #row = line.split()
        #hist[row[0]] = row[1]
        
        key, value = line.strip().split()
        hist[key] = value
        
    return hist 

hist = process_file("courses1.txt")
print hist
