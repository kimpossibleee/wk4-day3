class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head  = None

    def add_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.right:
                temp = temp.right
            temp.right = new_node

    def add_list_elements(self, lst):
        for ele in lst:
            self.add_node(ele)

    def __repr__(self):
        my_linked_list = ''
        while self.head:
            my_linked_list += f'{self.head.value} --> '
            self.head = self.head.right
        my_linked_list += 'None'
        return my_linked_list
