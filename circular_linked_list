from node import Node
class Clinkedlist:
    def __init__(self, head=None):
        self.head = head

    def insert_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            c = self.head
            while c.next != self.head:
                c = c.next
            c.next = newnode
            newnode.next = self.head
    def insert_start(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = newnode
        newnode.next = self.head
        self.head = newnode
    def insert_after(self,data,target):
        if self.head is None:
            raise Exception('List is empty')
        newnode = Node(data)
        c = self.head
        while True:
            if c.data == target:
                newnode.next = c.next
                c.next = newnode
                return
            c = c.next
            if c == self.head:
                break
        print(f"Target value {target} not found in the list")
    def del_node(self,key):
        if self.head is None:
            raise Exception('list is empty')
        c = self.head
        prev = None
        while True:
            if c.data == key:
                if prev:
                    prev.next = c.next
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    if temp == self.head:
                        self.head = None
                        return True
                    temp.next = self.head.next
                    self.head = self.head.next
                return True
            prev = c
            c = c.next
            if c == self.head:
                break
        print(f"Key {key} not found in the list")
        return False
    def search(self,key):
        if self.head is None:
            raise Exception('List is empty')
        c = self.head
        while True:
            if c.data == key:
                return True
            c = c.next
            if c == self.head:
                break
        return False
    def clear(self):
        self.head = None
    def count_node(self):
        if self.head is None:
            return 0
        count = 0
        c = self.head
        while True:
            count += 1
            c = c.next
            if c == self.head:
                break
        return count
    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        result = []
        while True:
            result.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(result) + " -> (back to head)")

    def reverse(self):
        if not self.head or self.head.next == self.head:
            return
        prev = None
        c = self.head
        head_ref = self.head
        while True:
            node_next = c.next
            c.next = prev
            prev = c
            c = node_next
            if c == head_ref:
                break
        head_ref.next = prev
        self.head = prev
