from node import Node

class Queue(): 
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
    
    def enqueue(self, node_to_push):
        node_to_push.next = self.head
        self.head = node_to_push

    def dequeue(self):
        if(self.head == None):
            raise Exception("Cannot dequeue empty queue!")
        for cur_node in self:
            next_node = cur_node.next
            if(next_node.next == None):
                cur_node.next = None
                return next_node
        
que = Queue(["a", "b", "c"])

         



