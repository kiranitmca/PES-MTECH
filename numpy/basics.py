import numpy as np

# Creation of arrays

#mylist = [1,2,3,4,6,8]
# mylist = [[1,2,3,4,6,8],
#           [2,4,6,8,10,12],
#           [3,6,9,12,15,18]]

# x= np.array(mylist)
# print(x)
# print(type(x))
# print(x.shape)
# print(x.dtype)
# print(x.itemsize)

# np.random.seed(23)
# n64 = np.random.randint(10,101,size=(6,4))
# print(n64)


# n = np.arange(20).reshape(5,4)
# print(n)

# print(n.ravel())
# print(n.flatten())

# m = np.arange(34650).reshape(5,-1).shape
# print(m)

# print(np.ones(shape=(3,4), dtype=np.int16))

# print(np.full((3,4), fill_value=5, dtype=np.float32))

# print(np.identity(4))


# Array Access

np.random.seed(23)
n64 = np.random.randint(10,101,size=(8,9))
# print(n64[0,0])
# print(n64[-1,-1])

# Grammar

'''
n64[row_index]
n64[row_index, column_index]
n64[start_row_index:stop_row_index, start_column_index:stop_column_index]
n64[:, column_index]  # All rows of a particular column
n64[row_index, :]  # All columns of a particular row]
n64[-row_index]  # Accessing from the end

n64[[row_list], [column_list]]  # Vector access 
'''
# print(n64[2:5])
# print(n64[2:5 ,2:7])
# print(n64[[0,2,-2,-1]]) # Vector access

# print(n64[[0,2,-2,-1],[1,2,3,4]])

# print(n64[: , 3:5])

# print(n64[1:3,3:5])

# Conditional Access

# mask1= n64 > 50
# print([mask1])

# Extract all even values greater than 50

# mask2 = (n64 > 50) & (n64 % 2 ==0)
# print(n64[mask2])

# n64[n64 > 50] = 100

# print(n64)

# Aggregation

np.random.seed(23)
n34 = np.random.randint(1,31,size=(3,4))

# print(n34)
# print(np.sum(n34)) # Sum of all elements in the array
# print(np.sum(n34, axis=0)) # Sum of each column
# print(np.sum(n34, axis=1)) # Sum of each row
# print(n34.sum(axis=0))
# print(np.mean(n34))
# print(np.max(n34))
# print(np.min(n34))

# print(np.median(n34))
# print(np.median(n34, axis=0))
# print(np.median(n34, axis=1))

# Array Split

np.random.seed(23)
n89 = np.random.randint(10,101,size=(8,9))
#print(n89)
r=np.vsplit(n89, 4) # Vertical split into 4 equal parts
c=np.hsplit(n89, 3) # Horizontal split into 3 equal parts
#print(c[0])
#print(c)
#d= np.dsplit(n89, 6) # Depth split into 6 equal parts
#print(d)

# alist = np.hsplit(n89, [2,5,6]) # Horizontal split at specified indices
# #print(alist)   
# for a in alist:
#     print(a)
# alist

# Stacking arrays

n34 = np.arange(12).reshape(3,4)
n36 = np.arange(100,118).reshape(3,6)
n64 = np.arange(200,224).reshape(6,4)

# print(n34)
# print(n36)
# print(np.hstack(tup=(n34,n36))) # Stack arrays horizontally (column-wise)

# print(np.concatenate((n34,n64), axis=0)) # Concatenate arrays along a specified axis (axis=1 for horizontal)

# for n in np.nditer(n34,order='F'):
#     print(n)

# for index,value in np.ndenumerate(n34):
#     print(index, value)

# for index, value in enumerate('hello'):
#     print(index, value)

# Linear Spaced  Values Linspace


# n=np.linspace(3,5,num=9)
# print(n)

# m = np.linspace(2.5,5.5,num=7,retstep=True)
# print(m)

#print(np.random.rand(3,4))   Uniform distribution over [0,1)

nr=np.random.randn(30,40) # standrard normal distribution (mean=0, std=1)
# print(nr.min())
# print(nr.max())
# print(nr.mean())

import matplotlib.pyplot as plt

plt.hist(nr.flatten(), bins=50)
plt.show()
