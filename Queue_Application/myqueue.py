class Queue:
    '''
    1. 采用 python List 来容纳 Queue 的数据项
    2. 将 List 的首端作为队列尾端，enqueue() 复杂度为 O(n)
    3. List 的尾端作为队列首端，dequeue() 复杂度为 O(1)
    4. 2, 3 倒过来也可以，倒过来实现，复杂度也倒过来
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)