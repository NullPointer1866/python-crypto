'''
Function for computing the solution to 
ax + by = c using the Euclidean algorithm.
Only works for c = 1 (sorry)
'''
a = int(input("Enter a value for x: "))
b = int(input("Enter a value for y: "))

def extEuclid(a, b):
    if a == 0:
        return(b, 0, 1)
    else:
        w, y, x = extEuclid(b % a, a)
        return(w, x - (b // a) * y, y)

ans = extEuclid(a, b)

print(ans)
