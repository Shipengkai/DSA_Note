"""
继二叉查找树BST，给每一个node增加一个attribute —— balance factor = 左右子树高度差
二叉查找树每个node的balance factor 都在 -1、0、1 之中，称之为平衡树

重点：重新平衡
    新node插入时：
    左子节点插入，父节点+1，反之-1
    接下来考虑影响的传递，
    子树root从 0 变 1、-1 时，子树高度 +1，反之不变
    左子树root如上变化，父节点bf+1，反之-1
"""
# 调用BStree.py的两个类
from BStree import Node, BinarySearchTree


# 子类，添加balance factor
class AVLnode(Node):
    def __init__(self, key, val, lchild, rchild, parent, bf):
        Node.__init__(self, key, val, lchild, rchild, parent)
        self.bf = 0


# 子类，重写_put方法
class AVLtree(BinarySearchTree):
    def _put(self, key, val, root):
        node = Node(key, val)
        cur = root
        while True:
            if key < cur.key:
                if cur.lchild == None:
                    cur.lchild = node
                    self.size += 1
                    self.updateBalance(cur.lchild)
                    return
                cur = cur.lchild
            elif key == cur.key:
                cur.val = val
                return
            elif key > cur.key:
                if cur.rchild == None:
                    cur.rchild = node
                    self.size += 1
                    self.updateBalance(cur.rchild)
                    return
                cur = cur.rchild

    def updateBalance(self, node):
        # 递归, node bf变点
        if node.bf > 1 or node.bf < 1:
            self.rebalance(node)
            return

        if node.parent is not None:
            if node.isLeftChild():
                node.parent.bf += 1
            else:
                node.parent.bf -= 1

        if node.parent.bf != 0:
            self.updateBalance(node.parent)

    def rebalance(self, node):
        pass
# https://www.icourse163.org/learn/PKU-1206307812?tid=1450242471#/learn/content?type=detail&id=1214420567&cid=1218119425
