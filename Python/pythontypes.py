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


l = range(10)
for i in set(l):
    if i%2==0:
        print(f"Even Number: {i} ")