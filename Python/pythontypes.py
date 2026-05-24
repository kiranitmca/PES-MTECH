# mlist=['hello',123,(20,'world'),[1,'Jan',(2,3)]]
# print(mlist[-1][2][1])

# m2= [22,33,"Hello"]
# print(m2)
# m2[-1]=m2[-1].replace('H','J')
# print(m2)

# word = list("Helloworld")
# print(word)

# print('r' in word)


# Matrix representation using list of lists
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0][1])  
# element=matrix[1][2]
# print(element)
# print(matrix[-1][-1])

# list functions 

# In python , a function/method  can modify the incoming mutable object -- This is called INPLACE update.
# mylist=[1,2,3]
# mylist.extend([4,5])
# print(mylist)
# mylist.insert(3,"Hello")
# print(mylist)
# mylist1=mylist.pop(3)
# print(mylist)
# print(mylist1)
# mylist.remove(5)
# print(mylist)
# mylist.reverse()
# print(mylist)

import copy


mylist2= list("helloworld")
# i = mylist2.index('o')
# print(i)
# c= mylist2.count('o')
# print(c)

# print(max(mylist2))
# print(min(mylist2))
# mylist2.sort()
# print(mylist2)

# while 'o' in mylist2:
#     mylist2.remove('o')
# print(mylist2)
# print(mylist2.reverse())

# print(isinstance(20,(int,float)))

def objcheck(obj):
    if isinstance(obj,(int,float)):
        return obj
    elif isinstance(obj,str):
        return len(obj)
    elif isinstance(obj,list):
        return 0
    else:
        return "Unknown type"
    
# print(objcheck(20))
# print(objcheck(3.14))
# print(objcheck("Hello"))
# print(objcheck([1, 2, 3]))

# m1 = [33,4,'jello',22,11,44,77,55,'Hello',[999,888,777]]
# print(m1)
# m1.sort(key=objcheck,reverse=False)
# print(m1)
# print(id(m1))

# m1= [22,11,77,44,55,45,77]
# print(m1)
# print(id(m1))
# m2=m1.copy()  # shallow copy 
# print(m2)
# print(id(m2))

# DIY copy module looks at function copy.copy,copy.deepcopy

# m1= [22,11,77,44,55,45,77]
# print(m1)
# m2=copy.deepcopy(m1)  # deep copy
# print(m2)
# m2[0]=999
# print(m1)
# print(m2)

# Tuple is immutable sequence type in python

# mt1 = (10+11,)
# print(type(mt1))

# May-9
# Dictionary is a collection of key-value pairs in python

md1 = {'Bank':'SBI','Branch':'Whitefield','country':'India'}

# print(type(md1))
# print(md1['Bank'])
# md1['Bank']='HDFC'
# print(md1)
# print(md1.get('Branch'))
# k=md1.keys()
# print(k)

# klist= list(md1.keys())
# print(klist)

# ilist= list(md1.items())
# print(ilist)

# Get Method to access value of a key in dictionary
# print(md1.get('Bank','Unknown Key'))

# r= md1.pop('State','Unknown Key')
# print(r)

# md1.setdefault('State','Maharashtra')
# print(md1)

# keys= ['Bank','Branch','country','City']
# for k in keys:
#     print(f"{k} :  {md1.get(k,'Unknown Key')}")


md2 ={'Bank':'HDFC','Branch':'MGR','country':'India'}

md1.update(md2)
#print(md1)

klist= ['Bank','Branch','country','City']
vlist= ['SBI','Whitefield','India','Bangalore']
# z=zip(klist,vlist) #  zip o/p is an iterator .one time consumable container
# #print(list(z))

# md3=dict(z)

# print(md3)

# for k,v in zip(klist,vlist):
#     print(f"{k} : {v}")


# slist=['S1','S2','S3']
# m1list=[70,65,74]
# m2list=[80,75,85]

# mlist=dict(zip(slist,zip(m1list,m2list)))
# print(mlist)


# Sets are unordered collection of unique elements in python.

# s1={10,20,30,40,50,20,30,60,70,80}
# print(sorted(set(s1)))

# # m5=set('Helloworld')
# # print(m5)

#ms1={10,20,30,40,50,80}
#ms2={30,40,50,60,70,10,20}
# ms3=ms1.union(ms2)
# ms4=ms1.intersection(ms2)
#ms5=ms1.difference(ms2)
# ms6=ms1.symmetric_difference(ms2)
# print(ms3)
# print(ms2)
# print(ms3)
# print(ms4)
#print(ms5)
# print(ms6)

# Decision Making

# temp = int(input("Enter the temperature in Celsius: "))
# if temp < 60:
#     print("It's a Cold day.")
# elif temp >=60 and temp <=99 :
#     print("It's a pleasant day.")
# elif temp > 99:
#     print("It's a Hot day.")

