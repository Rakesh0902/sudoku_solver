# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:32:00 2020

@author: carso
"""

#Delivery 1

import pandas as pd
import numpy as np
print("***DELIVERY 1***")
def main():
    df = pd.read_excel('clues.xlsx', header = None)
    print("***DATAFRAME***")
    print(df)
    puzzle = np.array(df.values)
    print("***ARRAY***")
    print(puzzle)
    for i in range(9):
    # get columns
        lst = puzzle[:,i]
        print("Column", i+1, ":", isValid(lst))
        #print(lst)
        lst = []
    # get rows
    for i in range(9):
        lst = puzzle[i,:]
        print("Row", i+1, ":", isValid(lst))
        #print(lst)
        lst = []
    # get blocks
    for i in range(0,3):
        for j in range(0,3):
            lst.append(puzzle[i,j])
    lst = np.array(lst)
    #print(lst)
    print("Box 1:" ,isValid(lst))
    
    lst = []
    for i in range(0,3):
        for j in range(3,6):
            lst.append(puzzle[i,j])
    lst = np.array(lst)
    #print(lst)
    print("Box 2:" ,isValid(lst))

    lst = []
    for i in range(0,3):
        for j in range(6,9):
            lst.append(puzzle[i,j])
    lst = np.array(lst)
    #print(lst)
    print("Box 3:" ,isValid(lst))

    lst = []
    for i in range(3,6):
        for j in range(0,3):
            lst.append(puzzle[i,j])
    lst = np.array(lst)
    #print(lst)
    print("Box 4:" ,isValid(lst))

    lst = []
    for i in range(3,6):
        for j in range(3,6):
            lst.append(puzzle[i,j])
    lst = np.array(lst)
    #print(lst)
    print("Box 5:" ,isValid(lst))

    lst = []
    for i in range(3,6):
        for j in range(6,9):
            lst.append(puzzle[i,j])
    lst = np.array(lst)
    #print(lst)
    print("Box 6:" ,isValid(lst))

    lst = []
    for i in range(6,9):
        for j in range(0,3):
            lst.append(puzzle[i,j])
    lst = np.array(lst)
    #print(lst)
    print("Box 7:" ,isValid(lst))

    lst = []
    for i in range(6,9):
        for j in range(3,6):
            lst.append(puzzle[i,j])
    lst = np.array(lst)
    #print(lst)
    print("Box 8:" ,isValid(lst))

    lst = []
    for i in range(6,9):
        for j in range(6,9):
            lst.append(puzzle[i,j])
    lst = np.array(lst)
    #print(lst)
    print("Box 9:" ,isValid(lst))
    
def isValid(lst):
    lst2 = list(lst)
    lst2 = set(lst2)
    lst2.discard(0)
    lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = set(lst3)    
    if len(lst2) == len(s):
        reply = True
    else:
        reply = False
    return reply    
main() 

#Delivery 2

print("***DELIVERY 2***")
def main():
    df = pd.read_excel('clues.xlsx', header = None) #Reads the puzzle as a dataframe
    print("***DATAFRAME***")
    print(df)
    puzzle = np.array(df.values) #Converts dataframe to a numpy array
    print("***ARRAY***")
    print(puzzle)
    for i in range(9): #Creates a loop that goes through each cell one at a time
        for j in range(9):
            cell = cell_finder(i, j, puzzle) #See cell_finder function below
            
            if cell == 0:
               row_lst = row_finder(i, puzzle) #See row_finder function below
               #print("Row_lst:", row_lst)
               column_lst = column_finder(j, puzzle) #See column_finder function below
               #print("Column_lst:", column_lst)
               block_lst = []
#Gives a list of numbers in the current block               
               if -1<i<3 and -1<j<3:
                   for x in range(0,3):
                       for y in range(0,3):
                           block_lst.append(puzzle[x,y])
               if -1<i<3 and 2<j<6:
                   for x in range(0,3):
                       for y in range(3,6):
                           block_lst.append(puzzle[x,y])
               if -1<i<3 and 5<j<9:
                   for x in range(0,3):
                       for y in range(6,9):
                           block_lst.append(puzzle[x,y])
               if 2<i<6 and -1<j<3:
                   for x in range(3,6):
                       for y in range(0,3):
                           block_lst.append(puzzle[x,y])
               if 2<i<6 and 2<j<6:
                   for x in range(3,6):
                       for y in range(3,6):
                           block_lst.append(puzzle[x,y])
               if 2<i<6 and 5<j<9:
                   for x in range(3,6):
                       for y in range(6,9):
                           block_lst.append(puzzle[x,y]) 
               if 5<i<9 and -1<j<3:
                   for x in range(6,9):
                       for y in range(0,3):
                           block_lst.append(puzzle[x,y])
               if 5<i<9 and 2<j<6:
                   for x in range(6,9):
                       for y in range(3,6):
                           block_lst.append(puzzle[x,y])
               if 5<i<9 and 5<j<9:
                   for x in range(6,9):
                       for y in range(6,9):
                           block_lst.append(puzzle[x,y])
               
               solutions = solution_finder(row_lst, column_lst, block_lst) #See solutions_finder function below
               print("Row", i+1, "Column", j+1, "=", solutions)
               
               if len(solutions) == 1: #If there can only be 1 solution for a cell
                   solutions = list(solutions)
                   value = min(solutions) #Use min function just to obtain the value from the list
                   puzzle[i,j] = value #Replace the 0 in the cell with the solution
    print("***NEW ARRAY***")
    print(puzzle)

def cell_finder(x, y, p): #Returns the value of a cell given its row and column #s
    row = x
    column = y
    cell = p[row, column]
    return cell

def row_finder(x, p): #Returns a list of numbers in the current row
    lst = list(p[x,:])
    return lst

def column_finder(y, p): #Returns a list of numbers in the current column
    lst2 = list(p[:,y])
    return lst2

def solution_finder(row_lst, column_lst, block_lst): #Returns a set of numbers that are within 1-9 but not in the row, column, or block lists
    cell_lst = row_lst + column_lst + block_lst
    numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    solutions = numbers.difference(cell_lst)
    return solutions

main() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    