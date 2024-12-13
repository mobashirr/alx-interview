#!/usr/bin/python3

'''
make change problem with greedy solution
'''

def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make the total.
    :param coins: List of coin denominations
    :param total: Total amount
    :return: Fewest number of coins or -1 if total cannot be met
    """

    if total <= 0:
        return 0
    count_coins = 0

    # sort the coins from greater
    coins.sort(reverse=True)

    # use greedy approach to solve the problem:
    for coin in coins:
        if total == 0:
            break
        if coin < total:
            # if the coin less than the total take the most
            poss = total / coin
            count_coins += poss
            total -= poss * (coin)
    return count_coins if total == 0 else -1
