class Node:
    def __init__(self, value, nex = None):
        self.value = value
        self.next = next
    
    def delete(self):
        if self.next:
            self.next = None
    

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.head = None
        # removes the one before the node
        self.prenode = None


    def append(self, item):
        if self.length < self.capacity:
            self.length += 1
            # node points to itself
            if self.head == None:
                self.head = Node(item)
                self.head.next = self.head
            # navigate to node before the end, add a new node
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = Node(item)
                current = current.next
                current.next = self.head
                self.prenode = current
                # all spots are taken
        else:
            # next nod eremoved after node is added
            removeNext = self.prenode.next.next
            # remove node
            remove = self.prenode.next
            self.prenode.next = Node(item)
            if self.head == remove:
                self.head = self.prenode.next
            remove.delete()
            # shifting node one over before node is removed
            self.prenode = self.prenode.next
            # connect node then removeNext
            self.prenode.next = removeNext

    def get(self):
        package = []
        current = self.head
        while current.next != self.head:
            package.append(current.value)
            current = current.next
        package.append(current.value)
        return package 