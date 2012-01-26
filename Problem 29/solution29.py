#! /usr/bin/env python

seq = []
for a in range(2, 101):
   for b in range(2, 101):
      c = a**b
      if c not in seq:
         seq.append(c)

print len(seq)
