from pythonds.basic.queue import Queue

'''
1. 用队列来实现热土豆问题的算法，
参加游戏的人名列表，以及传递次数 num，
算法返回最后剩下的人名
2. 模拟程序采用队列来存放所有参加游戏的人名，
按照传递土豆的方式从队头排到队尾，游戏开始时持有土豆的人在队首
3. 模拟游戏开始，只需要将队首的人出队，再回到队尾，
算是一次传递，这时土豆就在队首的人手里
4. 传递了 num 次后，将队首的人移除，不再入队
5. 如此反复，直到队中剩余一人
'''
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        print(simqueue.dequeue())

    return simqueue.dequeue()

if __name__ == "__main__":
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 7))