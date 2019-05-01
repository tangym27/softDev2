# To t
def inc(x):
    return x+1

f = inc
# # 11
# print(f(10))
# # <function inc at 0x1046e1b90>
# print(f)


def adder(a,b):
    return a+b

def caller(c):
    print(c(2,4))
    print(c(3,5))

# caller(adder)
#return 6 || 8
#
# def outer(x):
#     def contains(l):
#         return x in l
#     return contains
#
# contains_15 = outer(15)

# print contains_15([1,2,3,4,5])
#
# print contains_15([13,14,15,16,17])
#
# print contains_15(range(1,20))

# N: A closure remembers the context in which i was created even if you obliterate the creater fxn:
# del outer
# outer(42)

# print contains_15(range(14,20))
#
# To create a closure:
# - define nested fxn
# - nested fxn must refer to var defined in enclosing fxn (i mean not reallyyy)
# - return nested fxn
#


#
# def repeat(word):
#     def repeat(num):
#         return num*word
#     return repeat
#
# r1 = repeat("hello")
# print r1(2)
# r2= repeat("goodbye")
# print r2(2)
# print repeat('cool')(3)

#
# def outer():
#     x = "foo"
#     def inner():
#         x = "bar"
#     inner()
#     return x
#
# # print(outer()) returns foo
#
#
# def outer():
#     x = "foo"
#     def inner():
#         nonlocal x
#         x = "bar"
#     inner()
#     return x

# print(outer()) return bar

def make_counter():
    x = 0
    def inc():
        nonlocal x
        x += 1
        return x
    return inc


a = make_counter()
print (a())
print (a())
print (a())
print (a())

b = make_counter()
print (b())
print (b())
print (b())
