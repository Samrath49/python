# Printing string by ending line first using '\' and then whole string 
'''print("""\
Decoder:-
1 ~ 32bit
2 ~ 64bit
    """)'''
''' 

# ````List````

sa = ['s',24,'harsh',"$$",17]
# print(sa[2:])
# sa[0] = 'h'
# print(sa)
sa + [1,2,4,4] #sa + [1,2,4,4]  output at cmd = ['s', 24, 'harsh', '$$', 17, 1, 2, 4, 4]
print(sa)
'''
'''
x = [1,2,3]
z = ['a','b','c']
y = [x,z]
print(y[1][2])
'''
'''
sa = ['ss', 66, 'harsh', "$$", 17]
sa[2:4] = []
print(sa)
sa[:] = []
print(sa)'''

'''

# ```IF else statements```

x = int(input("Enter a number: "))
if x < 0:
    x = 0
    print("x changed to 0")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")'''
    
''' 
name = str(input("Eneter name: "))
if name == "sam":
    print("yeah")'''

'''

# `````For statements`````

words = ['cat', 'bat', 'rat', 'tat', 'sat']
for w in words:
    print(w, len(w))'''
'''
i = [1,2,3,4,5,6]
for j in i:
    print(j, bin(j))
'''

''' Method to modify and loop through collection by iterating over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
'''

''' Method to modify and loop through collection by iterating over a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
'''
'''
for i in range(2,10,2):
    print(i)

for i in range(-10, -100, -30):
    print(i)
'''
'''
a = ['Marry','had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i]) 
print(range(2,10))
'''
'''
total = sum(range(1,100))
print(total)

a = list(range(1,20,1))
print(a)
'''

'''# Break and Continue Statements with else clause
for n in range(1,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # if there is no factor then its a prime
            print(n, 'is a prime number')'''

# Break 
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
'''

# Continue
'''
for num in range(2, 10):
    if num % 2 == 0:
        print("Oh yeah a even no",num)
        continue
    print("No luck, found a no", num)
'''

# pass Stataement
'''
sad = True
while True:
    pass
'''
'''
class MyEmptyClass:
    pass
'''
'''
def initlog(*args):
    pass
'''
'''
def fib(val):
    # To print fibonacci series upto n
    a,b = 0,1
    while a < val:
        print(a, end=' ')
        a,b = b,a+b
    print()
fib(200)
'''
# one can also use the mechanisum to rename a fxn
'''
f = fib
f(100)
'''
# None as default returning type of the function
'''
def fib(n):
    a = 18
    totoal = a + n
    print(totoal)
fib(0)
print(fib(0))
'''
# Its easy to return a list of values than printing it
'''
def fib2(val):
    a,b = 0,1
    result = []
    while a < val:
        result.append(a)
        a,b = b,a+b
    return result
fibcall = fib2(100)
print(fibcall)
'''

# Default arguments in function with the use of in keyword
'''  
def ask_ok(prompt, retries = 4, remainder = 'Please try again' ):
    while True:
        ok = input(prompt)
        if ok in('y', 'ye', 'yes'):
            return True
        if ok in('n', 'no', 'nopes'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(remainder)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
'''

# USing default values as args
'''
val = 27
def f1(arg = val):
    print(arg)

val = 37
f1()'''

# Using default values in mutable list datatype in fxn
'''
def f9(a, l = []):
    l.append(a)
    return l
print(f9(1))
print(f9(2))
print(f9(3))'''

# Using none as default values
'''
def f9(a, l = None):
    if l == None:
        l = []
    l.append(a)
    return 
print(f9(1))
print(f9(2))
print(f9(3))
'''

# Keyword arguments
'''
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do u have any", kind, '?')
    print("-- I m sry sir, we r all out of ",kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "Its very very runny,sir.",
            "Its really very, VERY runny, sir.",
            Shopkeeper = "Michel Palin",
            Client = "John Cleese",
            Sketch = "Cheese Shop Sketch")
'''

# Function examples Proving positional only and othe parameters types using / and *
'''
def standard_arg(arg):
    print(arg)
standard_arg(2)

def pos_only_arg(arg, /):
    print(arg)
pos_only_arg(2) # as it is a postition only so if i pass (arg = 2) it will give me error of unexpected keyword argument
 
def kwd_only_arg(*, arg):
    print(arg)
kwd_only_arg(arg = 2) # as it is only keyword agr if i pass (2) it will give error
'''
# Arbitrary Argument Lists
'''
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
'''   
# Lambda Function
'''
def make_increment(n):
    return lambda x: x + n

f = make_increment(42)
print(f(0))

print(f(1))
'''
# Documentation Strings (Copy paste mariya)
'''
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
'''
#**#**  5 Data Structures

# More on lisits and every method
'''
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('pear'))
print(fruits.index('banana',4))
fruits.reverse()
fruits.append('mango')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)
'''
# Using lsit as stacks
'''
stack = [1,2,3,4,5,6]
stack.append(7)
stack.append(8)
stack.reverse()
stack.pop()
stack.sort()
print(stack)
'''
# Implementation of queue
'''
from collections import queue
queue = deque(['Eric','John','Shawn','Michel'])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
print(queue)
'''
# 5.1.3 List Comprihensions
'''
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# Second approach
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# 3rd and best approach
squares = [x**2 for x in range(10)]
print(squares)
'''
'''
comprihension = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(comprihension)
'''
'''
vec = [-4, -2, 0, 2, 4]
vec1 = [x*2 for x in vec]
print(vec1)
vec2 = [x for x in vec if x>=0]
print(vec2)
vec3 = [abs(x) for x in vec]
print(vec3)
'''
'''
freshfruit = ['   banana','   loganberry',' passion fruit ']
un = [weapon.strip() for weapon in freshfruit]
print(un)

