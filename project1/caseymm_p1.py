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
            linenum += 1
            
            match = re.search(r"((([A-Z]+\S*[A-Z]+))\s)+$", line)
            if match:
                title = match.group()
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
    return hist
    
            
hist = process_file('grimms.txt')
