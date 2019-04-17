
def triples(n):
    return [(x,y,z) for x in range(1,n) for y in range(1,n) for z in range(1,n) if x*x+y*y == z*z ]

print triples(100)
