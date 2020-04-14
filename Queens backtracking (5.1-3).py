# Author: Charles Ryan Barrett
# Purpose: Implementation of Queens backtracking and Monte Carlo estimate algorithm for it (5.1-5.3) from Class textbook
# For: CSC 320 bonus credit

import random


col = []  # Global columns variable


def queens(i):
    global col
    if promising(i):
        if i == (len(col) - 1):
            print_board()
            print()
        else:
            for j in range(0, len(col)):
                col[i+1] = j
                queens(i+1)


def promising(i):
    global col
    switch = True

    k = 0
    while k < i and switch:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            switch = False
        k += 1
    return switch


def monte_estimate():
    global col
    n = len(col)
    prom_c = []
    m = 1
    i = 0
    mprod = 1
    num_nodes = 1

    while m != 0 and i != (n-1):
        mprod *= m
        num_nodes += mprod*n
        i += 1
        m = 0

        for j in range(0, n):
            col[i] = j
            if promising(i):
                m += 1
                prom_c.append(j)
        if m != 0:
            j = random.choice(prom_c)
            col[i] = j
    return num_nodes


def avg_estimate(e):
    # The book mentions that the monte carlo algorithm should be ran multiple times and taken the average of
    est = 0
    for i in range(0, e):
        est += monte_estimate()
    est //= e
    return est


# This works well for single digit numbers, but if the board size greater than a digit it displaces things
# The same information can be given by just printing col[], and I am not familiar with print formatting on python
def print_board_graphically():
    global col
    s = '  '
    for k in range(0, len(col)):
        s += str(1+k) + ' '
    s += '\n'
    for i in range(0,len(col)):
        s += str(i+1) + ' '
        for j in range(0, len(col)):
            if col[j] == i:
                s += 'Q '
            else:
                s += '- '
        s += '\n'
    print(s)


def print_board():
    global col
    board = [0]*len(col)
    for x in range(0, len(col)):
        board[x] = col[x] + 1   # This just makes it easier to tell which row and column by starting at 1 instead of 0
    print(board)


def main():
    global col


    go = True
    while go:
        inny = int(input("Enter number of rows and columns:\n"))
        col = [0]*inny
        print('Average number of nodes to be pruned: ', avg_estimate(20))   # Book mentions 20 is a good number
        print("Here are all possible positions for Queens on a", inny, 'x', inny, 'size board')
        queens(-1)


if __name__ == '__main__':
    main()