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

    coins.sort(reverse=True)  # Sort coins in descending order
    num_coins = 0

    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            poss = total // coin  # Use as many of this coin as possible
            num_coins += poss
            # Reduce the total by the coin value times count
            total -= poss * coin

    return num_coins if total == 0 else -1
