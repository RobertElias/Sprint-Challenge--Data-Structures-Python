class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head == None:
            return
        elif node.next_node:
            self.reverse_list(node.next_node, node)
            node.next_node = prev
            return
        else:
            self.head = node
            node.next_node = prev
            return

    # print some values
    def showValues(self):
        current = self.head
        while True:
            print(current.value)
            if current.next_node == None:
                print("End of values")
                break
            if current == current.next_node:
                print("This is a tail")
                break
            current = current.next_node

# testing the values
#         tail = None
# list = LinkedList()
# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# list.add_to_head(4)
# list.add_to_head(5)
# list.showValues()
# list.reverse_list(list.head, None)
# list.showValues()