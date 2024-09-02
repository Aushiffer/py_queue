class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.append(val)

    def empty(self):
        return self.data == []

    def dequeue(self):
        if not Queue.empty(self):
            return self.data.pop(0)

        print('\ndequeue(): empty queue error')

    def size(self):
        return len(self.data)

    def print_queue(self):
        print('\nQueue: ', end = '')

        for value in self.data:
            print(f'{value} ', end = '')
        
        print('\n')

    def peek_tail(self):
        if not Queue.empty(self):
            print(f'Tail: {self.data[Queue.size(self) - 1]}')

            return None

        print('\npeek_tail(): empty queue error')

    def peek_head(self):
        if not Queue.empty(self):
            print(f'Head: {self.data[0]}')

            return None

        print('\npeek_head(): empty queue error')
