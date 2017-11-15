'''
Takes a message string and converts
each character to corresponding value 
of letter (position in alphabet with A = 0)
'''
Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

plain = input("Enter the message to convert: ")
plain = plain.replace(' ', '').upper()

out = ''

for i in range(len(plain)):
    num = Alphabet.index(plain[i])
    out = out + str(num) + ', '

print(out)
