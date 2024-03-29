from pythonds.basic import Stack

# 括号匹配的栈算法
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

if __name__ == "__main__":
    print(parChecker('((()))'))
    print(parChecker('(()(())())'))
    print(parChecker('(()'))