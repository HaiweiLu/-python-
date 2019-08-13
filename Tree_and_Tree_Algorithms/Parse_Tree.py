from pythonds.basic import Stack
from pythonds.trees import BinaryTree

# 将表达式解析为一颗二叉树
def bulidParseTree(fpexp):
    '''
    思路————
    1. 首先，把全括号表达式 fpexp(有空格相间)拆分为单词 fplist 列表
    其中单词分为括号 "()"、操作符 "+-*/" 和操作数 "0~9" 
    左括号就代表表达式开始，右括号是表达式的结束(即表达式最外层有一括号)

    2. 从左到右扫描全括号表达式的每一个单词，依据规则建立解析树
    1) 如果当前单词是 "(": 为当前节点添加一个新节点作为其左子节点，
    当前节点下降，设这个节点为新节点
    2) 如果当前单词是操作符 ['+','-','*','/']: 将当前节点的值设为此符号，
    为当前节点添加一个新节点作为其右子节点，当前节点下降，设这个为新节点 
    3) 如果当前单词是操作数：将当前节点的值设为此数，当前节点上升返回到父节点
    4) 如果当前单词是 ")": 则当前节点上升返回到父节点

    其中，
    当前节点创建左右子树，可以调用 BinaryTree.insertLeft/Right
    当前节点设置值，可以调用 BinaryTree.setRootVal
    当前节点下降到左右子树，可以调用 BinaryTree.getLeft/RightChild
    但是，当前节点上升到父节点，这个没办法支持！

    不妨使用一个栈来记录跟踪父节点
    当前节点下降时，将下降前的节点 push 入栈
    当前节点需要上升到父节点时，上升到 pop 出栈的节点即可
    '''
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

# 利用表达式树求值
import operator
def evaluate(parseTree):
    '''
    思路————
    1. 由于 BinaryTree 是一个递归数据结构，自然地，
    可以使用递归算法来处理 BinaryTree，
    由于表达式树的叶子节点是最先操作的，可以从树的底层子树开始，
    逐步向上层求值，最终得到整个表达式树的值
    
    2.求值函数 evaluate 的递归三要数:
    基本结束条件：叶子节点是最简单的子树，没有左右子节点，
    其根节点的数据项即为子表达式树的值 
    缩小规模：将表达式树分为左子树、右子树、即为缩小规模
    调用自身：分别调用 evaluate 计算左右子树的值，
    其基本操作是将左右子树的值依根节点的操作符进行计算，
    从而得到表达式的值

    引用函数 operator，增加程序的可读性
    因为 
    operator.add/sub/mul/truediv 分别为 加减乘除 四种运算
    所以，可以建立一个字典，使之与四种运算的操作符对应起来
    '''
    opers = {
        '+':operator.add, 
        '-':operator.sub, 
        '*':operator.mul, 
        '/':operator.truediv
        }

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
    pt.postorder()
    result = evaluate(pt)
    print(result)