class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_head(self, data):
        data = Node(data)
        if self.head is None:
            self.head = data
            self.tail = data
        else:
            data.next = self.head
            self.head = data

    def insert_tail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at(self, index, val):
        new_node = Node(val)
        if index == 0:
            self.insert_head(val)
        else:

            current = self.head
            for i in range(index - 1):
                current = current.next
                if current is None:
                    raise Exception("Index not found")

            new_node.next = current.next
            current.next = new_node

    def delete_head(self):
        if self.is_empty():
            print("list empty")
        else:
            self.head = self.head.next
            if self.head is None:
                self.tail = None



    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

            
linked_list = SinglyLinkedList()
linked_list.insert_head(10)
linked_list.delete_head()
linked_list.insert_tail(52)

# linked_list.insert_head(5)
# linked_list.insert_head(10)
# linked_list.insert_at(3,20)
# print(linked_list.head.next)

linked_list.display()