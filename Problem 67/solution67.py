#! /usr/bin/env python

from math import *

def getTriangle(file):
   # Store triangle in list
   triangle = []
   file = open(file, "r")
   for line in file:
      number = ''
      for char in line:
         if char != '\n' and char != ' ':
            number = number + char
            if len(number) == 2:
               triangle.append(int(number))
               number = ''
   file.close()
   return triangle

def getDownLeft(pos):
   return (pos[0] + 1, pos[1])

def getDownRight(pos):
   return (pos[0] + 1, pos[1] + 1)

def getTriangleElementAtPos(pos):
   row = (pos[0] * (pos[0] + 1)) / 2
   return row + pos[1]

def getOptimalSum(triangle):
   # Start at row above bottom of pyramid
   startRow = int(round(0.5 * (sqrt(8 * len(triangle) + 1) - 1))) - 2
   pos = (startRow, 0)

   # Work your way bottom up
   while pos[0] >= 0:         # For each row
      while pos[1] <= pos[0]: # For each column
         left = getDownLeft(pos)
         right = getDownRight(pos)
         leftScore = triangle[getTriangleElementAtPos(pos)] + triangle[getTriangleElementAtPos(left)]
         rightScore = triangle[getTriangleElementAtPos(pos)] + triangle[getTriangleElementAtPos(right)]
         maxScore = max(leftScore, rightScore)
         triangle[getTriangleElementAtPos(pos)] = maxScore
         pos = (pos[0], pos[1] + 1) # Move right in the pyramid
      pos = (pos[0] - 1, 0)
   return triangle[0]

if __name__ == "__main__":
   triangle = getTriangle("large_triangle.txt")
   optimalSum = getOptimalSum(triangle)
   print 'Answer:', optimalSum

   