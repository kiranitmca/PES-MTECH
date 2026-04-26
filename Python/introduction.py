# print('NSE')
# print('BSE # Mumbai')

# var1 = 'nse and bse is in ' \
# 'mumbai'\
# ' and ' \
# 'delhi'
# print(var1)

# import keyword
# print(keyword.kwlist)
# print(dir(keyword))

# sensor=0

# if sensor == 1:
#     print('Sensor is off')
#     print('Please turn on the sensor')
# else:
#     print('Sensor is on')
#     print('Sensor is working fine')

# v1= 10
# print(type(v1))  # shows the type of variable v1
# v2 = 10.5
# v2= 'hey'
# print(type(v2))  # shows the type of variable v2
# print(type(v2))  # shows the type of variable v2 
# #python dynamically types lang and in python, there is no contract between  variable and  object value.

# v3 = 2500
# print(id(v3))  # shows memory address of the varaible 
# v4= 2500
# print(id(v4))   # value  -5 to 256 are created during the boot time and stored in the memory and they are shared among all the variables. so, v3 and v4 are pointing to the same memory address. but for value 258, it is not created during the boot time and it is created at runtime, so v3 and v4 are pointing to different memory address.

# delete variable 

#del v4
#print(v4)
# Keyboard inputcls

# sub = input('Enter the subject name: ')
# print('The subject name is: ' + sub)

#print(20,30,40,50,'hello',sep=':')  # sep is used to separate the values with a specific character or string. by default, it is a space.
#print(7**2)

# def mf1(p0,p1):
#         r= p0+p1
#         return r
# x=mf1(10,20)
# print(x)

# Strings are immutable in python and it behaves as constants.
#ms1='abcdefghijkl'
# print(ms1[0])
# print(ms1[5])
# print(ms1[-1])
# print(ms1[7:10])
# print(ms1[-8:-2])
# print(ms1[:7])

# concatination and membership operators

#ms2='mnopqrstuvwxyz'
# print(ms1+ms2)
# print('a' in ms1)
# print('z' not in ms2)
#print(dir(str))
#help(str.replace)

ms1='king RING sing'

# print(ms1)
# print(ms1.replace('ng','ms'))
# print(ms1.replace('g','*').replace('G','#'))
# Find methods that starts with 'is' and 'endswith' in string class

# ind= ms1.find('g')
# print(ind)

# ind1= ms1.rfind('g')
# print(ind1)


# print(ms1.lower())
# print(ms1.count('g'))
# print(ms1.upper())
# print(ms1.capitalize())
# print(ms1.swapcase())

# print('2023S'.isdigit())

#print(ms1.split())

# ms2= 'world health org_geneva'
# print(ms2.split('_'))
# ms3 =['National','Stock','Exchange','Mumbai','City']

# print(' '.join(ms3))

sub ='Maths'
num = 58
avg = 87.65

ns1='The subject is {} and the number is {} and the average is {}'.format(sub,num,avg)
print(ns1)


