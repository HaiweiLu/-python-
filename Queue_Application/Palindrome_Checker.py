from pythonds.basic import Deque

def palchecker(aString):
    '''
    把字符存进双端队列里，
    再分别从头尾出队元素，
    逐一配对，是否相等
    '''
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

if __name__ == "__main__":
    print(palchecker("qwert"))
    print(palchecker("asddsa"))