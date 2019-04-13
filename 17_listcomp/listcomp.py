# Tangerines- Alexander Liu, Michelle Tang, Tim Marder
# Softdev2 pd6
# K16 -- Do You Even List?
# 2019-04-12

# 1a
def loopyOne():
    var = 0
    num = []
    while (len(num) < 5):
        num.append( str(var) + str(var) )
        var += 2
    return num

print( " 1A: ")
print(loopyOne())

# 1b
def listcompOne():
    nums = "02468"
    array = [x + x for x in nums]
    return array

print( " 1B: ")
print(listcompOne())

print ("\n==============\n")
# 2a
def loopyTwo():
    var = 0
    num = [7]
    while (len(num) < 5):
        num.append( 10 + num[len(num) - 1] )
        var += 1
    return num

print( " 2A: ")
print(loopyTwo())

# 2b
def listcompTwo():
    nums = "01234"
    array = [ int(x + "7") for x in nums]
    return array

print( " 2B: ")
print(listcompTwo())

print ("\n==============\n")
# 3a
def loopyThree():
    var = 0
    i = 0
    num = [0]
    while (len(num) < 9):
        while (i < 2):
            num.append( num[len(num) - 1] + var )
            i += 1
        num.append(0)
        i = 0
        var += 1
    num.pop()
    return num

print( " 3A: ")
print(loopyThree())

# 3b
def listcompThree():
    nums = "012"
    array0 = [ 0*int(x) for x in nums]
    array1 = [ 1*int(x) for x in nums]
    array2 = [ 2*int(x) for x in nums]
    array1.extend(array2)
    array0.extend(array1)
    return array0

print( " 3B: ")
print(listcompThree())

# Helper function for prime and composite!
def sieve():
    n = 100
    prime = []
    for i in range(n+1):
        prime.append(1)

    p = 2
    while (p <= n):
        if (prime[p]):
            for i in range(p * 2, n+1, p):
                prime[i] = 0
        p += 1
    return prime

print ("\n==============\n")
# 4a
def loopyFour():
    prime = sieve()
    primes =[]
    for p in range(2, 100):
        if prime[p]:
            primes.append(p)
    return primes

print( " 4A: ")
print (loopyFour())

# 4b
def listcompFive():
    pass


# print(listcompFive())
print ("\n==============\n")
# 5a
def loopyFive():
    composite = sieve()
    composites =[]
    for p in range(0, 101):
        if composite[p] == 0 :
            composites.append(p)
    return composites

print( " 5A: ")
print (loopyFive())

# 5b
def listcompFive():
    pass
