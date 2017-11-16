'''
Generates a key for LSFR sequence and applies it to a plaintext message.
Can customize key generation by editing lines 10 and 29.
Takes a "binary" string as input and outputs the same.
'''
def genkey(length, start):
    n = len(start)

    while n < length:
        k = (start[n - 1] + start[n - 3] + start[n - 4]) % 2 # Function to determine next bit
        start.append(k)
        n += 1

    return start


def buildCipher(plain, key):
    cipher = ''
    i = 0
    while i < len(plain):
        n = int(plain[i])
        n = (n + key[i]) % 2
        cipher = cipher + str(n)
        i += 1

    return cipher


initial = [1, 0, 0, 1] # Initial seeding for kit generation function
plain = (input("Enter plaintext: "))
plain = plain.replace(',', '')
plain = plain.replace(' ', '')

size = len(plain)

res = genkey(size, initial)

ciph = buildCipher(plain, res)

print(res)
print(ciph)
