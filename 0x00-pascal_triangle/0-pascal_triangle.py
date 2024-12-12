#!/usr/bin/python3

'''
alx interview tasks
'''

def pascal_triangle(n):
    '''construct to the nth pascal tringle row'''
    
    if n < 0:
        return []
    if  n == 0:
        return [[1]]

    tringle = [[1]]
    
    for i in range(1,n):
        element = [1]
        for j in range(1,i):
            element.append(tringle[i-1][j-1] + tringle[i-1][j])
        element.append(1)
        tringle.append(element)
    return tringle
