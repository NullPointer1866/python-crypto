'''
Computes the GCD of two numbers
'''
a = int(input("Enter value for x: "))
b = int(input("Enter value for y: "))


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

print("The gcd of " + str(a) + " and " + str(b) + " is " + str(gcd(a, b)))
