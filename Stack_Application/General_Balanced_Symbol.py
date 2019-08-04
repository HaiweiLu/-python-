from pythonds.basic import Stack

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

# 通用的括号匹配
def parChecker_General(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    #print("---------------")
    print(parChecker_General('{[()]}'))
    print(parChecker_General("([{(())}])"))
    print(parChecker_General("{(}]"))
