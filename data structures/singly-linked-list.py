class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self, headData=None):
        self.head = Node(headData) if headData else None
        self.tail = None
        self.size = 0

    def pushFront(self, data):
        node = Node(data, self.head)

        if self.isEmpty():
            self.tail = node

        self.head = node
        self.size += 1

    def pushBack(self, data):
        node = Node(data)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.nextNode = node  # update link of the current tail
            self.tail = node  # update class property to be the new node

        self.size += 1

    def popFront(self):
        if self.isEmpty():
            return None

        currentHead = self.head
        self.head = currentHead.nextNode

        self.size -= 1

        if self.size == 0:
            self.tail = None

        return currentHead

    def popBack(self):
        if self.isEmpty():
            return None

        # single node
        if not self.head.nextNode:
            head = self.head
            self.clear()
            return head

        # traverse til the second-last node
        prev = None
        current = self.head
        while current.nextNode:
            prev = current
            current = current.nextNode

        # swap tail with prev
        tail = prev.nextNode
        prev.nextNode = None
        self.tail = prev
        self.size -= 1

        return tail

    def reverse(self):
        # None --> (a) --> (b) --> (c) --> None
        prev = None
        current = self.head

        # switch head & tail properties
        self.head = self.tail
        self.tail = current

        # reverse links
        while current:
            # copy current.next
            nextNode = current.nextNode

            # current point to prev (actual reversing)
            current.nextNode = prev

            # update prev with current (for coming iteration)
            prev = current

            # update current with next (advance pointer)
            current = nextNode

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def remove(self, key):
        def isTarget(curr): return curr.data == key

        current = self.head
        prev = None
        while current and not isTarget(current):
            prev = current
            current = current.nextNode

        # empty or single list
        if self.isEmpty() or (self.isHead(current) and isTarget(current)):
            self.clear()
            return

        # current will be none only if we didn't find it
        if current:
            # skip target node
            prev.nextNode = current.nextNode
            self.size -= 1

    def isEmpty(self):
        return not self.head or self.size == 0

    def isHead(self, node):
        return node == self.head

    def remove2(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.nextNode

        # Unlink it from the list
        if prev is None:
            self.head = curr.nextNode
        elif curr:
            prev.nextNode = curr.nextNode
            curr.nextNode = None

    def __str__(self):
        currentNode = self.head
        result = 'head: ' + str(self.head)
        result += ', tail: ' + str(self.tail)
        result += ', size: ' + str(self.size) + '   |   '

        while currentNode:
            result += str(currentNode.data)
            currentNode = currentNode.nextNode  # advance pointer

            if currentNode:
                result += " --> "

        return result

    def __len__(self):
        return self.size


if __name__ == "__main__":
    mylist = SinglyLinkedList()

    mylist.pushBack(4)
    mylist.pushFront(0)
    mylist.pushBack(1)
    mylist.pushBack(9)
    mylist.pushFront(3)
    print(mylist)

    mylist.remove(9)
    print(mylist)

    mylist.popFront()
    mylist.popBack()
    print(mylist)
