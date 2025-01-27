import random

def get_cipher():
    numbers = list(range(3, 21))
    cipher = random.choice(numbers)
    return cipher

psn = {}
psn.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
psn.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
psn.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
psn.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
psn.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
psn.update({20: 13141911923282183731746416515614713812911})

n = get_cipher()
print('Слишком древний шифр:', n)

pnm1 = list(range(1, n))
pnm2 = list(range(1, n))
pairs = []
result = ''

for i in pnm1:
    for j in pnm2:
        pn1 = i
        pn2 = j
        if pn1 >= pn2:
            continue
        else:
            k = n % (pn1 + pn2)
            if k == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print(*pairs)
print(result)