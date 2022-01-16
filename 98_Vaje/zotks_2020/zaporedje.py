# Srečno zaporedje 1. in 2. sk. 2020

# Test
"""
Vhod
5
42 -17 30 10 -9
10 42 -9 30 -17

Izhod
4
1
5
3
2

"""

n = int(input())
zap_a = input()
zap_b = input()

zap_a = zap_a.split()
zap_b = zap_b.split()

#print(zap_a)

for b in zap_b:
  for i, a in enumerate(zap_a):
    if int(b) == int(a):
      print(i + 1)
      break
