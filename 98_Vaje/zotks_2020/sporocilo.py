# Šifrirano sporočilo 1., 2. in 3. sk. 2020

"""
Vhod
ABAABAABAABAA
3

Izhod
ABA
"""
from collections import Counter

sporocilo = input()
n = int(input())

podniz = [sporocilo[i:i + n] for i, _ in enumerate(sporocilo) if i + n <= len(sporocilo)]

#print(podniz)
count_podniz = Counter(sorted(podniz))

#print(count_podniz)

print(count_podniz.most_common(1)[0][0])
