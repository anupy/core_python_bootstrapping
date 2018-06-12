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
