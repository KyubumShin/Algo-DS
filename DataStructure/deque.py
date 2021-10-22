class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class Deque:
    def __init__(self):
        dummy = Node(None)
        self.head = dummy
        self.tail = dummy
        self.tail.prev = self.head
        self.head.next = self.tail
        self._count = 0

    def appendleft(self, data):
        assert data
        node = Node(data)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self._count += 1

    def append(self, data):
        assert data
        node = Node(data)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self._count += 1

    def count(self):
        return self._count

    def popleft(self):
        ret = self.head.next
        if ret == self.tail:
            raise IndexError
        self.head.next = ret.next
        ret.next.prev = self.head.next
        self._count -= 1
        return ret.data

    def pop(self):
        ret = self.tail.next
        if ret == self.head:
            raise IndexError
        self.tail.next = ret.next
        ret.next.prev = self.tail.next
        self._count -= 1
        return ret.data

    def __repr__(self):
        temp = []
        node = self.head.next
        for _ in range(self._count):
            temp.append(node.data)
            node = node.next
        return str(temp)

    def __add__(self, other):
        p_node = self.tail.prev
        n_node = other.head.next
        p_node.next = n_node
        n_node.prev = p_node
        self.tail = other.tail
        self._count += other.count()
        return self


if __name__ == "__main__":
    deque = Deque()
    deque.append(5)
    deque.append(5)
    deque.appendleft(3)
    print(deque.count())
    deque.append(5)
    deque.append(5)
    a = deque.pop()
    print(deque.count())
    b = deque.popleft()
    print(a, b)
    print(deque)
    deque2 = Deque()
    deque2.append(10)
    deque2.appendleft(7)
    print(deque2)
    n_deque = deque + deque2
    print(n_deque)
