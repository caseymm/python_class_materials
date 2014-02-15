import re, string

#grimms = open("grimms.txt","r")

def process_file(filename):
    hist = dict()
    grimms = open(filename)
    for line in grimms:
        process_line(line,hist)
    return hist

#match = re.search(r"([A-Z]+\s)+\n", grimms.read())
#titles = re.findall(r"[A-Z]+", grimms.read())

def process_line(line,hist):
    #line = line.replace('-',' ')
    match = re.search(r"((([A-Z]+\S*[A-Z]+))\s)+$", line)
    #match_break = re.search(r"\n+", line)
    #together = match + match_break
    if match:
        print match.group()
    #else:
        #print "No match!!"

process_file('grimms.txt')
