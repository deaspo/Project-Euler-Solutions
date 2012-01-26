#! /usr/bin/env python 
# -*- coding: utf-8 -*-

from copy import *

def getHands(file):
   """Reads hands from file and deals them out to the players """
   cards = []
   file = open(file, "r")

   for line in file:
      card = ''
      for char in line:
         if char != '\n' and char != ' ':
            card = card + char
            if len(card) == 2:
               cards.append(card)
               card = ''
   file.close()

   player1 = []
   player2 = []
   hand = []
   i = 0
   for card in cards:
      i += 1
      hand.append(card)      
      if i == 5:
         player1.append(hand)
         hand = []
      elif i == 10:
         player2.append(hand)
         hand = []
         i = 0
   return player1, player2

if __name__ == "__main__":
   value = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, \
            '10':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
   suit = {'Heart':1, 'Spade':2, 'Diamond':3, 'Club':4}
   player1, player2 = getHands('poker.txt')
   answer = 0
   print 'Answer:', answer