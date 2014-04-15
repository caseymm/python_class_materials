import re
import string
import sys
import os

user_query = raw_input ("Enter your query: ")

# Makes the user's query lowercase
query = user_query.lower()
print
if query == "qquit":
    sys.exit()

# Function restarts program if query != "qquit"    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

print "query = " + query
print
query_words = query.split()

# Takes the user's input and assigns search_param depending on matching terms
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
            query_words.sort()
        elif query_words[1] != 'and' or 'or':
            search_param = 'get_all'
            query_words.sort()

# Creates empty dict for words in the assigned content block to be searched
hist = dict()
brothers = open('brothers.txt')
block = ""
content = False

# Sets linenum = 120 since the first 120 lines of brothers.txt are skipped
linenum = 120

# Creates empty dict for pairing linenums with corresponding lines of text
inv = {}

# Reads stopwords.txt and creates the dict for stop_words  
fin = open("stopwords.txt","r")
stop_words = dict()
    
for line in fin:
    line = line.rstrip()
    stop_words.setdefault(line,{})
    
for line in brothers:
    if content:
        block += line
 
        if line.strip() == "THE END": # Finds end of brothers
            break
        
        linenum += 1
        printed_line = line.lower()
        
        # Populates dict that pairs linenums with corresponding lines of text
        inv.setdefault(linenum,[]).append(printed_line.rstrip())
        
        # Searches for titles within the content block taken from brothers
        match = re.search(r"((([A-Z]+\S*[A-Z]+))\s)+$", line)
            
        if match:
            #title = match.group()
            #title = title.rstrip()
            line = line.replace('-',' ')
        
        # Populates dict of words, w/dict of title, w/dict of linenums        
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            #hist.setdefault(word,{}).setdefault(title,[]).append(linenum)
            hist.setdefault(word,[]).append(linenum)
            
    else:   #Find beginning of Brothers
        if line.strip() == "PART I":
            content = True
            block = "PART I"

# Populates the stop_word hist   
for word in stop_words:
    if word in hist:
        del hist[word]  
    
def the_query(query_words, hist, inv):
    #inits dict of titles for the ability to match all
    title_dict = {}
    
    # Runs following code depending on search param
    if search_param == "and" or search_param == "get_all"\
                             or search_param == "get_one":
        for query_word in query_words:
            if query_word not in hist:
                print query_word
                print "  --"
            else:
                for title in hist[query_word]:
                    title_dict.setdefault(title,[]).append(query_word)
                    title_dict[title].sort()
                    
                # For words in query, create list of stories it appears in    
                final_titles = []
                for title in title_dict:
                    
                    # Do this if the lists for the words match
                    if query_words == title_dict[title]:
                        final_titles.append(title)
                        
                for title in final_titles:
                    print title
                    for query_word in query_words:
                        if query_word not in hist:
                            print "    " + query_word
                            print "    --"
                        else:
                            print "    " + query_word
                            query_upper = ("**"+ query_word.upper() +"**")
                            word_hist = hist[query_word]
                            this_line = word_hist.get(title, "empty")
                                            
                            # Take linenum and match it to key in inv dict to
                            # print line from brothers
                            for number in this_line:
                                if number in inv.keys():
                                    myline = inv.get(number)
                                    for i in myline:
                                        entry = "      " + str(number) + "  " +\
                                                i.replace(query_word, query_upper)
                                        print entry
        restart_program()   # End & restart if statement if search_param and,
                            # get_all, or get_one       
                            
    else:
        for query_word in query_words:
            if query_word not in hist:
                print 
            else:
                for title in hist[query_word]:
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
                                print "    --"
                            else:
                               
                                # Take linenum and match it to key in inv dict
                                # to print line from brothers
                                for number in this_line:
                                    if number in inv.keys():
                                        myline = inv.get(number)
                                        for i in myline:
                                            entry = "      " + str(number) +\
                                                    "  " + i.replace(query_word, query_upper)
                                            print entry
        restart_program()   # End & restart if statement if search_param not
                            # and, get_all, or get_one  
            
the_query(query_words, hist, inv)

