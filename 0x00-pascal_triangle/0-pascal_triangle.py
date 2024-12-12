#!/usr/bin/python3

'''
alx interview tasks
'''

def pascal_triangle(n):
    '''construct to the nth row pascal tringle'''
    
    if n < 0:
        return []
    
    tringle = []

    for row in range(n):
        elements = []
        elements.append(1)
        if row == 0:
            tringle.append(elements)
            continue
        elif (row > 0):
            for j in range(1,row):
                # note: when ever you retrive kind of a serial its better to
                # start from 1 to the index
                # get elements j and j-1 to avoid out of range 
                elements.append(tringle[row-1][j-1] + tringle[row-1][j])
        elements.append(1)
        tringle.append(elements)
    return tringle
