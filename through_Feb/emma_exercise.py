import string

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line,hist)
    return hist

def process_line(line,hist):
    line = line.replace('-',' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word,0) +1
        
def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    
    #Nice to return a list of tuples becuase it allows you to loop through and do stuff with the key and the value
    
    #for (key, value) in hist.items():
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse = True)
    return t

def subtract (d1, d2):
    result = dict()
    for key in d1:
        if key not in d2:
            result[key] = None
    return result

hist = process_file('emma_ch1.txt')

t = most_common(hist)
words = process_file('words.txt')
print "Total words = ", different_words(hist)
print
diff = subtract(hist, words)
print diff
for word in diff.keys():
    print word
print
print
print "Different words = ", different_words(hist)
print
print "Most common:"
for freq, word in t[0:10]:
    print word, "\t", freq
    

    
    