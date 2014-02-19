#REMEMBER
#check for the character length of my lines to abide by style guide
import re, string

print ("Enter your query:")

query = raw_input ("> ")
print query
query_words = query.split()

def process_stops(filename):
    stop_hist = dict()
    stopwords = open(filename)
    for line in stopwords:
        process_line(line, stop_hist)
    return stop_hist

def process_line(line, stop_hist):
    line = line.replace('-',' ')
    for each in line.split():
        each = each.strip(string.punctuation + string.whitespace)
        each = each.lower()
        stop_hist[each] = stop_hist.get(each,0) +1

def process_file(filename):
    hist = dict()
    grimms = open(filename)
    block = ""
    content = False
    inv = {}
    linenum = 120
    
    fin = open("stopwords.txt","r")
    stop_words = dict()
    for line in fin:
        line = line.replace('\n','')
        stop_words.setdefault(line,{})
    #print stop_words
    
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
                #print title
                line = line.replace('-',' ')
            for word in line.split():
                word = word.strip(string.punctuation + string.whitespace)
                word = word.lower()
                hist.setdefault(word,{}).setdefault(title,[]).append(linenum)
            
        else:
            if line.strip() == "THE BROTHERS GRIMM FAIRY TALES":
                content = True
                block = "THE BROTHERS GRIMM FAIRY TALES"
    
    for word in stop_words:
        if word in hist:
            del hist[word]
    
    
    for query_word in query_words:
        if query_word not in hist:
            print "--"
        else:
            #print hist[query_word]
            query_upper = ("**"+ query_word.upper() +"**")
            #print query_upper
            for title in hist[query_word]:
                print title
                this_line = hist[query_word][title] 
                
                for number in this_line:
                    print number
                
                    if number in inv.keys():
                        myline = inv.get(number)
                        for i in myline:
                            print i.replace(query, query_upper)
    return hist

#def subtract (d1, d2):
#    result = dict()
#    print d1
#    for key in d2:
#        if key in d1:
#            result[key] = None
#            #del result[key]
#            hist[query_word] = None
#    return result
    
            
hist = process_file('grimms.txt')
stops = process_stops('stopwords.txt')
#print stops
#grimms_dict = subtract(stops, hist)
#print grimms_dict

