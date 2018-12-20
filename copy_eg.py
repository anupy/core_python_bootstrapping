import copy

print( "\n\n ================ Deep Copy =================== \n\n" )

li1 = [1, 2, [3,5], 4]
li2 = copy.deepcopy(li1)
print ("The original elements before deep copying")
print (li1) 
print("\r")
li2[2][0] = 7
print ("The new list of elements after deep copying ")
print (li2) 
print("\r")
print ("The original elements after deep copying")
print (li1) 
print("\r")

print( "\n\n ================ Shallow Copy =================== \n\n" )

li2 = copy.copy(li1)
print ("The original elements before shallow copying")
print (li1) 
print("\r")
li2[2][0] = 9
li2.append(500)
print ("The original elements after shallow copying")
print (li1) 
print("\r")
li2.remove(4)
print (li1) 
print("\r")

print( "\n\n ================ 2nd Shallow Copy =================== \n\n" )

node = [[0,3], 1]
node2 = node
node3 = copy.copy(node)
node3[0][0] = 200
node3[1] = 400

print(node) 
print("\r")
print(node2) 
print("\r")
print(node3) 
print("\r")


# https://realpython.com/copying-python-objects/
'''3 Things to Remember

    Making a shallow copy of an object won’t clone child objects. Therefore, the copy is not fully independent of the original.
    A deep copy of an object will recursively clone child objects. The clone is fully independent of the original, but creating a deep copy is slower.
    You can copy arbitrary objects (including custom classes) with the copy module.'''


'''
a) A recursive function is a function which calls itself.

b) The speed of a recursive program is slower because of stack overheads. (This attribute is evident if you run above C program.)
c) A recursive function must have recursive conditions, terminating conditions, and recursive expressions.

Stack data structure . Because of its LIFO (Last In First Out) property it remembers its caller so knows whom to return when the 
function has to return. Recursion makes use of system stack for storing the return addresses of the function calls. 
Every recursive function has its equivalent iterative (non-recursive) function. Even when such equivalent iterative procedures 
are written, explicit stack is to be used.
'''

