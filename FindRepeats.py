cipher = input("Input the cipher text: ")
cipher = cipher.replace(' ', '').upper()

res = {}

for i in range(4,11):
    for j in range(0, int(len(cipher)/2)):
        sub = cipher[j:j+i]
        repeat = cipher.rfind(sub)

        dif = repeat - j
        if dif <= 0:
            continue

        else:
            res[sub] = dif

for key in res.keys():
    print(str(key) + ": " + str(res[key]))
