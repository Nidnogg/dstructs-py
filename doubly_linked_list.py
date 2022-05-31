from linked_list import LinkedList
class DoublyLinkedList(LinkedList):
    """Implements find() method from LinkedList, with small changes to the rest. 
    Previous node pointers cause a larger memory overhead than what a linked list would have.
    """
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Node(data=elem)
                node.next.previous = node
                node = node.next

    def prepend(self, node):
        """Inserts element at start of list 
        """
        node.next = self.head
        self.head = node

    def append(self, node):
        """Inserts element at end of list (before None pointer)
        """
        if(self.head is None):
            self.head = node
            return 

        for cur_node in self:
            pass
        
        node.previous = cur_node
        cur_node.next = node

    def insert_append(self, node, node_to_append):
        """Inserts node element after node with node_to_append data
        """
        if(self.head is None):
            raise Exception("List is empty!")

        for cur_node in self:
            if cur_node.data == node_to_append:
                node.next = cur_node.next
                node.previous = cur_node
                cur_node.next = node
                return

        raise Exception("Couldn't find Node with {} data.".format(node_to_append))

    def insert_prepend(self, node, node_to_prepend):
        """Inserts element before node with node_to_prepend data
        """
        if(self.head is None):
            raise Exception("List is empty!")

        if(self.head.data is node_to_prepend):
            self.prepend(node)
            return

        for cur_node in self:
            if cur_node.next.data == node_to_prepend:
                node.next = cur_node.next
                node.previous = cur_node
                cur_node.next = node
                return
        raise Exception("Couldn't find Node with {} data.".format(node_to_prepend))
                
    def remove(self, node_to_remove):
        """Removes element with node_val data
        """
        if(self.head is None):
            raise Exception("Cannot remove from empty linked list")
        
        if(self.head.data == node_to_remove):
            self.head = self.head.next
            return

        next_node = self.head
        for cur_node in self:
            next_node = cur_node.next
            if(next_node.data == node_to_remove):
                node_after_deleted_node = next_node.next
                node_after_deleted_node.previous = cur_node
                cur_node.next = node_after_deleted_node
                next_node = None
                return 
            
        raise Exception("Couldn't find Node with \"{}\" data.".format(node_to_remove))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data

llist = DoublyLinkedList(["a", "b", "c"])
