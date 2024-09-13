#FILE HANDLING
q=open("example.txt","r")
a=q.read()
print(a)


# EXCEPTION HANDLING
try:
    f=open("example1.txt","r")
    a=f.read()
    print(a)
except:
    print("pahle file banao ")
    
else:
    f.close()
    print("file closed")
    
#NUMPY
import numpy as np
#single dimensional array

import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
print(a)

#2D ARRAY

import numpy as np
a=np.array([[1,2,3,4],[1,2,3,4]])
print(a)

#SLICING  BY INDEXING 

import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
a1=a[4]
print(a1)
print(a[0])

#MATRIX

m = np.zeros((4, 6))
print(m)
n=np.ones((3,3,3))
print(n)
b=np.identity((4))
print(b)

#GENERATE THE RANDOM NUMBERS BY THE RANDOM FUNCTION 
import random
x=random.randint(1,100)
print(x)   

#DICTIONARY
dict={'name':"rajveer","class":"cyber security","rollno":"23100030049"}
print(dict)
print(dict['name'])

#UPPER AND LOWER 
upperstr="hello world"
print(upperstr.upper())

lowstr="HELLO WORLD"
print(lowstr.lower())

#LIST MODIFICATION SLICING, INDEXING
list=(1,2,3,4,5,6,7)
print(list[3])  #INDEXING
print(list[1:6])  #SLICING

#SET
set={1,2,3,4,5,6}
print(set)
print(frozenset(set))