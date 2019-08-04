# 栈顶尾端实现，其 push/pop 的复杂度为 O(1)
class Stack:
    '''
    Stack(): 创建一个空栈，其中不包括任何数据项
    push(item): 将 item 数据项加入栈顶，无返回值
    pop(): 将栈顶数据项移除，返回栈顶的数据项，栈被修改
    peek(): “窥视”栈顶数据项，返回栈顶的数据项但不移除，栈不被修改
    isEmpty(): 返回栈是否为空栈
    size(): 返回栈中有多少个数据项
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# 栈顶首端实现，其 push/pop 的复杂度为 O(n)
class Stack0:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    m = Stack()
    m.push('x')
    m.push('y')
    #print(m.pop())
    m.push('z')
    while not m.isEmpty():
        m.pop()
        m.pop()

    print(m.peek())
