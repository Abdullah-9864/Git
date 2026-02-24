x=12
print(id(x))
x=14
print(id(x))

# In immutable types, when you “change” the value, Python creates a new object — so the memory address usually changes.
import math
math.pi
x=2*math.pi
print(x)


string = "hello"
print(len(string))
print(string[-1])


mylist=[1, 2, 3]
print(len(mylist))

myD={"comic":"spiderman", "computer":"macbook"}
print(len(myD))
print(myD["comic"])


myTUP=(1, 2, 3)
print(myTUP[0])
