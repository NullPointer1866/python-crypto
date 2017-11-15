Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']


def shiftword(word, shift):
    shifted = ''
    for letter in word:
        ind = Alphabet.index(letter)
        newind = (shift + ind) % 26

        let = Alphabet[newind]
        shifted = shifted + let

    return shifted

while True:
    w = input("Enter word to shift: ")
    w = w.upper()
    if w == 'E':
        break

    res = {}
    for i in range(26):
        res[i] = shiftword(w, i)

    for key in res.keys():
        print(str(key) + ': ' + str(res[key]))
