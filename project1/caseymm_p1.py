#REMEMBER
#check for the character length of my lines to abide by style guide
import re, string

query = raw_input ("Enter your query: ")
print
print "query = " + query
print
query_words = query.split()

def process_file(filename):
    hist = dict()
    grimms = open(filename)
    block = ""
    content = False
    inv = {}
    linenum = 120
    
    fin = open("stopwords.txt","r")
    stop_words = dict()
    title_nums = {}
    
    for line in fin:
        line = line.rstrip()
        stop_words.setdefault(line,{})
    
    for line in grimms:
        if content:
            block += line
            if line.strip() == "End of Project Gutenberg\'s Grimms\' Fairy Tales, by The Brothers Grimm": break
            linenum += 1
            inv.setdefault(linenum,[]).append(line.rstrip())
            
            match = re.search(r"((([A-Z]+\S*[A-Z]+))\s)+$", line)
            if match:
                title = match.group()
                title = title.rstrip()
                #print title
                line = line.replace('-',' ')  
            for word in line.split():
                word = word.strip(string.punctuation + string.whitespace)
                word = word.lower()
                hist.setdefault(word,{}).setdefault(title,[]).append(linenum)
                #doesn't work
                #for title in hist[word]:
                    #title_nums.setdefault(title,[]).append(linenum)
            
        else:
            if line.strip() == "THE BROTHERS GRIMM FAIRY TALES":
                content = True
                block = "THE BROTHERS GRIMM FAIRY TALES"
    print title_nums
    
    for word in stop_words:
        if word in hist:
            del hist[word]
    
    #for query_word in query_words:
    for title in hist[query]:
        print "  " + title
        for query_word in query_words:
            if query_word not in hist:
                print query_word
                print "--"
            else:
                print "    " + query_word
                query_upper = ("**"+ query_word.upper() +"**")
                this_line = hist[query_word][title] 
                        
                for number in this_line:
                    if number in inv.keys():
                        myline = inv.get(number)
                        for i in myline:
                            entry = "      " + str(number) + "  " + i.replace(query, query_upper)
                            #print i.replace(query, query_upper)
                            print entry
    return hist
            
hist = process_file('grimms.txt')


