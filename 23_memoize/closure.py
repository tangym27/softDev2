import random

# # scenario: randomizing greeings in an html doc
# goal : separate geneartions of text from html-ificaation
#
# time-saving solutions via closures

# def Agreet():
#     greetings = ['hi', 'welcome', 'hola', 'we meet again']
#     return random.choice(greetings)
#
# def AmakeHTML(f):
#     print f
#     txt = f()
#     print txt
#     def inner():
#         return '<h1>' + txt + '</h1>'
#     return inner
#
# #Agreet_heading = AmakeHTML(greet)
# print(Agreet_heading())

##########


# def makeHTML(f):
#     def inner():
#         return '<h1>' + f() + '</h1>'
#     return inner
#
# # eqiv to greet_heading = makeHTML(greet)
# @makeHTML
# def greet():
#     greetings = ['hi', 'welcome', 'hola', 'we meet again']
#     return random.choice(greetings)
#
# print( greet())
# #
# # # memoization: process of storing previously calcultated results (ie writing memos) so as to aavoid recalcuations
#
# def memoize(f):
#     memo = {}
#     def inner(num):
#         memo[num] = '<h1>' + f() + '</h1>'
#         return memo
#     return inner
#
# # eqiv to greet_heading = makeHTML(greet)
# @memoize
# def greet(num):
#     greetings = ['hi', 'welcome', 'hola', 'we meet again']
#     return random.choice(greetings)
#
# print( greet(num))

# memoization: process of storing previously calcultated results (ie writing memos) so as to aavoid recalcuations

#
#

#
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = memoize(fib)
print(fib(40))

# # mS: resumes
#
# -action words
# - less is more
# - only list tech language inf you known it
# - do not leave out tech/lang you known
# - appropriate email
# proofread
# goal of a resume?: get you an interview
# need not fill page
# name and contact info clear at top
#
# def memoize(fxn):
#     cache = {}
#     def memoized_fxn(*args):
#         if args in cache:
#             return cache[args]
#         result = fxn(*args)
#         cache[args] = results
#         return results
#     return memoized_fxn
