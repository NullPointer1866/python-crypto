s1 = {'0': {"000": "101", "001": "010", "010": "001", "011": "110",
            "100": "011", "101": "100", "110": "111", "111": "000"},
      '1': {"000": "001", "001": "100", "010": "110", "011": "010",
            "100": "000", "101": "111", "110": "101", "111": "011"}}  # S-box 1

s2 = {'0': {"000": "100", "001": "000", "010": "110", "011": "101",
            "100": "111", "101": "001", "110": "011", "111": "010"},
      '1': {"000": "101", "001": "011", "010": "000", "011": "111",
            "100": "110", "101": "010", "110": "001", "111": "100"}}  # S-box 2


def buildkeys():
    res = []
    f = open('keys.txt', 'r')  # Keys.txt is a file containing all possible keys

    # Read them in one at a time
    # Make sure they're formatted correctly
    # Place them in the list of keys
    for line in f:
        line = line.replace('\n', '')
        while len(line) < 9:
            line = '0' + line
        res.append(line)

    return res


def roundkey(k, i):
    newkey = ''
    for j in range(8):
        newkey = newkey + k[(j+i) % 9]

    return newkey


def xor(bits1, bits2):
    res = ''

    for num in range(len(bits1)):
        n = (int(bits1[num]) + int(bits2[num])) % 2
        res = res + str(n)

    return res


def expand(r):
    res = ''
    # 0 1 3 2 3 2 4 5
    res = res+r[0]+r[1]+r[3]+r[2]+r[3]+r[2]+r[4]+r[5]
    return res


def sbox1(bits):
    res = s1[bits[0]][bits[1:]]  # Grab the result from S-box 1
    # print("s1 results: " + res)
    return res


def sbox2(bits):
    res = s2[bits[0]][bits[1:]]  # Grab the result from S-box 2
    # print("s2 results: " + res)
    return res


def f(bits, key):
    bits = expand(bits)  # Expand to 8 bits
    bits = xor(bits, key)  # XOR with the key
    # print("After expanding and XOR: "+bits)

    lbits = bits[:4]  # Get the first 4 bits
    rbits = bits[4:]  # Get the second 4 bits

    lbits = sbox1(lbits)  # Calculate new 3 bit sequence
    rbits = sbox2(rbits)  # Calculate second 3 bit sequence

    bits = lbits + rbits  # Concatenate and return
    return bits


def simDES(left, right, key, round):
    oldright = right  # Save value of R for end

    key = roundkey(key, round)  # Generate the key for this round

    postR = f(right, key)  # Apply the function

    right = xor(postR, left)  # XOR the results to get the new right
    left = oldright  # Map the old right to the left
    return left+right  # Concatenate and return


def decryptsim(decryptbits, key, rounds):
    while rounds >= 0:
        L = decryptbits[:6]
        R = decryptbits[6:]
        decryptbits = simDES(L, R, key, rounds)
        print("With " + str(rounds) + " rounds left, the bitstring is: " + decryptbits)
        rounds -= 1

    L = decryptbits[:6]
    R = decryptbits[6:]

    decryptbits = R + L
    print("The final decryption is: " + decryptbits)


def dosimDES(bitstring, key, rounds):
    for i in range(rounds):
        L = bitstring[:6]  # Take first 6 bits
        R = bitstring[6:]  # Take second 6 bits
        bitstring = simDES(L, R, key, i)
        print("After " + str(i) + " rounds, the bitstring is: " + bitstring)

    return bitstring
