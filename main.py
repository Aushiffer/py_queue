from queue import Queue

if __name__ == '__main__':
    opt = 0
    q = Queue()

    while opt != 7:
        q.print_queue()

        print('Select an option: ')
        print('\n1: enqueue')
        print('2: dequeue')
        print('3: size of the queue')
        print('4: is the queue empty?')
        print('5: peek head')
        print('6: peek tail')
        print('7: quit')

        opt = int(input())

        match opt:
            case 1:
                val = int(input('\nInput value to enqueue: '))

                q.enqueue(val)
            case 2:
                q.dequeue()
            case 3:
                print(f'Size: {q.size()}')
            case 4:
                print(f'Empty: {q.empty()}')
            case 5:
                q.peek_head()
            case 6:
                q.peek_tail()
