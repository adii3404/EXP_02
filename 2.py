class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            
    def insert(self, new_node, pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            p = 1
            while p != pos - 1 and temp.next is not None:
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node
            return
            
    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            print("Middle node:", slow.data)
            
    def del_node(self, value):
        temp = self.head
        if temp is not None and temp.data == value:
            self.head = temp.next
            return
            
        prev = None
        while temp:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
            
        if temp is None:
            print("Value is not in the list")
            return
            
        prev.next = temp.next
        temp = None
        
    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev
        
    def sum(self):
        temp = self.head
        while temp and temp.next:
            total = temp.data + temp.next.data
            print(f"{temp.data} + {temp.next.data} = {total}")
            temp = temp.next # Advances by 1 for consecutive pairs
            
    def print(self):
        temp = self.head
        print("Linked list data")
        while temp:
            print(temp.data)
            temp = temp.next

# Execution
linked_list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(50)

linked_list.append(n1)
linked_list.append(n2)
linked_list.append(n3)
linked_list.append(n4)
linked_list.print()

print("\nList after insertion")
linked_list.insert(Node(100), 3)
linked_list.insert(Node(70), 4)
linked_list.print()

print("\nMiddle node:")
linked_list.middle()

linked_list.del_node(100)
print("\nLinked list after deleting 100")
linked_list.print()

print("\nReversed list")
linked_list.reverse()
linked_list.print()

print("\nSum of consecutive pairs")
linked_list.sum()
