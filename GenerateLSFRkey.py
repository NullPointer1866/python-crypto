def genkey(length, start):
    n = len(start)

    while n < length:
        k = (start[n - 1] + start[n - 3] + start[n - 4]) % 2
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


initial = [1, 0, 0, 1]
plain = (input("Enter plaintext: "))
plain = plain.replace(',', '')
plain = plain.replace(' ', '')

size = len(plain)

res = genkey(size, initial)

ciph = buildCipher(plain, res)

print(res)
print(ciph)
