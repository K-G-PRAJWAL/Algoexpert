def minNumberOfCoinsForChange(n, denoms):
    """
    Time: O(ND), D = No of denominations
    Space: O(N), N = Amount
    """
    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                numOfCoins[amount] = min(
                    numOfCoins[amount], 1 + numOfCoins[amount - denom])
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1


print(minNumberOfCoinsForChange(6, [1, 2, 4]))
