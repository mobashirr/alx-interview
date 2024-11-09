#!/usr/bin/python3

'''
unlocked boxes problem
we traverse a given gragh and check if we can visit all the vertces
'''


def canUnlockAll(boxes):
    '''check if all boxes can be visited using modifed DFS algorithm'''

    # set to keep track of visited nodes
    visited = set()

    # stack of nodes we start to explore and visit
    stack = [0] # we will start from the box[0]

    if not boxes: return

    size = len(boxes)
    while(stack):

        node = stack.pop() # get the current node we want to explore

        if not node in visited and node < size:
            # if the node haven't been visited then do so
            # also if the node is bigger than the size of our boxes don't visit it
            visited.add(node)
        

        # check if the node is valid index of boxes
        if node < size:
            # append the children of the cuurent node to stack if its not explored yet
            for child in boxes[node]:
                if not child in visited:
                    stack.append(child)

    return  size == len(visited)
