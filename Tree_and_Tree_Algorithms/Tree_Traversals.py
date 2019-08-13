from pythonds.trees import BinaryTree

# 先序遍历
def preorder(tree):
    '''
    1) 如果树(跟节点)不为空，
    2) 先访问根节点，
    3) 再访问其左子节点，
    4) 再访问其右子节点，
    5) 重复以上步骤，直至节点为空才结束
    '''
    if tree:
        print(tree.getRootVal)
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# 中序遍历
def inorder(tree):
    '''
    1) 如果树(跟节点)不为空，
    2) 先访问其左子节点，
    3) 再访问根节点，
    4) 再访问其右子节点，
    5) 重复以上步骤，直至节点为空才结束
    '''
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

# 后序遍历
def postorder(tree):
    '''
    1) 如果树(跟节点)不为空，
    2) 先访问其左子节点，
    3) 再访问其右子节点，
    4) 再访问根节点，
    5) 重复以上步骤，直至节点为空才结束
    '''
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())