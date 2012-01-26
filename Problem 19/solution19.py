#! /usr/bin/env python

month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
leap = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
year = 1900
day = 7           # First sunday fell on 7th Jan 1900 (but we don't count that one)
cnt = 0           # So far no sunday has been on the 1st
while day < 365:
   day += 7
year += 1
day = day % 365   # First sunday in the last millenia fell on the day % 365 (6th)
i = 0
while year < 2001:
   if year % 4 != 0:
      while day < month[i]:
         day += 7
      if day % month[i] == 1:
         cnt += 1
      day = day % month[i]
   else:
      while day < leap[i]:
         day += 7
      if day % leap[i] == 1:
         cnt += 1
      day = day % leap[i]
   i += 1
   if i == 12:
      year += 1
      i = 0
print cnt
