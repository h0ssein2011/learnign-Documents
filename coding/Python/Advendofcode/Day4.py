
""" this program will generate will provide solution for the advent of code day 4

    the input file is provided in the form of a list of strings, each string is a row of the board
    the first row is the top row of the board, the second row is the second row of the board, and so on.
    the board is always 5x5
    the board is filled with integers, the integers are the number of times a certain letter appears in the row

steps:
1- read the input file --> done
2- seprate rand row from the boards --> done
3- create a list of boards --> done
4- create a class to represent the board and calulate win and score methods
5- for each board in the list of boards: 
    5.1- create a board object
    5.2- calculate the score of the board
    5.3- if this board is a win board, multiply the score by the last random number
"""

import this
import numpy as np
import re

with open('Day4.txt', 'r') as f:
    data = f.readlines()
    f.close()

data = [x.strip() for x in data]
rands =  data[0].split(',')
rands = [int(x) for x in rands]
data = [x for x in data[1:] if x != '']


class Board:
    def __init__(self,data):
        self.data = data
        self.marked = np.zeros((5,5))

    def mark(self,num):
        for i in range(5):
            for j in range(5):
                if self.data[i,j] == num:
                    self.marked[i,j] = 1

    def win(self):
        win = False
        for i in range(5):
            if np.sum(self.marked[i,:]) == 5:
                win = True

        for j in range(5):
            if np.sum(self.marked[:,j]) == 5:
                win = True
        return win

    def score(self,called):
        score = 0
        for i in range(5):
            for j in range(5):
                if self.marked[i,j] == 0:
                    score += self.data[i,j]
        return score * called

def fill_board(start):
    board = np.zeros((5,5))
    for i in range(5):
        row = re.sub(' +',' ',data[start+i])
        row = row.split(' ')
        row = [int(x) for x in row]
        for j in range(5):
            board[i,j] = row[j] 
    return board

def read_all_boards():
    boards = [] 
    for i in range(0,len(data),5):
        this_board = fill_board(i)
        boards.append(Board(this_board))
    return boards

boards = read_all_boards()

for r in rands:
    for b in boards:
        b.mark(r)
        if b.win():
            print(b.score(r))
            exit()