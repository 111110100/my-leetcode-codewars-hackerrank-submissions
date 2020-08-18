#!/usr/bin/env python3

#import time

def coinChange(coins, amount):
    coin_count = 0
    while amount > 0:
        if not coins and amount > 0:
            return -1
        curr_coin = max(coins)
        print("coins: {l}".format(l=coins))
        print("curr_coin: {i}".format(i=curr_coin))
        print("amount: {i}".format(i=amount))
        print("coin count: {i}".format(i=coin_count))
        if curr_coin <= amount:
            coin_count += 1
            amount -= curr_coin
        else:
            coins.remove(curr_coin)
        if amount == 0:
            return coin_count
        if amount < 0:
            return -1
        print("")
        #time.sleep(1)
    return count


coins = [25, 10, 1]
amount = 30

print(coinChange(coins, amount))
#FAIL
'''
You are given coins of different denominations and a total amount of money 
amount. Write a function to compute the fewest number of coins that you 
need to make up that amount. If that amount of money cannot be made up 
by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''
