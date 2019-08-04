from pythonds.basic import Stack

# 利用栈实现 10 进制转换为 2 进制
def divideBy2(decNumber):
    '''
    将整数不断除以 2，每次得到的余数就是由低到高的二进制
    即最早得到余数，反而最后输出(把余数分别输出，而不是作为一个整体输出)
    而起把数字变成字符处理，会简单些，输出是字符，不是数字
    操作步骤：
    1) 先建立一个空栈
    2) 把十进制数除以 2 得到的余数进栈
    3) 并把十进制数更新为除以 2 的商
    4) 重复 2, 3 步骤, 直到十进制数为零为止
    5) 出栈即可

    实际操作中，因为把该功能使用函数实现，因此要返回一个值
    所以要把栈中的数，输出后拼接在一起，再作为函数的返回值
    而拼接使用字符拼接更为方便，字符相加即可，
    故要把栈中数转换为字符
    '''
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(163))
print(divideBy2(1024))