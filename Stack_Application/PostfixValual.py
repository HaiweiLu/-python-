from pythonds.basic import Stack

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
    '''
    # 该代码只能实现 10 以内的运算，10 以上的数字匹配没有
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    '''
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

if __name__  == "__main__":
    # 输入的后缀表达式中每一个数字间、数字与运算符间须有空格
    print(postfixEval("17 10 + 3 * 9 /"))
