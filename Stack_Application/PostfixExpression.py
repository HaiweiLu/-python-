from pythonds.basic import Stack

def infixToPostfit(infixexpr):
    # 记录操作符优先级
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    # 解析表达式到单词列表
    tokenList = infixexpr.split()
    #print(tokenList)
    '''
    for token in tokenList:
        # 这样识别有一个 bug，只能识别单个数字和字母，两位数及其以上都不行
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:   # 操作符
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    '''
    for token in tokenList:
        if token in "+-*/":
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            postfixList.append(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())   # 操作符
    return " ".join(postfixList)    # 合成后缀表达式

if __name__ == "__main__":
    #print(infixToPostfit("A * B + C * D"))
    #print(infixToPostfit("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infixToPostfit("( 16 - 9 ) * 6"))
    print(infixToPostfit("10 + 3 * 5 / ( 16 - 4 )"))


