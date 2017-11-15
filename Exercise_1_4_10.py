from random import randrange
import SimpleDES

bitstring = input("Enter the string to be encoded: ")
rounds = int(input("Enter rounds of encryption: "))

# Assume you were given good input (don't break pls)

keys = SimpleDES.buildkeys()  # Creates list of keys

K = keys[randrange(len(keys))]  # Pick random key
# K = '110100101'  # Static key for testing

newbitstring = SimpleDES.dosimDES(bitstring, K, rounds)

decrypt = input("Do you want to decrypt? (y/n): ")

if decrypt == 'y':
    L = newbitstring[:6]
    R = newbitstring[6:]
    rev = rounds - 1

    decryptbits = R + L
    SimpleDES.decryptsim(decryptbits, K, rev)

findweak = input("Do you want to find weak keys? (y/n): ")

if findweak == 'y':
    weak = []
    for key in keys:
        print("Key: " + key)
        firstpass = SimpleDES.dosimDES(bitstring, key, 4)
        secondpass = SimpleDES.dosimDES(firstpass, key, 4)

        if secondpass == bitstring:
            weak.append(key)
    print(weak)

swappy = input("Do you want to find weak keys for swappy encryption? (y/n): ")


def swap(message):
    first = message[:6]
    second = message[6:]
    temp = second

    second = first
    first = temp

    res = first + second
    return res

if swappy == 'y':
    swappyweak = []
    for key in keys:
        print("Key: " + key)
        firstpass = SimpleDES.dosimDES(bitstring, key, 4)
        firstpass = swap(firstpass)

        secondpass = SimpleDES.dosimDES(firstpass, key, 4)
        secondpass = swap(secondpass)

        if secondpass == bitstring:
            swappyweak.append(key)
    print(swappyweak)

'''
SimpleDES Algorithm: 

Message has 12 bits: 6 in L and 6 in R
Key has 9 bits.

1 round:
    i is the round number, up to n rounds
    L(i - 1)R(i - 1) maps to LiRi
    Li = R(i - 1)
    Ri = L(i - 1) XOR f(R(i - 1), Ki)

f(R, K):
    Input R is expanded from 6 bits to 8 bits:
        0 1 2 3 4 5 -> 0 1 3 2 3 2 4 5
    
    E(R) is XOR with Ki:
        Ki is 8 bits starting at bit i of K
        and wrapping as needed
        
    Split in to 4 bits and 4 bits
    
    First 4 Bits sent to S1:
        S is a box containing 2 rows and 8 columns
        Bit 1 indicates row, 0 for first, 1 for second
        Bits 2,3,4 indicate column (binary 0 - 8)
        Entry here is 3 bit sequence (see book for layout)
        Return this entry
    
    Second 4 bits are sent to S2:
        Same scheme as S1, different entries
        Return entry located at given row and column
        
    Combine results to make new 6 bit string
    
    This is f(R, K)
    
    Goes on to be XOR with L(i-1) giving Ri
'''
