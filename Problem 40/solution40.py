#! /usr/bin/env python

if __name__ == "__main__":
   fraction = ''
   i = 1
   while len(fraction) < 1000000:
      fraction = fraction + str(i)
      i = i + 1
   print int(fraction[0]) * int(fraction[9]) * int(fraction[99]) * int(fraction[999]) * int(fraction[9999]) * int(fraction[99999]) * int(fraction[999999])