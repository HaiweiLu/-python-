# 美元找零，美元有 penny 1 分、nikel 5 分、dime 10 分、quarter 25 分

'''
问题解决思路：
1. 首先是确定基本结束条件，兑换硬币问题最直接的情况就是，
兑换的找零，其面值正好等于某种硬币
2. 其次是减小规模，在美元体系里，我们要尝试 4 次
1) 找零减去 1 分(penny)后，求兑换硬币最少的解(递归调用自身)
2) 找零减去 5 分(nikel)后，求兑换硬币最少的解
3) 找零减去 10 分(dime)后，求兑换硬币最少的解
4) 找零减去 25 分(quarter)后，求兑换硬币最少的解
'''

# 这种递归过多，无用功做太多了，效率太低，找零 63 分，要 31 秒
def recMC(coinValueList, change):
    minCoins = change
    # 如果要找零的数值恰好是法币的面值，直接返回 1
    if change in coinValueList:
        return 1    # 最小规模，直接返回
    else:   # 减小规模：每次减去一种硬币面值挑选最小数量的
        # [c for c in coinValueList if c <= change] 生成一个小于找零(change)的货币面值列表
        # for i in [] 是 i 遍历列表，i 从列表第一个数字开始，逐一等于列表中的元素  
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins

def recMC1(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1    # 最小规模的记录
        return 1
    elif knownResults[change] > 0:  # 查表命中直接返回
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC1(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins     # 记录部分找零最优解
                print(knownResults)
    return minCoins


import time

start = time.time()
print(start)
print("mincoins: ", recMC1([1, 5, 10, 25], 63, [0]*64))
end = time.time()
print(end - start)
# 花费了 31 秒