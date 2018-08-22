# encoding: utf-8

class Node(object):

    def __init__(self,data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


class SingleLinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def insert(self, data, index):
        if index < 0 or index > self.length:
            raise Exception("Out of length")
        if self.head == None or index == 0:
            newNode = Node(data)
            self.head = newNode
            self.length += 1
        else:
            cureentNode = self.head
            for i in range(index-1):
                cureentNode = cureentNode.next
            if cureentNode == None:
                raise Exception("Wrong insert location")
            else:
                newNode = Node(data)
                newNode.next = cureentNode.next
                cureentNode.next = newNode
                self.length += 1
        return True

    def append(self, data):
        return self.insert(data,self.length)

    def getItem(self, index):
        if self.isEmpty():
            raise Exception("The link list is empty")
        if index < 0 or index > self.length:
            raise Exception("Out of length")
        cureentNode = self.head
        for i in range(index):
            cureentNode = cureentNode.next
        return cureentNode.data

    def delete(self, index):
        if self.isEmpty():
            raise Exception("The link list is empty")
        if index < 0 or index > self.length:
            raise Exception("Out of length")

        if index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            cureentNode = self.head
            for i in range(index-1):
                cureentNode = cureentNode.next
            deleteNode = cureentNode.next
            nextNode = deleteNode.next
            cureentNode.next = nextNode
            self.length -= 1
        return True

    def update(self, data, index):
        if self.isEmpty():
            raise Exception("The link list is empty")
        if index < 0 or index > self.length:
            raise Exception("Out of length")

        cureentNode = self.head
        for i in range(index):
            cureentNode = cureentNode.next
        cureentNode.data = data

        return True

    def clear(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            print("The link list is empty")
        else:
            currentNode = self.head
            res = ""
            while currentNode != None:
                res += str(currentNode.data) + " "
                currentNode = currentNode.next
        return res




if __name__ == "__main__":
    linklist = SingleLinkList()
    print(linklist.isEmpty())
    print(linklist.append(11))
    print(linklist.insert(22, 1))
    print(linklist.length)

    print(linklist.update(12,0))
    print(linklist.getItem(0))
    print(linklist)




