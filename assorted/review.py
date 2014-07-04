####### List Comprehensions

#Create a list from a sequence based on a condition
#[<expr> for <item> in <seq> if <cond>]
a = [10, 20, 80, 90]
b = [n*2 for n in a]
#[20, 40, 160, 180]

c = [n*2 for n in a if n>50]
#[160, 180]

# list to include the squares of the even numbers b/w 1 to 11
even_squares = [x**2 for x in range(1,11) if (x**2) % 2 == 0]
#prints [4, 16, 36, 64, 100]

###### Dictionaries
#before
{'pears': 217, 'apples': 430, 'oranges': 523, 'bananas': 312}

inv['pears'] = 0
inv['bananas'] += 200
del inv['oranges']
#after
{'pears': 0, 'apples': 430, 'bananas': 512}

#dict operations
#items() returns k-v pairs as tuples
for (k,v) in inv.items():
    print k,v
    
for k in inv:
    print k, inv[k]

#in and not in
if 'bananas' in inv:
    print "We have ", inv['bananas'], 'bananas'
else:
    print "Yes sir! We have no bananas."
    
# .get()
#print inv['kiwi'] # error! print inv.get('apples')
print inv.get('kiwi')   #prints None
print inv.get('kiwi',0) #prints 0

###### JSON

j = json.loads(s)
print "Report date = ", j['reportDate']
if j['reportType'] == 'emprec':

##########Use of methods:

class Point:
    def __init__(self, initX, initY):
	self.x = initX
	self.y = initY
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFromOrig(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    # __str__ Special Method
    #py will automatically call this method if you print this obj
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
    #can invoke methods on halfway since it returns a NEW POINT
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx,my)

p = Point(3,4)
print p.getX()
print p.distFromOrig()

mid = p.halfway(q)
print mid.getX()
print p.halfway(q).getX()

#Objects as arguments:

    def distance(point1, point2):
        xdiff = point2.getX()-point1.getX()
        ydiff = point2.getY()-point1.getY()
        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

#references the methods above to get the point info
#and compute distance    
p = Point(3,4)
q = Point(0,0)
print distance(p,q)

######## Inheritance

#Allows use of <, >, == operators with objects
##Rules:Take two objects
##Return positive number if first is greater
##Return negative number if second is greater
##Return zero if both are equal

    def __cmp__(self, other):
        # check the ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

#Hand object inherits from Deck
class Hand(Deck):
    ''' Hand inherits from Deck. '''
    def __init__(self,label=''):
        self.cards = []
        self.label = label
        
mydeck = Deck()
print mydeck
mydeck.shuffle()
print mydeck

myhand = Hand('new hand')
mycard = mydeck.pop_card()
myhand.add_card(mycard)
print myhand.label
print myhand

#NEED TO LOOK AT THIS AGAIN
# in class Deck
def move_cards(self, hand, num):
    for i in range(num):
        hand.add_card(self.pop_card())

mydeck.move_cards(myhand,4)

########Algorithm Analysis
#Sum of integers

#Big-O
#So we had figured out the sumofn was T(n) = 1 + n
#As n gets large, the 1 does not matter so much
    #For n=4, the 1 is 20% of the steps
    #For n=400, the 1 is 0.25% of the steps
#Big-O drops the lower-order parts of T(n)

#sumofn() is said to be O(n)
def sumofn(n): s=0
    for i in range(1,n+1):
        s=s+i
    return s

#O() is the "order of magnitude"
if equation was T(n) = 4 + 2n + 7n^2:
    order of magnitude would be O(n^2)
    
########Sorting
#sort a list
a = [1,3,8]
a.sort()
print a

#sorted
sorted(a) #would print a sorted list
d={'d':3, 'b':2, 't':2}
sorted(d) #would sort they dict keys, but not values
#would print ['a', 'b', 't']

#this will return sorted list of tuples
#necessary since lower and upper case are assigned different vals
s = "This this IS is UNC unc"
print s.split()
print sorted(s.split())
def tolower(i):
    return str.lower(i)

