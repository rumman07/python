class Node:

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node 

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.__count = 0 

    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self.__count 
    
    def add(self, data):
        new_head = Node(data, next_node = self.head)
        self.head = new_head
        self.__count += 1

    def search(self, key):

        current = self.head

        while current: 
            if current.data == key:
                return current
            else: 
                current = current.next_node
        return None
    
    def insert(self, data, index):

        if index >= self.__count:
            raise IndexError('index out of range')
        
        if index == 0:
            self.add(data)
            return 
        
        if index > 0: 
            new = Node(data)
            position = index
            current = self.head 

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node
        self.__count += 1

    def node_at_index(self, index):
        if index >= self.__count:
            raise IndexError('index out of range')
        
        if index == 0:
            return self.head
        
        current = self.head 
        position = 0 

        while position < index:
            current = current.next_node
            position += 1
        
        return current

    def remove(self, key):

        current = self.head
        previous = None 
        found = False 

        while current and not found: 
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
                self.__count -= 1 
                return current 
            elif current.data == key:
                found = True 
                previous.next_node = current.next_node 
                self.__count -= 1
                return current 
            else:
                previous = current
                current = current.next_node 
        return None    
    
    def remove_at_index(self, index):
        
        if index >= self.__count: 
            raise IndexError("Index out of range")

        current = self.head 

        if index == 0:
            self.head = current.next_node
            self.__count -= 1
            return current 

        position = index 

        while position > 1: 
            current = current.next_node
            position -= 1

        prev_node = current 
        current = current.next_node
        next_node = current.next_node 

        prev_node.next_node = next_node
        self.__count -= 1

        return current 

    def __iter__(self):
        current = self.head 

        while current: 
            yield current 
            current = current.next_node

    def __repr__(self): 

        nodes = []
        current = self.head 
        while current: 
            if current is self.head: 
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None: 
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return "->".join(nodes)
     





