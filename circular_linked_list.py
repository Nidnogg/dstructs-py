from linked_list import LinkedList

class CircularLinkedList():
    """(Note) Difference in complexity between List and Linked-List:
    Python lists are implemented in a way that elements inserted onto the end of the list take up O(1) complexity, whereas elements inserted 
    near the start of the list take up O(n) time.

    Linked-lists, however, take up O(1) time for append/insert.
    """
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
                
            print("final node  {}".format(node.data))
            node.next = self.head

    def __repr__(self):
        node = self.head
        nodes = []

        for node in self.traverse():
            nodes.append(str(node.data))
            node = node.next

        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        starting_node = self.head  

        while node is not starting_node:
            yield node
            node = node.next

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point

        while node is not None and (node.next != starting_point):
            yield node
            node = node.next

        yield node

    def print_list(self, starting_point=None):
        nodes = []

        for node in self.traverse(starting_point):
            nodes.append(str(node))
            
        print(" -> ".join(nodes))

    def find(self, node_to_find):
        if(self.head.data == node_to_find):
            return self.head
                
        for cur_node in self.traverse():
            if cur_node.data == node_to_find:
                return cur_node
        
        raise Exception("Couldn't find Node with {} data.".format(node_to_find))


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

        cur_node.next = node

    def insert_append(self, node, node_to_append):
        """Inserts node element after node with node_to_append data
        """
        if(self.head is None):
            raise Exception("List is empty!")

        for cur_node in self:
            if cur_node.data == node_to_append:
                node.next = cur_node.next
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
                cur_node.next = next_node.next
                next_node = None
                return 
            
        raise Exception("Couldn't find Node with \"{}\" data.".format(node_to_remove))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

llist = CircularLinkedList(["a", "b", "c"])

llist.print_list(llist.find("a"))


