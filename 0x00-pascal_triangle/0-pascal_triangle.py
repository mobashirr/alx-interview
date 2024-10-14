#!/usr/bin/python3


def pascal_triangle(n):
    '''construct to the nth pascal tringle row'''
    
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
                elements.append(tringle[row-1][j-1] + tringle[row-1][j])
        elements.append(1)
        tringle.append(elements)
    return tringle