numnSq = [(x, x**2) for x in range(6)]
print(numnSq)

# flatten a list using listcomp with two 'for'
vec = [[1,2,3],[4,5,6],[7,8,9]]
ou = [num for elem in vec for num in elem]
print(ou)

'''
# 5.1.4 Nested List Comprihensions
'''
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
'''
#print(matrix)

'''
transpose = [[row[i] for i in matrix] for i in range(4)]
print(transposep)

#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]] gives output if we run on idle
'''
# 5.2 The del statement 
'''
a = [-1,1,66.25, 333, 1234.567]
del a[0]
print(a)
del a[:3]
print(a)
del a[:]
print(a)
'''
# 5.3 Tuples adnd Sequences
'''
t = 12345,54321,13542,'Hello! Tupple' # example of tuple unpacking

print(t[3])

print(t)

u = t,(11,22,33,44,55)
print(u)

v = ((1,2,3,4),(1,2,4,4))
print(v)

empty = () # empty tuple
print(len(empty))

sigleton = 'hello', # comma says its a tuple with only one value
print(len(sigleton))
print(sigleton)
'''

# 5.4 Sets
'''
basket = {'Apple','mango','Banana','Grapes','mango','Apple','Oranges','Papaya','Watermelon','Pomegrand'}
print(basket)

print(set(basket))

a = set('abdakadabra')
b = set('giliabragilishu')
print(a-b) # elements of a not in b
print(a|b) # elements of a or b or both 
print(a&b) # elemnts of a which are also in b i.e common
print(a^b) # elements of a or b but not in both

a = {x for x in 'assadjasdajsd' if x not in 'abs'}
print(a) 
'''
# 5.5 Dictionaries
'''
tel = {'jack':4098, 'saep':4139}
tel['guideo'] = 4127
print(tel) 

del tel['saep']
tel['irv'] = 4421
print(tel)
print(list(tel))
print(sorted(tel))
print('irv' not in tel)

sa = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # dict method just converts the list given in tuple as dictionary and makeing key val pairs
print(sa)

ss = {x:x**2 for x in (2,4,6)}
print(ss)

pap = dict(sape=4139, guido=41312,kjack=30330)
print(pap)
'''

# Looping techniques
'''
knights = {1 : 'rohit', 2: 'kalu', 3: 'sahil', 4: 'laddo'}
for k,v in knights.items():
    print(k,v)

for i,v in enumerate(['like','my','dog']):
    print(i,v)

questions = ['name','age','fav color']
answers = ['Sam','22','White']
for q,a in zip(questions,answers):
    print('What is ur {0}? It is {1}.'.format(q,a))

for i in reversed(range(1,10,2)):
    print(i)

basket = ['apple','mango','grapes','mango','grapes','apple']
for i in sorted(set(basket)):
    print(i)

