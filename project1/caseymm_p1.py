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
    linenum=0
    
    for line in grimms:
        if content:
            block += line
            if line.strip() == "End of Project Gutenberg\'s Grimms\' Fairy Tales, by The Brothers Grimm": break
            match = re.search(r"((([A-Z]+\S*[A-Z]+))\s)+$", line)
    
            if match:
                title = match.group()
                print title
                process_line(line,hist)
            linenum += 1
            #(num) = line.strip().split()
            #print dept, item, num, linenum
            #inv.setdefault(num,{}).append(linenum)
            ###print linenum
            
        else:
            if line.strip() == "THE BROTHERS GRIMM FAIRY TALES":
                content = True
                block = "THE BROTHERS GRIMM FAIRY TALES"
                
    return hist

#match = re.search(r"([A-Z]+\s)+\n", grimms.read())
#titles = re.findall(r"[A-Z]+", grimms.read())


def process_line(line,hist):
    
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word,0) +1
    print hist #This prints one (the same) histogram for each title
            
process_file('grimms.txt')
