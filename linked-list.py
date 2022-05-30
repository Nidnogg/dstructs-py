class LinkedList:
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

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head        
        while node is not None:
            yield node
            node = node.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

llist = LinkedList(["a", "b", "c"])

# node1 = Node("a")
# node2 = Node("b")
# node1.next = node2
# llist.head = node1

print(llist)