import math
raw_data = [56.2, float('NaN'), 51.7, 52.5, float('NaN'),47.8]
filtered_data = []
for values in raw_data:
    if not math.isnan(values):
        filtered_data.append(values)
print(filtered_data)
'''
# 5.7 More on Conditions
'''
The conditions used in while and if statements can contain any operators, not just comparisons.
'''
# 6 Modules
#Creating different files.
# Code is present on fibo.py and modimpoter.py

# 7 In nd Out

# 7.1 fancier output formatting
'''
year = 2020
event = 'Corona'
print(f'Result of {year} {event} is death')

s = 'Hello world'
print(str(s))

repr(s)
print(str(1/7))
'''

# 7.1.1 Formatted String Literals
'''
import math
print(f'The value of pie is approximately {math.pi:.3f}.')

game = {'Best' : 'Valorant', 'Favorite': 'Valorant', 'So_Ezz': 'Valorant'}
for key, var in game.items():
    print(f'{key} ==> {var}')
'''

# 7.1.2 The Stirng format() Method
'''
print('We are the {} who say "{}!"'.format('knights','Ni'))
print('We are the {0} who say "{1}!"'.format('knights','Ni'))
print('We are the {1} who say "{0}!"'.format('knights','Ni'))
print('We are the {player} of "{CSGO}!"'.format(player = 'agents', CSGO = 'Valorant'))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
'''

# 7.1.3. Manual String Formatting

'''
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3),end = ' ')
    print(repr(x*x*x).rjust(4))
'''

# 7.2 Reading and Writing files
'''
with open('read') as f:
    read_data = f.read()
'''
'''
fw = open('read.txt','r+')
print(fw.read())
#print(fw.write('Some random text'))
fw.close()
'''

# 7.2.1 Methods of File Object

'''
fw.read() reads entier file
fw.readline() read one line
to read multiple lines loop

for lines in fw:
    print(line,end = '')
'''

# 7.2.2 Saving structures data with json

'''
Passing 123 in read will have to call another method i.e int() to
read it and then converted to string, so we have to spend more time
to do that. But python offers json file type which will convert python
datatypes into strings easliy
'''

# 8 Errors and Exceptions

# 8.1 Syntax Error

# 8.2 Exceptions
'''
Errors detected during execution are called exceptions
'''

# 8.3 Handling Exceptions
'''
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Opps not a number dude")
'''

# 8.4 Raising Exceptions
'''
raise NameError('HiThere')

try:
    raise NameError('Sam')
except NameError:
    print('An exception flew by')
    raise
'''

# 8.5 User-Defined Exceptions
'''
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
'''

# 8.6 Defining Clead-up Actions
'''
try:
    raise KeyboardInterrupt
finally:
    print("Goodbye World!")

def bool_return():
    try:
        return True
    finally:
        return False
print(bool_return())
'''
'''
def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by 0!")
    else:
        print("result is", result)
    finally:
        print("execution finally clause")

divide(2,1)
'''

# 8.7 Predefined Clean-up Actions 

# 9.0 Classes

# 9.1 A word about Names and Objects

# 9.2 Python Scopes And Namespaces

# 9.2.1 Scopes and Namespaces Examples
'''
def scope_test():
    def do_local():
        spam = 'local spam'
    
   def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
    
    def do_global():
        global spam
        spam = 'gloabal spam'
    
    spam = 'test spam'
    do_local()
    print("After local assignment: ", spam)
    do_nonlocal()
    print("After nonlocal assignment: ", spam)
    do_global()
    print("After global assignment: ", spam)

scope_test()
print("In global scope: ", spam)
'''

# 9.3 A FIrst Look at Classes

# 9.3.1 Class Defination Syntax

# 9.3.2 Class Objects
'''
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    
x = Complex(3.0, -4.5)
print(x.r,x.i)
'''

# 9.3.3 Instance Objects

# 9.3.4 Methods Objects

# 9.3.5 Classes and Intance Variables
'''
class Dog:
    kind = 'Akita'

    def __init__(self, name):
        self.name = name

d = Dog('Fiddo')
e = Dog('Cheeto')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)


class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name
    
    def addtricks(self, tricks):
        self.tricks.append(tricks)

a = Dog('Bruno')
b = Dog('Buddy')
a.addtricks('RollOver')
b.addtricks('FetchBall')
# incorrect as it gives a.tricks and b.tricks so we will use instance variabel
print(a.tricks)

