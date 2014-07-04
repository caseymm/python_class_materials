#########Ex 2
def sqroot_newton(a):
    x = a/2
    y = (x+(a/x))/2

    while x != y:
        x = y
        y = (x+(a/x))/2
    
    return x

print sqroot_newton(17.0)
#output 4.1231

#########Ex 5
import re
faculty = open("faculty.html","r")
emails = re.findall(r'[\w\.-]+@[\w\.-]+', faculty.read())
emails = list(set(emails))

########Ex 6
import string 
fp = open("courses2.txt", "r")
hist = dict()

for line in fp:
    line = line.strip()
    row = line.split()
    courses = row[0]
    instructors = row[1] 
    
    if courses in hist:
        hist[courses].append(instructors)
    else:
        hist[courses] = [instructors]

print hist
{'760': ['Capra'], '512': ['Haas'], '884': ['Kelly'], '523':
['Capra', 'Haas', 'Mostafa'], '509': ['Arguello', 'Kelly', 'Losee']}

course_numbers = list(hist.keys())
print course_numbers
['760', '512', '884', '523', '509']

print hist.get('523')
['Capra', 'Haas', 'Mostafa']

course_list = []
for key in hist:
    if 'Capra' in hist[key]:
        course_list.append(key)
print course_list
['760', '523']

instructor_names = list(hist.values())
instructor_list = []
 
for i in instructor_names:
    for name in i:
        if name not in instructor_list:
            instructor_list.append(name)

print instructor_list
['Capra', 'Haas', 'Kelly', 'Mostafa', 'Arguello', 'Losee']

######### Ex 7
class Elevator:
    def __init__(self):
        self.floor = 1
        self.num_pass = 0
        self.door_open = False
    def get_floor(self):
        return self.floor
    def get_num_pass(self):
        return self.num_pass
    def get_door(self):
        return self.door_open
    def __str__(self):
        return "floor=" + str(self.floor) + ", passengers=" +\
        str(self.num_pass) + ", door open=" + str(self.door_open)
    
    def call_to_floor(self, newfloor):
        self.door_open = False
        self.floor = newfloor       
    def enter_pass(self, num):
        self.door_open = True
        self.num_pass = self.num_pass + num
    def exit_pass(self, num):
        self.door_open = True
        self.num_pass = self.num_pass - num
        
e = Elevator()
#floor=1, passengers=0, door open=False
e.call_to_floor(9)
#floor=9, passengers=0, door open=False
e.enter_pass(3)
#floor=9, passengers=3, door open=True
e.call_to_floor(4)
#floor=4, passengers=3, door open=False
e.exit_pass(1)
#floor=4, passengers=2, door open=True

####### Ex 8
import random

class Card(object):

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        # check the ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # ranks are the same, so check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # suits and ranks are the same, so tie
        return 0

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
        
class Hand(Deck):
    ''' Hand inherits from Deck. '''
    def __init__(self,label=''):
        self.cards = []
        self.label = label
    def has_pair(self):
        res = []
        result = False
        for card in self.cards:
            res.append(card.rank)
            for i in res:
                res.count(i)
                if res.count(i) >= 2:
                    result = True
        return result
    def has_twopair(self):
        res = []
        result = False
        for card in self.cards:
            res.append(card.rank)
            res2 = []
            for i in res:
                res2.append(res.count(i))
                n = 0
                for second_i in res2:
                    if second_i == 2:
                        n = n+1
                        if n >= 4:
                            result = True
        return result
    def has_flush(self, num):
        res = []
        result = False
        for card in self.cards:
            res.append(card.suit)
            for i in res:
                res.count(i)
                if res.count(i) == num:
                    result = True
        return result
    def classify(self):
        label = ''
        if h.has_flush(7):
            label = "flush"
            return label
        if h.has_twopair():
            label = "two pair"
            return label
        if h.has_pair():
            label = "pair"
            return label
        else:
            label = "high card"
        return label
       

d = Deck()
h = Hand()
d.shuffle()
#allows for running 5 or 7 card hands
d.move_cards(h,7)
print "Your hand is:"
#7 cards, 6 of Diamonds...
print "You have a pair:"
print h.has_pair() #T or F
print "You have two pair:"
print h.has_twopair() #T or F
print "You have a flush:"
#allows for running 5 or 7 card hands
print h.has_flush(7) #T or F
print "Your hand is:"
print h.classify() #prints hand

