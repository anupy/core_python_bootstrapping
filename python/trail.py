import one
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print(__name__)

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

dictVar = {1:"one",2:"two"}
print(dictVar)
dictVar.update({3:"three"})
print(dictVar)
del dictVar[1]
print(dictVar)

sets = {"one","two","three","three"} # It takes unique elements only.
print(sets)
sets.remove('two')
print(sets)
sets.discard('one')
print(sets)
sets.pop()
print(sets)
sets.add('three')
print(sets)
sets.add('two')
print(sets)
sets.add('one')
print(sets)
sets.clear()
print(sets)

listVar = [2,3,4,5,6,6]
print("List All elements.....")
print(listVar)
print("List unique set.....")
print(set(listVar))

print("List Comprehensions.....")
anslist = [i for i in listVar if i%2 == 0]
print(anslist)

from decorators import *

@uppercase
def greet():
    return 'Hello!'

print(greet())

@outerfunc
@check_role_permissions
def checkDecorator():
    print("Called decorator........")

checkDecorator()

class MyClass:

    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super(MyClass, cls).__new__(cls)

    def __init__(self):
        print("__init__")
        self.x = 0

    def my_method(self):
        print("called using self.....")
        return 'hello'

    def method(self):
        self.my_method()
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

immutablestring = "My name"
print(id(immutablestring))
# immutablestring[0] = "j"
print(immutablestring)

string = "hello"
str_temp = ""
i = 0
j = 0
while j < len(string):
    i = i -1
    str_temp +=  string[i]
    j += 1
print(str_temp)


# Generators
def rgenrange(listobj):
    for listo in listobj:
        yield listo
        listo = listo + 1
        yield listo
listobj = [1,2,3,4,5,6]
print("=========== Generator with multiple yield. ===============")
print([i for i in rgenrange(listobj)])

# The built-in function enumerate takes an iteratable and returns an iterator
# over pairs (index, value) for each value in the source.
lista = [5,6,9,0]
for i, v in enumerate(lista):
    print(i,v)

lista = [(2,3,[5,6],{3:5,0:4}),4,5,{3:5,0:4}]
print(lista)

tupled = ([2,3],{3:4});
print("tupled",tupled)

try:
    dict_try = {(2,3):3,[4,4]:5}
    print(dict_try)
except:
    print("TypeError: unhashable type: 'list'")

a = {i for i in range(0, 10, 2)}
print(a)


to_sort_list = [1,2,4,3,5,7,6,8]
print(".sort returns None")
print("sorted return values")
print(sorted(to_sort_list))
to_sort_list.sort()
print(to_sort_list)

print("===== Closure Function ======")

def outerfunc(x):
    print("We are outer")
    def innerfunc(y):
        print("We are inner")
        return x + y
    return innerfunc(4)

output = outerfunc(5)
print(output)

#json.dump(dict_object, file_object)
#json.dumps(string_object)

#json.load(file_object)
#json.loads(string_like_json_object)





