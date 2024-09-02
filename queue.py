class Queue:
    def __init__(self) -> None:
        self.data = []

    def enqueue(self, val) -> None:
        self.data.append(val)

    def empty(self) -> bool:
        return self.data == []

    def dequeue(self) -> int:
        if not Queue.empty(self):
            return self.data.pop(0)

        print('\ndequeue(): empty queue error')

    def size(self) -> int:
        return len(self.data)

    def print_queue(self) -> None:
        print('\nQueue: ', end = '')

        for value in self.data:
            print(f'{value} ', end = '')
        
        print('\n')

    def peek_tail(self) -> None:
        if not Queue.empty(self):
            print(f'Tail: {self.data[Queue.size(self) - 1]}')

            return

        print('\npeek_tail(): empty queue error')

    def peek_head(self) -> None:
        if not Queue.empty(self):
            print(f'Head: {self.data[0]}')

            return

        print('\npeek_head(): empty queue error')