print(5)
nums = [1,"prem"]
print(nums)
nums.remove(1)
print(nums)
nums.remove("prem")
print(nums)
nums.extend([44,43,234])
print(nums)
nums[4:]
print(nums[7:])
del nums[2:]
print(nums)
tup = (21,36,14)
print(tup)
set = {1,"hello"}
print(set)
set.add("hey")
print(set)
dictionary = {1:"hello",2:"hi"}
print(dictionary)
dictionary[2]
print(dictionary[2])
print(dictionary.get(5,"not found"))
key = ['1','2']
values = ["one","two"]
data = dict(zip(key,values))
print(data)
num = 3.5
type(num)
print(type(num))

a="lol"
b=a
b='lol'
print(id(a),id(b))
print(a,b)
listWithRange = list(range(3,10,2))
print(listWithRange)
print(int(5/3))
a=7
b=3
a=b
b=a
'''
print(a)
print(b)
'''
#x=input()
#x=int(x)
#y=input()
###z=x+y
#print(z)
if False:
    print('hi')
print('hello')
if True:
    print(1)
else:
    print(2)
if True:
     print(3)
     if True:
        print(5)
     elif True:
         print(6)
i=1
while i<5:
    print(i)
    i+=1
x = [5,6,3]
for i in x:
    print(i)

a = [3,6,4,3]
#a.remove(3)
print(a)
#a.__delitem__(0)
print(a)
a.remove(3)
print(a)
a = 1
while( a < 10):
    if(a%2):
        pass
    else:
        print("pre")
        #print("tis o odd")
    a+=1
a=1
while( a < 10):
    a+=1
    if(a%2):
        continue
    print("tis o  odd")
nums1 = [10,23,56,22]
for num in nums1:

    if num % 5 == 0:
        print(num)
        break
else:
    print("notf ound")

#import array as arr
#arr.array()
from array import *
vals = array('i',[5,6,7,8])
print(vals)
vals.buffer_info()
print(vals.buffer_info())
print(vals.typecode)
print(vals[0])
for i in range(4):
     print(vals[i])
for e in vals:
    print(e)
newArr = array(vals.typecode,(a for a in vals))
print(newArr)
array1 = array('i',[])
'''
lengthOfArray1 = int(input("enter length of the array"))
for i in range(lengthOfArray1):
    x = int(input("enter the value"))
    array1.append(x)
print(array1)'''
##matrix multiplication s with numpy need to impart from tut 35
#functions

def greet():
    print("hello")
    print("enter")
greet()
def add(x,y):
    c = x+y
    d = x-y
    return c,d

c,d= add(5,8)
print(c,d)

def update(x):
    x = 8
    print(x)
a = 10
update(a)
print(a)
def person(name, **data):
    print(name)
    for i,j in data.items():
       print(i,j)
person('perm',age=24,village = 'guntur')
l = 10
def something():
    global l
    l = 49
    print(l,"inside")
something()
m=45
print(l,"outside")
def something1():
    x = globals()['m']
    globals()['m'] = 46
    m=47
    print(m)
something1()
print(m)
list3 = [20,421,654,234,12,64,63]
def countOfList(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
even,odd = countOfList(list3)
print(even,odd)

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n):

        c = a+b
        a=b
        b=c
        print(c)
fib(10)
#recursion calling fuction itself
f = lambda a : a*a
print(f(5))
nums2 = [3,5,7,3,2,5,3,2]
def is_even(n):
    return n%2==0
evens = list(filter(is_even,nums2))
print(evens)
odds = list(filter(lambda n : n%2==1,nums2))
print(odds)
doubles = list(map(lambda n:n*2,odds))
print(doubles)
from functools import reduce
sum = reduce(lambda a,b:a+b,doubles)
print(sum)
#decorators
def div(a,b):
    print(a/b)
def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div = smart_div(div)
div(3,5)
from calc import add
def fun1():
    print("func1")
def fun2():
    print("func2")
def main1():
    fun1()
    fun2()

class Computer:

    def __init__(self):
        print(345)

    def config(self):
        print("i5")
    def main2(self):
        print("main1 in computer")

com1 = Computer()
com1.config()
com1.main2()
class Comptuer2:
    g = 9
    def comp2(self):
        print("comp2")
    def __init__(self,cpu,ram):
        print(9)
        self.cpu = cpu
        self.ram = ram
        self.g = 10
    def config(self):
        print(self.cpu,self.ram)
s = Comptuer2(cpu=4,ram=6)
s.config()

class Computer3:
    def __init__(self):
        self.name = "name"
        self.age = 65
    def update(self):
        self.age = 67


c3 = Computer3()
c4 = Computer3()
c4.name = "prem"
print(c3.age)
print(c4.name)
c4.update()
print(c4.update())
print(c4.age)
class Car:
    wheels = 4
    def __init__(self):
        self.mil = 10
        self.company = "bmw"


car1 = Car()
Car.wheels = 5
Car.mil = 11
print(car1.company)
car2 = Car()
print(car2.wheels)
print(car2.mil)
car2.mil = 11
print(car2.mil)
#Types of methods

class Student:
    school = 'Telusko'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.Laptop()
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def info1(cls):
        print('im in info1')
        return cls.school
    @staticmethod
    def info1():
        print("This is student class in staic method")
    def show(self):
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand = 'hp'
        def show(self):
            print(self.brand)

m1 = Student(34,5,6)
print(m1.avg())
print(m1.info1())
lap1 = m1.lap
print(m1.lap.brand)
m1.show()
#inheritance

class A:
    def __init__(self):
        print('inside the inita')
    def feature1(self):
        print("feature1")

    def feature1(self):
         print("feature1")

a1 = A()
a1.feature1()

class B(A):
    def __init__(self):
        print('inside the initb')
        super().__init__()
    def feature3(self):
        print('feature3')

b1 = B()
b1.feature3()
b1.feature1()

class Student3:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):

        s = a+b+c
        return s
s3 = Student3(50,64)

print(s3.sum(50,67,65))
#abstract classes

from abc import ABC,abstractmethod
class Computer5(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer5):
    def process(self):
        print('hello')

#com1 = Computer5()
com1 = Laptop()
com1.process()

#iterators

nums4 = [1,2,3]
it = iter(nums4)

print(it.__next__())
print(next(it))

for i in nums4:
    print(i)