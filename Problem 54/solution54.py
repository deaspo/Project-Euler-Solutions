#! /usr/bin/env python 
# -*- coding: utf-8 -*-
pip = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
suit = {'H':1, 'S':2, 'D':3, 'C':4}
def main():
   player1, player2 = getHands('poker.txt')


def getHands(file):
   """Reads hands from file and deals them out to the players """
   cards = []
   file = open(file, "r")
   cards = [char for line in file for char in line if char != '\n' and char != ' ' and char != '\r']
   cards = [i+j for i,j in zip(cards[::2],cards[1::2])]
   file.close()

   player1 = [cards[5*i:5*i+5] for i in xrange(0, len(cards)/5, 2)]
   player2 = [cards[5*i+5:5*i+10] for i in xrange(0, len(cards)/5, 2)]

   return player1, player2

if __name__ == "__main__":
   from time import time
   
   start = time()
   answer = main()
   stop = time()
   print 'Answer:', answer
   print 'Time:', stop - start