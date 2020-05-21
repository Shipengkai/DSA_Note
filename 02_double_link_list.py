class Node():
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoubleLinkList():
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
        count = 0
        while cur != None:
            print(f"Node{count}: {cur.item}")
            cur = cur.next
            count += 1

    def add(self, item):
        node = Node(item)
        if self._head == None:
            self._head = node
        else:
            node.next = self._head
            self._head = node

    def append(self, item):
        node = Node(item)
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        length = self.length()
        if pos > length:
            print('No such positon!')
            return 0
        node = Node(item)
        if self._head == None:
            self._head = node
        elif pos == 0:
            node.next = self._head
            self._head.prev = node
            self._head = node
        elif pos == length:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
        else:
            cur = self._head
            count = 1
            while count != pos:
                cur = cur.next
                count += 1
            cur.next.prev = node
            node.next = cur.next
            cur.next = node
            node.prev = cur

    def remove(self, item):
        cur = self._head
        while self._head.item == item:
            self._head = self._head.next
        while cur.next != None:
            if cur.next.item == item:
                if cur.next.next == None:
                    cur.next = None
                    break
                else:
                    cur.next.next.prev = cur
                    cur.next = cur.next.next
            if cur.next.item != item:
                cur = cur.next


dll = DoubleLinkList()
dll.insert(3, 1)
dll.insert(0, 'a')
dll.insert(1, 'd')
dll.insert(1, 'k')
dll.add(100)
dll.add(100)
dll.add(100)
dll.add(100)
dll.add(100)
dll.append(10)
dll.insert(0, 'b')
dll.insert(1, 'c')
dll.append(10)
dll.append(100)
dll.append(100)
dll.remove(100)

dll.travel()
