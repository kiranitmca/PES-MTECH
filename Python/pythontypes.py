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

md1 = {'Bank':'SBI','Branch':'MGR','country':'India'}

# print(type(md1))
# print(md1['Bank'])
# md1['Bank']='HDFC'
# print(md1)
# print(md1.get('Branch'))
k=md1.keys()
print(k)

klist= list(md1.keys())
print(klist)

ilist= list(md1.items())
print(ilist)