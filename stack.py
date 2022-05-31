from node import Node

class Stack(): 
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
            nodes.append(str(node.data))
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head  

        while node is not None:
            yield node
            node = node.next
    
    def push(self, node_to_push):
        node_to_push.next = self.head
        self.head = node_to_push

    def pop(self):
        if(self.head == None):
            raise Exception("Cannot pop empty stack!")
        node_to_pop = self.head
        self.head = node_to_pop.next
        return(node_to_pop)
        
stk = Stack(["a", "b", "c"])

         



