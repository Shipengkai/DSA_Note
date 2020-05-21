"""
二叉查找树（BST）：任意子树满足——左子树元素<根节点<右子树元素
so 插入顺序不同，树不一样

二叉查找树是为了实现动态查找而设计的数据结构，它是面向查找操作的，在二叉排序树中查找一个结点的平均时间复杂度是O(log n)；
堆是为了实现排序而设计的一种数据结构，它不是面向查找操作的。
"""


class Node():
    def __init__(self, key, val, lchild=None, rchild=None, parent=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild

    def hasLeftChild(self):
        return self.lchild

    def hasRightChild(self):
        return self.rchild

    def isLeftChild(self):
        return self.parent and self.parent.lchild == self

    def isRightChild(self):
        return self.parent and self.parent.rchild == self

    # 中序遍历
    def __iter__(self):
        if self is not None:
            if self.hasLeftChild():
                for elem in self.lchild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rchild:
                    yield elem

    def isRoot(self):
        return self.parent == None

    def isLeaf(self):
        return self.lchild == None and self.rchild == None

    def hasAnyChild(self):
        return not self.isLeaf()

    def hasBothChild(self):
        return self.lchild and self.rchild

    # 修改了本node的key, val, lchild, rchild; 本node的parent不变
    def replaceNodeData(self, key, val, lchild, rchild):
        self.key = key
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
        if self.lchild is not None:
            self.lchild.parent = self
        if self.rchild is not None:
            self.rchild.parent = self


class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, val):
        self.put(key, val)

    def put(self, key, val):
        if self.root == None:
            node = Node(key, val)
            self.root = node
        else:
            self._put(key, val, self.root)

    def _put(self, key, val, root):
        node = Node(key, val)
        cur = root
        while True:
            if key < cur.key:
                if cur.lchild == None:
                    cur.lchild = node
                    self.size += 1
                    return
                cur = cur.lchild
            elif key == cur.key:
                cur.val = val
                return
            elif key > cur.key:
                if cur.rchild == None:
                    cur.rchild = node
                    self.size += 1
                    return
                cur = cur.rchild

    # 按层遍历，打印每个node的item
    def travel(self):
        print('Start Travel... the tree is')
        queue = [self.root]
        while queue[0] is not None:
            cur = queue.pop(0)
            print(cur.key, end=' ')
            queue.append(cur.lchild)
            queue.append(cur.rchild)
        print('')
        print('Travel Finished')

    def get(self, key):
        if self.root is None:
            return 'empty tree'
        cur = self.root
        while cur:
            if cur.key == key:
                return cur.val
            if cur.key > key:
                cur = cur.lchild
            else:
                cur = cur.rchild
        return 'do not have this key'

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key) != None:
            return True
        else:
            return False


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst[1] = 'one'
    bst[0] = 'zero'
    bst[-1] = '-one'
    bst[2] = 'two'
    bst.travel()

    for key in bst:
        print(key, bst[key])