for w in s.split():
    print tolower(w)

print sorted(s.split(), key=tolower)

#Itemgetter
#The itemgetter function in the operator module makes it each to
#access specific items to use as the sort key.

from operator import itemgetter
t = [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print sorted(t, key=itemgetter(0))


#######Data Analysis
#methods of pulling out tzs w/key = 'tz'
#First try:
tzs = []
for rec in records:
    tzs.append(rec['tz'])
#Longer version with a for loop:
tzs = []
    for rec in records:
        if 'tz' in rec:
            tzs.append(rec['tz'])
#Shorter version using list comprehension:
tzs = [rec['tz'] for rec in records if 'tz' in rec]

#3 methods of COUNTING tzs
tz_counts = {}
for tz in tzs:
    if tz in tz_counts:
        tz_counts[tz] += 1
    else:
        tz_counts[tz] = 1
print tz_counts['America/New_York']

tz_counts2 = {}
for tz in tzs:
    tz_counts2[tz] = tz_counts2.get(tz,0) + 1
print tz_counts2['America/New_York']

from collections import defaultdict
#using (int) will init new val of new ent to be int set to 0
#ex. could use (list) to init a new val to be an empty list
tz_counts3 = defaultdict(int)
for tz in tzs:
    tz_counts3[tz] += 1
print tz_counts3['America/New_York']

#collections.Counter
tzs2 = [rec['tz'] for rec in records if 'tz' in rec]
cc = Counter(tzs2)
cc.most_common(10)

######## NumPy

#creating ndarrays - created using array(), can be created
#from any sequence-like obj
t = [1,3,5]
a1 = np.array(t)
print a1
#array([1,3,5])

#ndim, shape, dtype
t2 = [[1,2,3],[4,5,6]]
a2 = nap.array(t2)
print a2
#array([1,2,3],
#      [4,5,6])
print a2.ndim
#2
print a2.shape
#(2L, 3L)
print a2.dtype
#dtype('int32')

#zeros, ones, empty
np.zeroes((1,3))
#array([[0., 0., 0.]])
a3 = np.ones((2,2))
#array([[1.,1.],
#       [1.,1.]])
np.empty((2,1))
#array([[3.58623],
#       [6.25723]])

#zeros_like, ones_like, arange
np.arange(7)
#array([0,1,2,3,4,5,6])
a4 = np.zeros_like(a3)
#array([[0.,0.]
#       [0.,0.]])

#identity
a5 = identity(5)
#array([[1.,0.,0.],
#       [0.,1.,0.]
#       [0.,0.,1.]])
a5.dtype
#dtype('float64')

#can specify dtype
np.array([1,2,3], dtype=float64) #would usually be 'int32'
#map to machine data types, which relates to processing speed

#Convert (cast) array from one type to another
#astype always creates new array (copy of the data),
#even if the data type is the same as the old type

           In [42]: a9
           Out[42]: array([ 1.2,  2.5,  3.7])
           In [43]: a9.dtype
           Out[43]: dtype('float64')
           In [44]: a10 = a9.astype(int32)
           In [45]: a10
           Out[45]: array([1, 2, 3])
           In [46]: a10.dtype
           Out[46]: dtype('int32')
           In [47]: a11 = a10.astype(float64)
           In [48]: a11
           Out[48]: array([ 1.,  2.,  3.])
           In [49]: a11.dtype
           Out[49]: dtype('float64')

#convert strings to numbers
In [50]: a12 = np.array(['1.2', '2.5', '3.7'],
           dtype=np.string_)
In [51]: a12
Out[51]:
array(['1.2', '2.5', '3.7'], dtype='|S3')
In [52]: a12.dtype
Out[52]: dtype('S3')
In [53]: a13 = a12.astype(float)
In [54]: a13
Out[54]: array([ 1.2,  2.5,  3.7])
In [55]: a13.dtype
Out[55]: dtype('float64')

#Arrays vs Lists
#arrays have built-in support for many common operations
#without having to use for loops

#in NumPy Array
In [65]: a1 = np.array([1,2,3])
In [66]: a1
Out[66]: array([1, 2, 3])
In [67]: a2 = a1 + 1
In [68]: a2
Out[68]: array([2, 3, 4])

#in List
In [56]: t1 = [1,2,3]
In [57]: t2 = []
In [58]: for i in t1:
    ...:     t2.append(i+1)
    ...:
In [59]: t2 Out[59]: [2, 3, 4]
    
#list comprehension
In [60]: t3 = [ i+1 for i in t1 ]
In [61]: t3
Out[61]: [2, 3, 4]
    
#More operations
#arrays & scalars
#vector operations
#ops b/w equal-sized arrays (elementwise)

In [69]: a1 = np.array([1,2,3]) In [70]: a1
Out[70]: array([1, 2, 3])
In [71]: a2 = a1 * a1
In [72]: a2
Out[72]: array([1, 4, 9])
In [73]: a3 = a1 * 2
In [74]: a3
Out[74]: array([2, 4, 6])
In [75]: a4 = a1 ** 2
In [76]: a4
Out[76]: array([1, 4, 9])

#1-dim indexing and slicing
Out[78]: array([0, 1, 2, 3, 4, 5, 6])
In [79]: a1[2]
Out[79]: 2
In [80]: a1[3:5]
Out[80]: array([3, 4])
In [81]: a1[:3]
Out[81]: array([0, 1, 2])

#Broadcasting - changes the array
In [82]: a1 = np.arange(10)
In [83]: a1
Out[83]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
In [84]: a1[3:5] = 99
In [85]: a1
Out[85]: array([ 0, 1, 2, 99, 99, 5, 6, 7, 8, 9])
In [86]: a1[:3] = 44
In [87]: a1
Out[87]: array([44, 44, 44, 99, 99, 5, 6, 7, 8, 9])

#array slices are VIEWS into orig array, not copy like list slice
In [90]: a1 = np.arange(10)
In [91]: a1
Out[91]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
In [92]: fred = a1[3:7]
In [93]: fred
Out[93]: array([3, 4, 5, 6])
In [94]: fred[:3] = 99
In [95]: fred
Out[95]: array([99, 99, 99,  6])
In [96]: a1
Out[96]: array([ 0, 1, 2, 99, 99, 99, 6, 7, 8, 9])

#Copy a slice - can EXPLICITLY do this
a1 = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
In [99]: fred = a1[3:7].copy()

#higher dimension indexing
In [105]: a1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
In [106]: a1
Out[106]:
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
In [107]: a1[1]
Out[107]: array([4, 5, 6])
In [108]: a1[1][1]
Out[108]: 5
In [109]: a1[1,1]
Out[109]: 5

#can copy items from array to local var and save for later use/
#can reimplement it after you altered data to revert to normal

#Boolean Indexing will cross reference two arrays and return bool T/F
#can also use with operations like in project
In [129]: names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will',
                            'Joe', 'Joe'])
