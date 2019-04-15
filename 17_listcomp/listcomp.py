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

# 1b
def listcompOne():
    nums = "02468"
    array = [x + x for x in nums]
    return array

# 2a
def loopyTwo():
    var = 0
    num = [7]
    while (len(num) < 5):
        num.append( 10 + num[len(num) - 1] )
        var += 1
    return num

# 2b
def listcompTwo():
    return [x*10+7 for x in range(5)]

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

#3b
def listcompThree():
    return [ x*y for x in range(3) for y in range(3) ]

# 4&5 : Helper function for prime and composite!
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

# 4a
def loopyFour():
    composite = sieve()
    composites =[]
    for p in range(0, 101):
        if composite[p] == 0 :
            composites.append(p)
    return composites

# 4b
def listcompFour():
    return [i for i in range(2, 101) if 1 in [1 if i%j == 0 else 0 for j in range(2, i)]]

# 5a
def loopyFive():
    prime = sieve()
    primes =[]
    for p in range(2, 100):
        if prime[p]:
            primes.append(p)
    return primes

#5b
def listcompFive():
    return [i for i in range(2, 101) if 1 not in [1 if i%j == 0 else 0 for j in range(2, i)]]

#6a
def loopySix(n):
    i = 1
    list = []
    while (i < n):
        if not n%i:
            list.append(i)
        i +=1
    list.append(n)
    return list

#6b
def listcompSix(n):
    list = [i for i in range(n) if i > 0 and n%i == 0]
    list.append(n)
    return list


print( " 1: ? -> ['00', '22', '44', '66', '88'] ")
print(" 1A: " + str(loopyOne()))
print(" 1B: " + str(listcompOne()))
print ("\n==========================================\n")
print( " 2: ? -> [7, 17, 27, 37, 47] ")
print( " 2A: " + str(loopyTwo()))
print( " 2B: " + str(listcompTwo()))
print ("\n==========================================\n")
print( " 3: ? -> [0, 0, 0, 0, 1, 2, 0, 2, 4] ")
print( " 3A: " + str(loopyThree()))
print( " 3B: " + str(listcompThree()))
print ("\n==========================================\n")
print( " 4: Composites on range [0,100], in ascending order. ")
print( " 4A: " + str(loopyFour()))
print( " 4B: " + str(listcompFour()))
print ("\n==========================================\n")
print( " 5: Primes on range [0,100], in ascending order. ")
print( " 5A: " + str(loopyFive()))
print( " 5B: " + str(listcompFive()))
print ("\n==========================================\n")
print( " 6: All divisors of a number, listed in ascending order. ")
print( " 6A: " + str(loopySix(100)))
print( " 6B: " + str(listcompSix(100)))
print ("\n==========================================\n")
print( " 7: Transpose a matrix (turn rows into columns and vice-versa...). ")
print( " 7A: " + str(loopySeven()))
print( " 7B: " + str(listcompSeven()))
print ("\n==========================================\n")
