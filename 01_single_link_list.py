class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList():
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def append(self, item):
        node = Node(item)
        if self._head == None:
            self._head = node
            return 0
        cur = self._head
        while cur.next != None:
            cur = cur.next
        cur.next = node

        # node = Node(node)
        # if self.is_empty:
        #     self._head = node
        #     return 0
        # cur = self._head
        # while True:
        #     print('a')
        #     if cur.next == None:
        #         cur.next = node
        #         return 0
        #     cur = cur.next

    def add(self, node):
        node = Node(node)
        node.next = self._head
        self._head = node

    def insert(self, pos, node):
        node = Node(node)
        if pos == 0:
            self.add(node)
            return 0
        length = self.length()
        if pos == length:
            self.append(node)
            return 0
        cur = self._head
        count = 0
        while True:
            if count == pos-1:
                node.next = cur.next
                cur.next = node
                return 0
            cur = cur.next
            count += 1

    def remove(self, node):
        node = Node(node)
        cur = self._head
        while self._head.item == node.item:
            self._head = self._head.next
        while cur.next != None:
            if cur.next.item == node.item:
                cur.next = cur.next.next
            cur = cur.next
        return 0

    def search(self, node):
        node = Node(node)
        pos = 0
        cur = self._head
        while cur != None:
            if cur.item == node.item:
                return pos
            cur = cur.next
            pos += 1
        return -1


sll = SingleLinkList()
print('is_empty:', sll.is_empty())
print('length:', sll.length())
sll.append(100)
sll.append(200)
sll.append(500)
sll.add(1)
sll.remove(1)
print('start travel:')
sll.travel()
print('length:', sll.length())
