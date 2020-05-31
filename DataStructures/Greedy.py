# coding=utf-8
#!/usr/bin/python3

def rec_mc(coin_list, change):
    min_coins = change
    if change in coin_list:
        return 1
    else:
        for i in [c for c in coin_list if c <= change]:
            num_coins = 1 + rec_mc(coin_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins
# 很慢而且不正确，缺乏缓存表减少运算量
# print(rec_mc([1,5,10,25],63))


"""
动态规划
自底向上，从问题规模最小的单元开始往上推
最困难的是找出状态转移方程
最核心的思想是保存结果，降低复杂性，以空间换时间令动态规划有使用价值
"""


def fib(n):
    # 动态规划法计算斐波那契数列
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        print(i)
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


print(fib(10))


# TODO:动态待补全