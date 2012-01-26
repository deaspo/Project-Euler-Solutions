#! /usr/bin/env python 

def getWords(path):
   words = []
   file = open(path, "r")
   beginFound = False
   endFound = False
   for line in file:
      word = ''
      for char in line:
         if beginFound and (str(char) == '"'):
            endFound = True
         elif (str(char) == '"') and not beginFound:
            beginFound = True
         elif beginFound and not endFound:
            word += str(char)
         elif beginFound and endFound:
            beginFound = False
            endFound = False
            words.append(word)
            word = ''
   return words

def isTriangleWord(word, letterValues):
   sum = 0
   for char in word:
      sum += letterValues[char]
   N = n = 1
   while N <= sum:
      if N == sum:
         return True
      else:
         n += 1
         N = (n * (n + 1) / 2)
   
   return False
   
if __name__ == "__main__":
   words = getWords('words.txt')
   letterValues = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
   answer = 0
   for word in words:
      if isTriangleWord(word, letterValues):
         answer += 1
   print 'Answer:', answer