'''
'''
# Correct way using instance variable
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)

d = Dog('Bruno')
e = Dog('Buddy')
d.add_tricks('Playing with ball')
e.add_tricks('Fetching ball')
print(d.tricks)
'''

# 9.4 Random Remarks

# 9.5 Inheritance

# 9.5.1 Multiple Inheritance

# 9.6 Private Variables

# 10

# 10.1 Operating system interface
'''
import os

print('Disrector is '+ os.getcwd())  # to get the directory
print(dir(os))
print(help(os))

import shutil # use shutil for file related tasks
'''

# File Wildcards
'''
import glob
print(glob.glob('*.py'))
'''

# 10.4 Error Output Redirection & Program Termination

# 10.5 String Pattern Matching
'''
import re
print(re.findall(r'\bf[a-z]*','which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
'''

# 10.6 Mathematics
'''
import math
print(math.cos(math.pi / 4))
print(math.log(1024,2))

import random
print(random.choices(['apple','pear','banana']))
print(random.sample(range(100),10))
print(random.random())
print(random.randrange(10))

import statistics
data = [2.75, 1.25, 3.55, 0.5, 2.98, 9.2, 1.19, 3.98]
print(statistics.mean(data))
print(statistics.mean(data))
print(statistics.variance(data))
'''

# 10.7 Internet Access

# 10.8 Dates and Times
'''
from datetime import date
now = date.today()
print(now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1998, 12, 16)
age = now - birthday
print(age)
'''

# 10.9 Data Compression

# 10.10 Performace Measurement
'''
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
'''

# 10.11 Quality Control (Unit testing)
'''
def average(values):
    return sum(values) / len(values)

import doctest
doctest.testmod()
 
import unittest
class TestStaticsticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
unittest.main()
'''
# 10.12 Batteries Included

# 11 Brief Tour of the standard library 

# 11.1 Output Formatting 
'''
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
'''
'''
import pprint
t = [[[['black','cyan'],'white', ['green','red']], [['magenta','yellow'],
'blue']]]

pprint.pprint(t,width=30)
'''
'''
import textwrap
doc = """The wrap() method is just like a fill() except that it returns
a list of strings instead of one big string with newlines to seprate 
the wrapped lines."""

print(textwrap.fill(doc, width = 40))
'''

# 11.2 Templating
'''
from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village = 'Nottingham', cause = 'the ditch fund'))
'''

# 11.3 Working with Binary Data Record Layouts

# 11.4 Multi-threading
'''
import threading, zipfile
class AsynZip(threading, Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished in background zip of: ', self.infile)

backgroud = AsynZip('mydata.txt', 'myarchive.zip')
backgroud.start()
print('The main program continues to run in forground.')

backgroud.join()
print('Main program waited untill background was done.')
'''

# 11.5 Logging

# 11.6 Weak References 
'''
import weakref, gc
class A:
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return str(self.value)
'''

# 11.7 Tools for Working with lists
'''
from array import array
a = array('H', [4000,10,700,22222])
print(sum(a))
print(a[1:3])

from collections import deque
d = deque(["task1","task2","task3"])
d.append("task4")
print('All tasks', d)
print('Handling',d.popleft())


import bisect
scores = [(100,'perl'),(200,'tcl'),(400,'lua'),(500,'python')]
bisect.insort(scores,(300,'ruby'))
print(scores)


from heapq import heapify, heappop, heappush
data = [1,3,4,5,7,8,3,2,4,0]
heapify(data)
heappush(data,-5)
print([heappop(data) for i in range(3)])
'''

# 11.8  Decimal Floating point arithemetic
'''
from decimal import *
round(Decimal('0.70') * Decimal('1.05'),2)
print(Decimal('0.74'))
print(round(.70 * 1.05,2))

print(Decimal('1.00') % Decimal('.10'))
getcontext().prec = 36
print(Decimal(1) / Decimal(7))
'''

# 12 Virtual Eni=vironments and Packages

# 12.1 Introduction

# 12.2 Creating Virtual ENvirornments

# 12.3 Merging Packages with pip

# 13 What now?

# 14 Interactive Input Editing and History Susbstitution

# 14.1 Tab Completion and History Editing

# 14.2 Alternatives to the Interactive Interpreter

# 15 Floating Point Arithemetic : Issues and Limitatiton

# 16