In [130]: names
Out[130]: array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'],
dtype='|S4')
In [131]: rdata = randn(7,4)
In [132]: rdata
Out[132]:
#array([[lost of random numbers]])
In [133]: names == 'Bob'
array([ True, False, False, True, False, False, False], dtype=bool)
In [135]: rdata[names == 'Bob']
Out[135]:
array([[-0.50616171, -0.22846826, -0.42737071, -0.63261581],
[ 0.17286501, -0.01831906, 0.23977178, -0.47188809]])
In [136]: rdata[names == 'Bob', 2:] Out[136]:
array([[-0.42737071, -0.63261581],
[ 0.23977178, -0.47188809]])

######## pandas

#floating-point numbers as base 2 (binary) fractions

#format
("{0:.2f}".format(a))

#Series
#one-dimensional data structure
#contains an array of data & associated array of labels called INDEX

#no index specified in this example - default to integer index
In [40]: s = Series([31, 25, 18])
In [41]: s
Out[41]:
0    31
1    25
2    18
dtype: int64
In [42]: s.values
Out[42]: array([31, 25, 18], dtype=int64)
In [43]: s.index
Out[43]: Int64Index([0, 1, 2], dtype=int64)

#Specify series index
s = Series([31, 25, 18], index=['inls285', 'inls382', 'inls523'])
In [47]: s.index
Out[47]: Index([u'inls285', u'inls382', u'inls523'], dtype=object)

