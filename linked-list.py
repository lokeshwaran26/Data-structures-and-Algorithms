class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_big(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        node = Node(data, None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def remove_middle(self, index):
        if index < 0:
            raise Exception('Invalid syntax!')
        if index == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def add_middle(self,index, data):
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next  = node 
                break

            itr = itr.next
            count+=1


    def print(self):
        if self.head is None:
            print('It is empty linked list!')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


a = LinkedList()
a.insert_big(6)
a.insert_big(23)
a.insert_big(11)
a.insert_end(22)
a.insert_big(35)
a.remove_middle(3)
a.print()
