#REMEMBER
#check for the character length of my lines to abide by style guide
import re, string

#grimms = open("grimms.txt","r")

def process_file(filename):
    hist = dict()
    grimms = open(filename)
    block = ""
    content = False
    inv = {}
    linenum = 120
    
    for line in grimms:
        if content:
            block += line
            if line.strip() == "End of Project Gutenberg\'s Grimms\' Fairy Tales, by The Brothers Grimm": break
            linenum += 1
            inv.setdefault(linenum,[]).append(line)
            
            match = re.search(r"((([A-Z]+\S*[A-Z]+))\s)+$", line)
            if match:
                title = match.group()
                title = title.replace('\n','')
                print title
                line = line.replace('-',' ')
            for word in line.split():
                word = word.strip(string.punctuation + string.whitespace)
                word = word.lower()
                hist.setdefault(word,{}).setdefault(title,[]).append(linenum)
            
        else:
            if line.strip() == "THE BROTHERS GRIMM FAIRY TALES":
                content = True
                block = "THE BROTHERS GRIMM FAIRY TALES"
    print hist
    print hist['quails']
    this_line = hist['quails'][title][0] #this returns the bracketed line matching the line number of the query
    #Only set to the first word in the list atm
    #Isn't working for other queries either - try something like for get title in this_line
    
    print this_line
    #for x in this_line:
    #    print this_line
    
    if this_line in inv.keys():
        myline = inv.get(this_line)
        for i in myline:
            print i
    #line_list = list(inv.keys())
    #print line_list
    #print inv
    return hist

    #for i in list following in title change [0] to something like [i] so that it will do it for each word
    #OR figure out how to get all of them at once
    
            
hist = process_file('grimms.txt')
