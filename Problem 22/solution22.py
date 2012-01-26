#! /usr/bin/env python

names, name, score, total, cnt = [], '', 0, 0, 0
file = open('names.txt', 'r')
for line in file:
   for char in line:
      if cnt == 2:
         cnt = 0
         names.append(name);
         name = ''
      elif char == '"':
         cnt += 1
      elif char != ",":
         name += char
names.append(name)

names.sort()
value = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,
      'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21,
      'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
cnt = 1
for name in names:
   for letter in name:
      score += value[letter]
   total += cnt*score
   score = 0
   cnt += 1
print total