#Examples of series operations and indexing
# + - * add series together, > <
#examples in exercises and project
In [61]: s13 + 1
Out[61]:
inls285 32
inls382 26
inls523 19
dtype: int64

#Series from Dicts
#can be used like ordered dict
#map index vals to data vals
In [68]: d = {'a': 5, 'b': 10, 'c': 15}
        In [69]: s = Series(d)
In [70]: d
Out[70]: {'a': 5, 'b': 10, 'c': 15}
In [71]: s
Out[71]:
a   5
b   10
c   15
dtype: int64
In [72]: if 'a' in s:
    ...:     print s['a']
5

#indexing and missing data
In [73]: d = {'a': 5, 'b': 10, 'c': 15}
#says to make these letters the index of the series
In [74]: t = ['b', 'c', 'd']
In [75]: s = Series(d, index=t)
#prints NaN for d since wasn't in the dict - it put it there,
#but no associated num
#NaN only suppored for floats, otherwise would have used ints
In [76]: s
Out[76]:
b    10
c    15
d   NaN
dtype: float64

#Can name series and index
In [78]: s14.name = "Spring 2014"
In [79]: s14.index.name = "Course names"
In [80]: s14
Out[80]:
Course names
inls285 29
inls382 23
inls523 14
Name: Spring 2014, dtype: int64

#index can be changed by assignment
s14.index = ['INLS 284', 'INLS 323', 'INLS 623']

In [33]: type(df)
Out[33]: pandas.core.frame.DataFrame

#Columns are retrieved as a Series
#Retrieve columns by dict-like notation, or by attribute

In [35]: s = df['course'] #or df.course
In [36]: type(s)
Out[36]: pandas.core.series.Series

In [37]: s
Out[37]:
0 inls285
...
5 inls523
Name: course, dtype: object

#can create custom index for DataFrame
#assuming series d

In [43]: df = DataFrame(d, index=['c1234', 'c2345', 'c8822',
                                  'c7654', 'c5512', 'c4321'])
In [44]: print str(df)
        course enrollment semester
c1234  inls285         31      s13
c2345  inls285         58      s14

#Columns are retrieved as a Series w/ same index as DF

#Retrieve Rows using .ix
In [55]: s = df.ix['c1234']
In [56]: type(s)
Out[56]: pandas.core.series.Series

#row is retrieved as Series whose index is the columns of the DF
In [57]: s
Out[57]:
#s.index    #s.values
course        inls285
enrollment         31
semester          s13
Name: c1234, dtype: object

#can create a new column and assign values to it
df['tmp'] = [1, 3, 5, 7, 8, 9]

#dict of dicts
In [76]: d = {'unc': {2012: 4.1, 2013: 4.3, 2014: 4.5},
    'duke': {2012: 3.8, 2013: 3.8, 2014: 4.1}}
In [77]: df = DataFrame(d)
In [79]: print str(df)
    duke unc
2012 3.8 4.1
2013 3.8 4.3
2014 4.1 4.5

#DF columns can be extracted and operated on as either
#Series or numpy arrays
In [96]: s = df.unc
In [97]: type(s)
Out[97]: pandas.core.series.Series
In [98]: a = df.unc.values
In [99]: type(a)
Out[99]: numpy.ndarray
#will sum the series or the each as numpy item
In [100]: s.sum()
Out[100]: 12.899999999999999
In [101]: a.sum()
Out[101]: 12.899999999999999

#getting specific elements from dfs
#Columns
##The first [], using the column name: df['unc']
##Or can be accessed as an attribute: df.unc
#Rows
##The second [], using the row name: df.unc['oct']
##The second [], using the row position: df.unc[1]

