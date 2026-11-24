"""
#variables
a=10
print(id(a))
1=10
print(1)
a1=100
print(a1)
_=10
print(_)
a b=10
print(a b)
#multiplke variables
a,b,c=102,0,30
print(a,b,c)
a,b,c=10,20
print(a,b)
a,a,b=1,20,10
print(a)
#keywords
import keyword
print(keyword.kwlist)
a=None
print(a)
a=10
bool(a)
a=0
bool(a)
print(type(a))
#print(len(a))
a=3+5J
print(a)
a=5J+3
print(a)
a=5+j
print(a)
a=6j
print(a)

#strings
a="happy father's day"
print(a)
print(a[0])
print(a[1])
print(a[2])

#lists
a=[1,2,3,4,5,True,False,'hi',5+3j,(1,2),'hello']
print(a)
a.append(10)
a.pop()
a.pop(2)
a.remove(True)
#sets
a={}
'''List'''
my_list = [1, 2, 3, 4, 'hello', 5.6, True]
# to Extract hello from the list
print(my_list[4])
# Now H from hello 
print(my_list[4][0])

#Appened Function
my_list.append(10)
print(my_list)

#Pop Function
print(my_list.pop())
print(my_list)
#finding data type of list
print(type(my_list))

#TUPLE
my_tuple = (1, 2, 3, 4,5J,'hello', 5.6, True,)
#set operations     
set1 = {1, 2, 3, 4, 'hello', 5.6, True}
print(type(set1))

my_dict = {'a':[10,20,30], 'b':[40]}
print(my_dict['a'][-2])
#list of keys
print(my_dict.keys())

'''slicing '''
a = "hello world"
print(a[0:5])
print(a[6:11])


#dictories
a={'a':10,'b':30,c':40}
print(a.values())
print(a.keys())
a={'a':[10,20,30],'c':40}

#slicing
a='hello'
print(a[2:4])
print(a[2:3])
a="good morning"
print(a[7:11])
#a="hello"
print(a[3:1-1:-1])
print(a[-2:-4-1:-1])
print(a[3:0:-1])
print(a[::-1])
#'odm'
print(a[1:5+1:2])
#'mng'
print(a[-7::3])

a="good morning"
#negative way slicing
print(a[-2:-8-1:-3])
#positive way slicing
print(a[10:4-1:-3])

a=input("enter :")
print(type(a))
a=float(input("enter :"))
print(type(a))
#conditional statements
a=eval(input("enter :"))
print(type(a))
if a%2==0:
    print("even")
else:
    print("odd")
    
l=eval(input("enter the list:"))
if len==5:
    print("length is 5")
else:
    print("no")

    #ascii valuesK
print(ord('a'))
print(chr(97))
print(chr(ord('A')+32))

ch=input("enter a character:")
if"A"<=ch<="z":
    print("uppper case")
elif "a"<=ch<="z":
    print("lower case")
else:
    print("not a alphabet")

un= input("Enter a character: ")
if un=='hero':
    print("correct username")
    pw= input("Enter a password: ")
    if pw=='hero123':
        print("correct password")
    else:
        print("incorrect password")
else:
    print("incorrect username")

username = 'herooo'
password = 'hero123'
un= input("Enter a username: ")
if un==username:
    print("correct username")
    pw= input("Enter a password: ")
    if pw==password:
        print("login")
    else:
        print("incorrect pw") 
else:
    print("incorrect un")

i=1
while i<=100:
    print(i)
    i+=1    

i=1
while i<=50:
    if i%2==0:
     print(i)
    i+=1
else:
    print("odd")
    
n=int(input("enter a number:"))
rev=0
while n>0:
    id=n%10
    n=n//10
    rev=(rev*10)+id
print("reverse number is:",rev)

for i in range(1,100):
    if i%2==0:
     print(i)

l=[1,2,3,4,5,6,7,8,9]
for i in l:
    print(i)

s=int(input("enter a number:"))
out=''
for i in s:
    if "A"<=1<="Z":
        out+=chr(ord(i)+32)
    elif "a"<=1<="z":
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)

s=input("enter a string:")
rev=''
for i in s:
    rev=i+rev
print(rev)
for i in range(1,6):
    print("*")

for i in range(1,6):
        print("*",end="")
print()
"""

for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,6):
    for j in range(1,6):
        if i<j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,6):
    for j in range(1,6):
        if i>j:
            print("*",end="")
        else:
            print(" ",end="")
    print()