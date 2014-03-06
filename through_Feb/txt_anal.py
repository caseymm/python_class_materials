
#print words w/no chars from list
def has_no(word,forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if has_no(word,'aeiou'):
        print word