#can do arithmetic between df and series
In [158]: d = {'unc': 0.4, 'duke': 0.8, 'ncstate': 0.6}
In [159]: s = Series(d)
In [160]: s Out[160]:
duke    0.8
ncstate 0.6
unc     0.4
dtype: float64
In [161]: print str(df - s)
    duke  ncstate  unc
2012 3.0      3.3  3.7
2013 3.0      3.2  3.9
2014 3.3      3.7  4.1

#sorting by row or column index
#           rows to get in order      cols to get in order
df2 = df.ix[[2014, 2012, 2013], ['unc', 'duke', 'ncstate']]
str(df2.sort_index()) #changes back to 2012, 13, 14
str(df2.sort_index(axis=1) #sorts the cols in alpha order
    
#can sum(), mean(), and idxmax() on df, index, col, or row
In [51]: df.sum(axis=1)
Out[51]:
2012     7.9
2013    11.9
2014    12.9
dtype: float64

In [52]: df.idxmax()
Out[52]:
duke       2014
ncstate    2014
unc        2014
dtype: int64

#sorting a series
s = Series([6, 2, 8, 4], index=['b', 'd', 'a', 'c'])
s.sort_index() #sort by index
s.order() #sort by values

In [26]: print df.sort_index(axis=1, ascending=False)
#axis=1 sorts the col index, then reverse b/c ^
    cb ca
ie   6  7

#can sort by column
In [29]: print df.sort_index(by='cb')
    ca  cb
ia   3   2
ic   5   4
ie   7   6
ib   1   8

#sort by multiple columns
In [33]: print df.sort_index(by=['a','b'])
    a   b
3   1   6
2   1   8
0   5   2
1   7   4

#Partial Hierarchical indexing
In [11]: s
Out[11]:
a   x   8
    y   2
b   x   5
    y   9
c   x   4
    y   7
d   x   5
    y   3
dtype: int64

In [13]: s['b':'c']
b   x   5
    y   9
c   x   4
    y   7

In [14]: s.ix[['a','c']]
a   x   8
    y   2
c   x   4
    y   7

#by secondary index
In [17]: s[:,'y'] 
a   2
...
d   3

#unstack() takes off secondary index / stack() makes it again

#multiple hierarchical example
In [33]: df = DataFrame(d, index=[['a','a','b','b'], [1, 2, 1, 2]],
                    columns=[['unc','unc','duke'], ['x','y','x']])
In [34]: print df
        unc     duke
        x   y      x
a   1   0   1      2
    2   3   4      5
b   1   6   7      8
    2   9  10     11
    
#summary statistics by LEVEL
In [43]: print df.sum(level=0)
        unc     duke
        x   y      x
a       3   5      7
b      15  17     19

print df.sum(level=1)
    unc         duke
       x   y      x
   1   6   8     10
   2  12  14     16

print df.sum(level=0, axis=1)
        duke     unc
a   1      2       1
    2      5       7
b   1      8      13
    2     11      19
    
print df.sum(level=1, axis=1)
        x   y
a   1   2   1
    2   8   4
b   1  14   7
    2  20  10   

#reset_index() will rem hierarchical-prints all multiples in index

######## Data Aggregation

#merge
#will auto merge on column if possible
print pd.merge(stats_df, city_df)

#to merge on index
print pd.merge(stats_df, city_df, left_index=True, right_index=True)

#to merge one on index and one on col
print pd.merge(stats_df, city_df, left_index=True, right_on='team')

#can use merge to filter
z = city_df[:3] #will only get first three rows
#merge will only merge the entries in z, so will only have 3

#can do summary stats two ways, print same
df['enroll'].sum(level=0)
df.sum(level=0)['enroll']

# GroupBy

#.groupby() on a DataFrame returns a GroupBy object
#GroupBy objects have methods such as .sum() and .mean()
In [84]: print df
    course  sem  enroll  assign
0  inls101  f12      12       3
1  inls161  f12      18       4
...
In [85]: g = df['enroll'].groupby(df['sem'])
In [86]: print g
<pandas.core.groupby.SeriesGroupBy object at 0x0000000011422860>
In [87]: print g.sum()
sem
f12 45
f13 57
dtype: int64

In [95]: print type(g.sum())
<class 'pandas.core.series.Series'>
In [103]: print g.sum().index
Index([u'f12', u'f13'], dtype=object)

#groupby multiple columns, when you perform an operation such
#as .sum(), the result will have a hierarchical index
In [97]: g = df['enroll'].groupby([df['sem'], df['course']])
In [98]: print g.sum()
sem  course
f12  inls101    12
     inls161    18

print g.sum().index
#Will return 'MultiIndex' of a list of tuples (u'sem', u'course')

#groupby unstack() basically df.T
print g.sum().unstack()
course  inls212 inls234
sem
f12          12       2
f13          11       8

print g.sum().unstack()['inls212']['f13'] #prints a value

print df.groupby(df['sem']).sum()
print df.groupby('sem').sum() #shorthand - print same
    enroll  assign
sem
f12     33      14
f13     22      44


#cannot do this b/c it is not now looking for 'sem' w/in the enroll
#column need to go back up a level to find the df's 'sem' col
print df['enroll'].groupby('sem').sum() #DOESN'T WORK

#can do
print df['enroll'].groupby(df['sem']).sum() #most sense
print df.groupby('sem').sum()['enroll']
df.groupby('sem')['enroll'].sum()
sem
f12     33    
f13     22
#pandas.core.series.Series

#joining
In [212]: print z
course
inls161    37
inls382    36
Name: enroll, dtype: int64

In [213]: zdf = DataFrame(z.values, index=z.index)
In [214]: print zdf
          0
course
inls161  37
inls382  36

In [215]: zdf.columns = ['enroll'] #etc...

In [218]: y = DataFrame(['Tools', 'InfoSys'],
                index=['inls161', 'inls382'])
In [219]: print y
               0
inls161    Tools
inls382  InfoSys
In [220]: y.columns = ['coursename'] #etc...

In [222]: zdfy = zdf.join(y)
In [223]: print zdfy
        enroll  coursename
course
inls161     37       Tools
inls382     36     InfoSys

###### RegEx

import re
astring = "uncle"
match = re.search(r'unc', astring)
if match:
    print 'found = ', match.group()
else:
    print 'not found'

# RegEx examples
c = "on March 9, 1995"

match = re.search(r'19\d\d',c)
#prints 1995
match = re.search(r'1?9',c)
#prints the first 9
match = re.search(r'^March',c)
#doesn't find since March not first

#leftmost & largest
#find the leftmost match for the pattern, then try to use
#as much of the string as possible ('greedy')
9+ one or more 9s
9* zero or more 9s
9? zero or one 9s

a = "199987659955"
match = re.search(r'9+',a)
#prints 999
match = re.search(r'19*',a)
#prints 1999
match = re.search(r'9*',a)
#prints blank
match = re.search(r'9+.*9+',a)
#prints 999876599

match = re.search(r'pi+', 'piiig')
#prints piii
match = re.search(r'i+', 'piigiiii')
#prints ii
match = re.search(r'\d\s*\d\s*\d', 'xx1 2    3xx')
#prints 1 2    3
match = re.search(r'\d\s*\d\s*\d', 'xx12 3xx')
#prints 12 3
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
#prints 123

#Matching Alternatives
#Square brackets - any listed char can match
##[ab] means either a or b can match
##[a-d] matchesaorborcord
#Use caret for negation
#[^a-d] matches any char except a, b, c, or d

a = "A765-2781-ZFQ"
match = re.search(r'([AB])([0-9]+)-([0-9]+)\
                  -([A-Z0-9]+)',a)
print match.group() #A765-2781-ZFQ
print match.group(1) #A
print match.group(2) #765
print match.group(3) #2781
print match.group(4) #ZFQ

a = "crate"
b = "state"
match = re.search(r'(cr|st)ate',a)
#prints crate
match = re.search(r'(cr|st)ate',b)
#prints state















