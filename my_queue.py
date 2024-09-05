class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, val):
        new_node = Node()
        new_node.data = val

        if self.empty():
            self.tail = new_node
            self.head = new_node
            self.size += 1

            return None

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.empty():
            print('\ndequeue(): empty queue\n')

            return None
            
        return_val = self.head.data
        node_rm = self.head
        self.head = self.head.next
        self.size -= 1

        del node_rm
        return return_val
        
    def empty(self):
        return self.head == None

    def get_size(self):
        return self.size

    def peek_head(self):
        if self.empty():
            print('\npeek_head(): empty queue\n')

            return None

        return self.head.data

    def peek_tail(self):
        if self.empty():
            print('\npeek_tail(): empty queue\n')

            return None

        return self.tail.data

    def print_queue(self):
        if self.empty():
            return None

        aux_node = self.head

        while aux_node != None:
            print(f'{aux_node.data} -> ', end='')

            aux_node = aux_node.next

        print('NULL')