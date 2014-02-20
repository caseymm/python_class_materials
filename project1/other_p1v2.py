#REMEMBER
#check for the character length of my lines to abide by style guide
import re, string, sys

query = raw_input ("Enter your query: ")
print
print "query = " + query
print
query_words = query.split()

n = 0
search_param = 'get_all'
for i in query_words:
    n = n+1
    if n > 1:
        if query_words[1] == 'and':
            search_param = "and"
            del query_words[1]
            query_words.sort()
        elif query_words[1] == 'or':
            search_param = 'or'
            del query_words[1]
print search_param
print query_words

hist = dict()
grimms = open('grimms.txt')
block = ""
content = False
inv = {}
linenum = 120
    
fin = open("stopwords.txt","r")
stop_words = dict()
    
for line in fin:
    line = line.rstrip()
    stop_words.setdefault(line,{})
    
for line in grimms:
    if content:
        block += line
        if line.strip() == "End of Project Gutenberg\'s Grimms\' Fairy Tales, by The Brothers Grimm": break
        linenum += 1
        printed_line = line.lower()
        inv.setdefault(linenum,[]).append(printed_line.rstrip())
        match = re.search(r"((([A-Z]+\S*[A-Z]+))\s)+$", line)
            
        if match:
            title = match.group()
            title = title.rstrip()
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
    
def the_query(query_words, hist, inv):    
    print query
    title_dict = {}
    for query_word in query_words: 
        if query_word not in hist:
            print "--"
        else:
            for title in hist[query_word]:
                title_dict.setdefault(title,[]).append(query_word)
                title_dict[title].sort()
                if search_param == "and":
                    final_titles = []
                    for title in title_dict:
                        if query_words == title_dict[title]:
                            final_titles.append(title)
                            print final_titles
                            
                
                    
                elif search_param == "or" or "get_one":
                    print "  " + title
                    
                    for query_word in query_words:
                        if query_word not in hist:
                            print "    " + query_word
                            print "    --"
                        else:
                            print "    " + query_word
                            query_upper = ("**"+ query_word.upper() +"**")
                            word_hist = hist[query_word]
                            this_line = word_hist.get(title, "empty")
                            
                            if this_line == "empty":
                                if search_param == 'and':
                                    print "no match"
                                    #sys.exit()
                                else:
                                    print "    --"
                            else:            
                                for number in this_line:
                                    if number in inv.keys():
                                        myline = inv.get(number)
                                        for i in myline:
                                            entry = "      " + str(number) + "  " + i.replace(query_word, query_upper)
                                            print entry
                                        
    #print title_dict
            

the_query(query_words, hist, inv)