# temp1=98
# r = 'Hot' if temp1 > 90 else"cold" if temp1 < 60 else 'Normal'
# print(r)
# import sys
# r = range(10,20)
# vlist= list(r)
# #print(vlist)
# print(sys.getsizeof(r))
# print(sys.getsizeof(vlist))

# Loops / Iterators

# lcount1=10
# lcount2=20
# while lcount1 < lcount2:
#     print(lcount1, end = ' ')
#     lcount1+=2
# print("Bye")


# l = range(10)
# for i in set(l):
#     if i%2==0:
#         print(f"Even Number: {i} ")

# a =(10,20,30,40,50)
# print(a)


# lcount1=9
# while (lcount1>0):
    
#     if lcount1==6:
#         lcount1-=1
#         continue
#     print(lcount1)
#     lcount1-=1
# print("Bye")

# Write a function to take an number and check if it is even or not 

# def evencheck(num):
#     if (num%2) == 0:
#         return 'Even'
#     else:
#         return 'Odd'

# num=20
# print(evencheck(num))

# a = 10,202,30,40
# print(a)

# May -10 
# Rule-1 While defining the function 
# the required param must be specified before default param
#Rule-2  while calling a function ,positional mapping by python 
# should be done and then programmers parameter-based mapping

# Rule-3  A variable tuple can be populated by positional mapping 
# Rule-4  Avariable dict in the function definition,
# should be specified last


# def mf15(r1,r2,*args,d1=111,d2=3333,**kwargs):
#     print(r1,r2)
#     print(d1,d2)
#     print(args)
#     print(kwargs)

# mf15(10,20,30,40,50,'Hello',v=20,v2=30)


# lambda function

# def isEven1(num):
#     return (num%2)==0

# print(isEven1(2))

# iseven2=lambda n1 : (n1%2)==0
# print(iseven2(22))

# isnum = lambda n2 : 'even' if (n2%2) == 0 else 'Odd'

# print(isnum(30))

# isnum1 = lambda n3 : n3**2 if (n3%2) == 0 else n3**3

# print(isnum1(20))

# istemp = int(input("Enter temp:"))

# temp = lambda istemp : 'Hot' if istemp > 99 else 'cold' if istemp < 60 else 'Normal'
# print(temp(istemp))

# DIY : list.sort with key method code it using anomynous function objects


# mlist = [1,2,3,4,5]
# cmobj = map(lambda m: m*100 ,mlist) # inline, created,consumed,destroyed
# print(list(cmobj))

# nlist=[10,20,13,16,19,22,28]

# fobj=filter(lambda n1: (n1%2) == 0 ,nlist)
# print(list(fobj))

# fobj1=filter(lambda char : char.lower() in 'aeiou' ,'pythonpdsDSAIml')
# print(list(fobj1))

# import functools
# nlist=[10,20,13,16,19,22,28]

# robj=functools.reduce(lambda n1,n2 : n1 if n1 > n2 else n2 ,nlist)
# print(robj)

# Grammer 
#1  
'''
final_list = [<2. expression > <1. for loop >]

'''


# l = [2,4,5,6,7,9]
# lobj = [ x**2 for x in l]
# print(lobj)

# olist=[]

# for i in l:
#     olist.append(i**2)
# print(olist)


l1 = [2,4,5,6,7,9]
num2=[]

# for n in l1:
#     if n%2 == 0:
#         num2.append(n**2)
#     else:
#         num2.append(n**3)
# print(num2)


# olist = [n**2 if (n%2) == 0 else n**3 for n in l1 ]
# print(olist)

# ilist =[1,2,4,5,7,9,10,12]
# olist1=[]
# for n in ilist:
#     if n%2 == 0:
#         olist1.append(n**2)
# print(olist1)

#2 

'''
final_list = [<3.expression> <1. for loop> <2.gating_condition>]

'''

# Grammer
# final_list =[<3. expression> <1. for_loop> <2. for_loop_1>]



# olist2=[]

# for n in range(1,30):
#     if n%3 == 0:
#         if n%2 ==0:
#             olist2.append([n,n**2])
#         else:
#             olist2.append([n,n**3])
# print(olist2)

# olist3=[[n,n**2] if n%2==0 else [n,n**3]for n in range(1,30) if n%3==0]
# print(olist3)

# sqdict = {n:n**2 for n in range(1,10)}
# print(sqdict)


# mlist =[]
# for n in [2,3,4,5]:
#     olist = []
#     for m in [1,2,3,4,5]:
#         olist.append(n*m)
#     mlist.append(olist)


# print(mlist)


# olist=[[n*m for m in [1,2,3,4,5]] for n in [2,3,4,5]]
# print(olist)


# Recursion

def fact(n):
    if not isinstance(n,int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(-5))