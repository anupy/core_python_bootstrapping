import sys

print("File name is :",sys.argv[0]) # This is default is sys.argv[0]
first_name = sys.argv[1] if 1 in sys.argv else "Anup"
last_name = sys.argv[2] if 2 in sys.argv else "Yadav"
print("Hello " + first_name + " " + last_name)



def function_get_id():
    return True

print(id(function_get_id))

class GetId():
    pass

print(id(GetId))

