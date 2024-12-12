#!/usr/bin/python3

'''
in this module we will be solving intersting problem which is prime game problem

the idea is that we will be given a number of roundes that two players will play and array contains numbers 

for each round there will be a given n number from the array
then starting from the player one that will choose prime numbers which is from 0 - n
when the player choose the number the number and its multiplys will be marked which means they can't be choosen anymore
the game goes on like this unitl the first player who can't find any prime number to choose will be the loser of the game

'''

import math

def prime(n):
    '''
    find prime number from range 0 to n
    @n: limit
    Return: list of boolean of nummbers that are prime
    '''

    if n < 0:
        return []
    elif n <= 1:
        return [False]

    nums = [True for _ in range(n+1)]
    num = 2

    nums[0] = False
    nums[1] = False

    while(num < math.sqrt(n)):
        if nums[num]:
            '''the nummber is not marked so its prime then we update the array'''
            for mul in range(num ** 2,n + 1, num):
                '''mark all mul of that numer as composite'''
                nums[mul] = False
        num += 1
    return nums


def req_sol(turn,primes):
    '''
    @primes: list of prime numbers
    '''
    if len(primes) == 0:
        # base case which is the player don't have any prime number to choose
        if turn == 1:
            # this mean our p1 did not won
            return False
        else:
            return True
    
    winner = False
    for prime in primes:
        if turn == 1:
            primes = list(filter(lambda x: (x != prime) and (x % prime != 0), primes))
            winner  = req_sol(2,primes)
        elif turn == 2:
            primes = list(filter(lambda x: (x != prime) and (x % prime != 0), primes))
            winner = req_sol(1,primes)
        
        if winner:
            return False # this mean the base case returned True (that the first player don't have choise)

    return True

def isWinner(x, nums):
    '''
    prime game check winner
    @x: number of roundes to play
    @nums: array contain n for each round
    Return: the winner
    '''
    p1,p2 = 0,0

    for round in range(x):
        prime_list = []
        # for each round
        for ind,num in enumerate(prime(nums[round])):
            if num:
                prime_list.append(ind)

        # print(prime_list)
        winner = req_sol(1,prime_list)

        if winner:
            # print(f'round {round} p1 won')
            p1 +=1
        else:
            #print(f'round {round} p2 won')
            p2 +=1

    if p2 > p1:
        print('Winner: Ben')
    else:
        print('Winner: Maria')

# isWinner(3, [4,5,1])