# from collections import deque

# class Node:
#     def __int__(self):
#         self.container = deque()

#     def push(self, val):
#         self.container.append(val)

#     def pop(self):
#         return self.container.pop()

#     def peek(self):
#         return self.container[-1]

#     def is_empty(self):
#         return len(self.container) == 0
    
#     def size(self):

#         return len(self.container)

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        self.name = "lithi"
        type1 = 'bujuu'

    def push(self,value):
        self.stack.append(value)
        # print(self.name)

    def pop(self):
        print(self.name)
        # print(type1)

        return self.stack.pop()
    

s1 = Stack()

s1.push(2)
s1.push(4)
s1.push(5)
s1.pop()




    


        


        


    


    