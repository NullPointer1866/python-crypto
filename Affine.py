'''
	Computes simple affine cipher ( (a*x + b) % 26 ) 
'''
Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']


alpha = int(input("Enter alpha"))
beta = int(input("Enter beta"))
message = input("Enter message")


def affine(a, b, letter):
    return (a*letter + b) % 26


def encode(secret):
    secret = secret.replace(' ', '')
    secret = secret.upper()
    ciphertext = ''
    for letter in secret:
        orig = Alphabet.index(letter)
        coded = affine(alpha, beta, orig)
        newletter = Alphabet[coded]
        ciphertext = ciphertext + newletter
    return ciphertext


print(encode(message))


