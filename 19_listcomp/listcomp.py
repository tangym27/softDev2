# Student Union (SU)

def union(a, b):
    # a.extend(b)
    # print a
    return [element for element in a if element not in b] + b

    # return [a[element] for element in range(0, len(a)) for element2 in (element,len(a)-1) if not a[element] == a[element2]]
# NOT WORKING YET
print "union"
print union([1,2,3], [2,3,4])


#intersection
def intersection(a, b):
    return [element for element in a for element2 in b if element == element2]
print "intersection"
print intersection([1,2,3], [2,3,4])


#set difference, find what is not in it
def difference(a, b):
    return [element for element in a if element not in b]

print "difference"
print difference([1,2,3], [2,3,4])

def symDiff(a, b):
    return union(difference(a, b), difference(b, a))

print("symDiff")
print(symDiff([1,2,3], [2,3,4]))

def cartProd(a, b):
    return [(element, element2) for element in a for element2 in b]

print("cartProd")
print(cartProd([1,2], ['red','white']))

def even(a, b):
    return [element for element in union(a,b) if element % 2 == 0]
