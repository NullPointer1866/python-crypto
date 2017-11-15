Alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z')


def shift(orig, shifter):
    post = (Alphabet.index(orig) + Alphabet.index(shifter)) % 26
    postletter = Alphabet[post]

    return postletter

key = input("Enter the key (no spaces): ")
key = key.upper()

message = input("Enter the message to be encrypted: ")
message = message.replace(" ", "").upper()

crypto = ""

for i in range(len(message)):
    print(i)
    cryptoletter = shift(message[i], key[i%len(key)])

    crypto += cryptoletter

print(crypto)

