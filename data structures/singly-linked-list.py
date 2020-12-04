class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self, headData=None):
        self.__head = Node(headData) if headData else None
        self.__tail = None
        self.__size = 0

    def head(self):
        return self.__head

    def tail(self):
        return self.__tail

    def prepend(self, data):
        node = Node(data, self.__head)

        if self.isEmpty():
            self.__tail = node

        self.__head = node
        self.__size += 1

    def append(self, data):
        node = Node(data)

        if self.isEmpty():
            self.__head = self.__tail = node
        else:
            self.__tail.nextNode = node  # update link of the current tail
            self.__tail = node  # update class property to be the new node

        self.__size += 1

    def popFirst(self):
        if self.isEmpty():
            return None

        currentHead = self.__head
        self.__head = currentHead.nextNode

        self.__size -= 1

        if self.__size == 0:
            self.__tail = None

        return currentHead

    def pop(self):
        if self.isEmpty():
            return None

        # single node
        if not self.__head.nextNode:
            head = self.__head
            self.clear()
            return head

        # traverse til the second-last node
        prev = None
        current = self.__head
        while current.nextNode:
            prev = current
            current = current.nextNode

        # swap tail with prev
        tail = prev.nextNode
        prev.nextNode = None
        self.__tail = prev
        self.__size -= 1

        return tail

    def remove(self, key):
        if self.isEmpty():  # empty list
            return

        if self.__head.data == key:  # head is the target
            self.clear()

        current = self.__head
        while current and current.nextNode:
            if current.nextNode.data == key:
                current.nextNode = current.nextNode.nextNode  # skip next node
                return

            current = current.nextNode

    def reverse(self):
        # None --> (a) --> (b) --> (c) --> None
        prev = None
        current = self.__head

        # switch head & tail properties
        self.__head = self.__tail
        self.__tail = current

        # reverse links
        while current:
            nextNode = current.nextNode  # copy next node
            current.nextNode = prev  # current point to prev (actual reversing)
            prev = current  # update prev with current (for coming iterations)
            current = nextNode  # advance pointer

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def isEmpty(self):
        return not self.__head or self.__size == 0

    def __len__(self):
        return self.__size

    def __str__(self):
        currentNode = self.__head
        result = 'head: ' + str(self.__head)
        result += ', tail: ' + str(self.__tail)
        result += ', size: ' + str(self.__size) + '   |   '

        while currentNode:
            result += str(currentNode.data)
            currentNode = currentNode.nextNode  # advance pointer

            if currentNode:
                result += " --> "

        return result


if __name__ == "__main__":
    mylist = SinglyLinkedList()

    mylist.append(4)
    mylist.prepend(0)
    mylist.append(1)
    mylist.append(9)
    mylist.prepend(3)
    print(mylist)

    mylist.remove(1)
    print(mylist)

    mylist.popFirst()
    mylist.pop()
    print(mylist)
