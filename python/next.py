

def gen_a(table):
    for x in table: # same as for x in table.keys()
        print("x",x)
        if x > 4000:
            yield x

def gen_b(table):
    for x in table:  # same as for x in table.keys()
        if x > x: # will never happen
            yield x

table ={1249.99: 36.30,
        1749.99: 54.50,
        2249.99: 72.70,
        2749.99: 90.80,
        3249.99: 109.00,
        3749.99: 127.20,
        4249.99: 145.30}


val = next(x for x in table if x > 4000)

print(val)

print("=========================================")

x = 1500 # note that x isn't in the same scope as the other x's

print(next(gen_a(table))) # result varies since dict are unordered, I got 4249.99

print(next(gen_b(table))) # raises a StopIteration