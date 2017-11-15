Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

Inverses = (1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25)


def unaffine(a, b, c):
    p = (a*(c - b)) % 26
    return p

Ciphertext = input("Enter the message to decrypt: ")
Ciphertext = Ciphertext.upper()

results = open('DecryptAffine.txt', 'w')

for inverse in Inverses:
    decrypted = ''

    for beta in range(0, 26):
        decrypted = ''

        for letter in Ciphertext:
            code = Alphabet.index(letter)
            plain = unaffine(inverse, beta, code)

            decrypted += Alphabet[plain]

        results.write('Key: inverse of alpha = ' + str(inverse) + ', beta = ' + str(beta) + '\n')
        results.write(decrypted)
        results.write('\n\n')

results.close()
