array = [0, 3, 2, 5, 6, 3, 4, 1, 0, 4]

def find_duplicates(array):
    #Create an empty dicitonary to store i as key and count as value
    num_dict = {}
    for i in array:
        
        #counts number of times item appears in array
        num_count = array.count(i)
        
        #outputs results to dictionary
        num_dict.setdefault(i, num_count)
        
    print num_dict
    
    #creates list to store repeated numbers in
    repeats = []
    for item in num_dict:
        
        #if the value associated w/the item is 2 or more, the number was repeated at
        #least once in the original array, no append that number to the repeats list
        if num_dict[item] >= 2:
            repeats.append(item)
    
    print repeats

find_duplicates(array)
    