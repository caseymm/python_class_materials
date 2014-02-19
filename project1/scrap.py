for i in query_words:
    n = n+1
    if n > 1:
        if query_words[1] == 'and':
            del query_words[1]
            search_param = param + "and"
        elif query_words[1] == 'or':
            del query_words[1]
            search_param = param + 'or'
        else:
            search_param = param + 'get_all'
    else:
        search_param = param + 'get_one'
    
print search_param

elif search_param == "get_all":
        print "line for getting all"
    elif search_param == "and":
            print "line for AND"
    else:
            print "failed"
            

def the_query(query_words, hist, inv):
            print query
            for query_word in query_words: 
                if query_word not in hist:
                    print "--"
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
                                    for number in this_line:
                                        if number in inv.keys():
                                            myline = inv.get(number)
                                            for i in myline:
                                                entry = "      " + str(number) + "  " + i.replace(query_word, query_upper)
                                                print entry
            
        the_query(query_words, hist, inv)