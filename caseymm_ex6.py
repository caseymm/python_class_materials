import string 



def process_file(filename): 
    hist = dict() 
    fp = open(filename) 
    for line in fp:
        
        key, value = line.strip().split()
        hist[key] = value
        print key
        #need set default or check something to see if this is in the dictionary
        #hist[row[0]] should be referring to a list -> and run .append on the list
        
        
        for key in hist.items():
            empty = []
            if key not in empty:
                empty.append(key)
            #else:
            #    empty[key].append(value)
            return empty
            print empty
          
    return hist
    

hist = process_file("courses2.txt")
print hist
#empty


#def count_up(hist):
#    t = []
#    for key in hist.items():
#        t.append((value, key))
#        for value in hist.items():
#            if value not in t():
#                t.append(value)
#    return t
#t = count_up(hist)
#print t