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
    return e


coins = [25, 10, 1]
amount = 30

print(coinChange(coins, amount))
#FAIL
