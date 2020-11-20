class Solution:
    def coinChange(self, coins, amount):
        if not amount:
            return 0
        dp = [amount + 1] * (amount + 1)
        for i in range(amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            candidates = [dp[i - coin] + 1 for coin in coins if i - coin > 0]
            if candidates:
                dp[i] = min(candidates)

        return -1 if dp[amount] > amount else dp[amount]

answer = Solution()
print(answer.coinChange([1,2,5], 11)) 
print(answer.coinChange([186,419,83,408], 6429)) 

'''
class Solution:
    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        coin_list = []
        for i in range(len(coins)):
            while amount >= coins[i]:
                amount -= coins[i]
                coin_list.append(coins[i])

        return len(coin_list)
'''