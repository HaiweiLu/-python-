from pythonds.basic import Stack

rStack = Stack()

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base

    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())

    return res

if __name__ == "__main__":
    print(toStr(2341, 16))