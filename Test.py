class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_end(self, data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        
        node = Node(data,None)
        itr = self.head
        while itr:
            itr = itr.next
        itr.next = node
    def insert_big(self,data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_middle(self,idx,data):
        count = 0
        itr = self.head
        while itr:
            if count == idx-1:
                node = Node(data,itr.next)
                itr.next = node
            itr = itr.next
            count+=1

    def remove_middle(self,idx,data):
        count = 0
        if idx == 0:
            self.head = Node(data,self.head)
            return
        itr = self.head
        while itr:
            if count == idx-1:
                node = Node(data,itr.next.next)
                itr.next = node
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

        
