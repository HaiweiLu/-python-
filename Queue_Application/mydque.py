class Deque:
    '''
    1. 采用 python List 保存数据项
    2. List 首端作为 deque 的尾端
    3. List 末端作为 deque 的首端
    4. addFront/removeFront O(1)
    5. addRear/removeRear O(n)
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)