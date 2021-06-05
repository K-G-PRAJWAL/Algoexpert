def numberOfWays(n, denoms):
    """
    Time: O(ND), D = No. of Denominations
    Space: O(N), N = Target Amount
    """
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]


print(numberOfWays(10, [1, 2, 5, 10, 25]))
