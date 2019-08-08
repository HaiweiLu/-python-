from pythonds.basic import Stack
from pythonds.trees import BinaryTree

# 将表达式解析为一颗二叉树
def bulidParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == fplist:
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

    return eTree

# 利用表达式树求值
import operator
def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, \
        '*':operator.mul, '/':operator.truediv}

    # 减小规模，先算左子树，再算右子树
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

if __name__ == '__main__':
    pt = bulidParseTree('( ( 10 + 7 ) * 2 )')
    result = evaluate(pt)
    print(result)