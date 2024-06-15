class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    # Points toward the head of a linked list
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Empty list")
            return
        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        # if it's not blank then iterate to the end and insert a value
        itr=self.head
        while itr.next:
            itr = itr.next
        itr.next =Node(data,None)




ll = LinkedList()
ll.insert_at_beginning(89)
ll.insert_at_beginning(123)
ll.insert_at_end(12)
ll.insert_at_end(123)
ll.print()  # This will print the elements of the linked list
