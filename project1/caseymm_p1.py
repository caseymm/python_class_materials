import re, string

#grimms = open("grimms.txt","r")

def process_file(filename):
    hist = dict()
    grimms = open(filename)
    block = ""
    content = False
    
    for line in grimms:
        if content:
            block += line
            if line.strip() == "End of Project Gutenberg\'s Grimms\' Fairy Tales, by The Brothers Grimm": break
            process_line(line,hist)
        else:
            if line.strip() == "THE BROTHERS GRIMM FAIRY TALES":
                content = True
                block = "THE BROTHERS GRIMM FAIRY TALES"
                
    return hist

#match = re.search(r"([A-Z]+\s)+\n", grimms.read())
#titles = re.findall(r"[A-Z]+", grimms.read())

def process_line(line,hist):
    #line = line.replace('-',' ')
    match = re.search(r"((([A-Z]+\S*[A-Z]+))\s)+$", line)
    if match:
        print match.group()
    #else:
        #print "No match!!"

process_file('grimms.txt')
