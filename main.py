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

