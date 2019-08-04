'''
代码分两大部分，一部分是处理把中缀表达式转换为后缀表达式
另一部分是如何求后缀表达式的值
'''
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

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def postfixEval(postfixExpr):
    operandStack = Stack()
    # 把后缀表达式以空格分割，并把结果存在列表
    tokenList = postfixExpr.split()
    
    # 修改后，可以实现 10 以上的数字运算
    for token in tokenList:
        if token in "+-*/":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
        else:
            operandStack.push(int(token))

    return operandStack.pop()

if __name__ == "__main__":
    infixexpr = input("请输入以空格相间的中缀表达式：")
    #postexpr = infixToPostfit("( 16 - 9 ) * 6")
    postexpr = infixToPostfit(infixexpr)

    print("运算结果为：", postfixEval(postexpr))

