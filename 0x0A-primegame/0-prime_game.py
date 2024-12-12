#!/usr/bin/python3

'''
this problem is about a game in which two players will play
by the same order each time for given rounds (x)

in each round there will be a given numer (n)
and the p1 will choose prime number in range from (0-n)
then that number marked as selected
the first player who can't choose any prime number will be loser of the round
for given rounds (x) where x is the number of rounds
and a list (nums) contain n's for each round find the winner of all round


the solution:
-> first i used algorithm called sieve of eratosthenes
 to determine the prime number less that n
beautifull algorithm that takes O(nlog(n)log(n))

-> then the apprach to determine the winner in each round
is by culclating the number  of primes in each round
if the numer is even then the player2 will by last one to select
hence player2 won the round if its odd player1 won the round
this is O(x) solution where x is the number of rounds

overall it takes O(nlog(n)log(n) + x) to solve this problem.
'''


def sieve_of_eratosthenes(n):
    """Returns a list of boolean"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                # mark all multiplecation of any prime number as composite
                primes[j] = False
    return primes


def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Precompute the cumulative prime counts
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Number of primes up to `n`
        prime_count = prime_counts[n]

        # If prime count is odd, Maria wins (she starts); if even, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
