'''dictVar = {
    "name": "root",
    "children": [
        {
            "name": "a",
            "children": [
                {
                    "name": "b",
                    "children": [
                        {
                            "name": "c",
                            "size": "1"
                        },
                        {
                            "name": "d",
                            "size": "2"
                        }
                    ]
                },
                {
                    "name": "e",
                    "size": 3
                }
            ]
        },
        {
            "name": "f",
            "children": [
                {
                    "name": "g",
                    "children": [
                        {
                            "name": "h",
                            "size": "1"
                        },
                        {
                            "name": "i",
                            "size": "2"
                        }
                    ]
                },
                {
                    "name": "j",
                    "size": 5
                }
            ]
        }
    ]
}

name = {}
for dobj in dictVar['children']:
    for c in dobj['children']:
        if not dobj['name'] in name:
            name[dobj['name']] = [c]
        else:
            name[dobj['name']].append(c)
print(name)


collection = [{
    "name": "foo",
    "place": "Paris",
    "other": {
        "var1": "asdf",
        "var2": "asdf",
        "var3": "sdfw"
        }
    },
    {
    "name": "Bar",
    "place": "Paris",
    "other": {
        "var1": "asdf",
        "var2": "asdf"
    }
    }]

for obj in collection:
    obj.update(obj.pop("other"))

print(collection)
'''
'''
from multiprocessing import Process


def square(x):
    for x in numbers:
        print('%s squared  is  %s' % (x, x ** 2))


def is_even(x):
    for x in numbers:
        if x % 2 == 0:
            print('%s is an even number ' % (x))


if __name__ == '__main__':
    numbers = [43, 50, 5, 98, 34, 35]

    p1 = Process(target=square, args=('x',))
    p2 = Process(target=is_even, args=('x',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")


a = [['abc','Hello World'],['bcd','Hello Python']]
b = [['abc','Hello World'],['bcd','Hello World'],['abc','Python World']]

'''

# Here is source code of the Python Program that reads a file and
# capitalizes the first letter of every word in the file. The program output is also shown below.
fname = input("Enter file name: ")
with open(fname, 'r') as f:
    for line in f:
        l = line.title()
        print(l)

#https://www.geeksforgeeks.org/str-vs-repr-in-python/

#str() vs repr() in Python
#Example of str():
'''s = 'Hello, Geeks.'
print str(s)
print str(2.0/11.0)

#Example of repr():
s = 'Hello, Geeks.'
print repr(s)
print repr(2.0/11.0)
'''