######## Ex 9
import codecs
from operator import itemgetter

fp = codecs.open("ex9_courses.txt", encoding="utf-8")
fp.readline()
cis_list = []
for line in fp:
    line = line.strip()
    fields = line.split();
    course = fields[0]
    instructor = fields[1]
    semester = fields[2]
    tmp = {}
    tmp['course'] = course
    tmp['instructor'] = instructor
    tmp['semester'] = semester
    cis_list.append(tmp)
fp.close()
print cis_list

c_counts = {} #course counts
for d in cis_list:
    c = d['course']
    c_counts[c] = c_counts.get(c,0) + 1
    
ci_counts = {} #course instructor counts
for d in cis_list:
    c = d['course']
    i = d['instructor']
    ci_counts[(c,i)] = ci_counts.get((c,i),0) + 1

#items gives you both things in the dictionary in tuple form
sorted_c_counts = sorted(c_counts.items(), key=itemgetter(1),
                         reverse=True)

#iteritems will return an object, but is much faster
sorted_ci_counts = sorted(ci_counts.iteritems(),
                          key=itemgetter(1), reverse=True)

for (course,count) in sorted_c_counts:
    print course, count
    #inls523 4
for ((course,instructor), count) in sorted_ci_counts:
    print course, instructor, count
    #inls760 capra 3

print c_counts
#{u'inls760': 3, u'inls512': 1, u'inls523': 4,
#u'inls582': 1, u'inls509': 2}
print ci_counts
#{(u'inls523', u'boone'): 1, (u'inls512', u'haas'): 1,...
print sorted_c_counts
#[(u'inls523', 4), (u'inls760', 3), (u'inls509', 2),
#(u'inls512', 1), (u'inls582', 1)]
print sorted_ci_counts
#[((u'inls760', u'capra'), 3), ((u'inls509', u'arguello'), 2)...

######## Ex 10

import json
import re
from operator import itemgetter

#parse json data into list of dicts
fp = open('usagov_ex1.txt')
records = [json.loads(line) for line in fp]
fp.close()

urls = []
for rec in records:
    if 'u' in rec:
        urls.append(rec['u'])

url_counts = {}
for url in urls:
    match = re.search(r'://([^/]*)',url)
    #need to strip ://
    if match:
        new_url = match.group(1)
        url_counts [new_url] = url_counts.get(new_url, 0) + 1

sorted_url_counts = sorted(url_counts.items(),
                           key=itemgetter(1), reverse=True)
for url, count in sorted_url_counts[:10]:
    print url, count
    #www.nysdot.gov 836

######### Ex 11

from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

artist_list = {'David Bowie': {"August": 571, "Sept": 623,
                "Nov": 409}, 'The Beatles': {"August": 725,
                "Sept": 518, "Nov": 822}, 'New Order':
                {"August": 274, "Sept": 492, "Nov": 368}}

df = DataFrame(artist_list)
flipped = df.T
print "September sum"
print df.T['Sept'].sum() #1633
print "Bowie Sum"
print df['David Bowie'].values.sum() #1603

######## Ex 12
d = [[12,15,26], [2,0,4], [1,0,3], [3,0,4], [24,18,31],
    [8,12,5], [6,3,0], [8,14,27], [28,21,16]]

df = DataFrame(d, index=[['uid123','uid123','uid123',
        'uid345','uid345','uid345','uid678','uid678','uid678'],
    ['Bowie', 'Gaga', 'Spears', 'Bowie', 'Gaga', 'Spears',
     'Bowie', 'Gaga', 'Spears']], columns=['Aug','Sep','Nov'])

print df
                Aug  Sep  Nov
uid123 Bowie    12   15   26
       Gaga      2    0    4
       Spears    1    0    3
uid345 Bowie     3    0    4
       Gaga     24   18   31
       Spears    8   12    5
uid678 Bowie     6    3    0
       Gaga      8   14   27
       Spears   28   21   16
       
print df.sum(level=0)

        Aug  Sep  Nov
uid123   15   15   33
uid345   35   30   40
uid678   42   38   43

print df.sum(level=1)

        Aug  Sep  Nov
Bowie    21   18   30
Gaga     34   32   62
Spears   37   33   24

print df.sum(level=0).sum(axis=1)

uid123     63
uid345    105
uid678    123
dtype: int64



