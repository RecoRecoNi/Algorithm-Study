'''
21:50 -> 22:00

명령의 수가 10000까지 주어질 수 있으므로 O(N)안에서 해결해야 할듯!

덱을 쓰려다 심심해서 Queue 클래스를 정의해보았습니다!
`48ms` 나왔는데 예전에 deque으로 문제 풀이한 기록 보니 `72ms`이네요. 이게 type hint의 힘..?
'''
import sys
input = sys.stdin.readline

class Queue:
    ''' 
    First-in-First-out(FIFO) 방식의 자료구조
    Python의 list를 활용해 Class 정의
    '''
    def __init__(self) -> None:
        '''
        python list 활용
        '''
        self.lst = list()

    def push(self, X : int) -> None:
        '''
        push X: 정수 X를 큐에 넣는 연산이다.
        '''
        self.lst.append(X)

    def pop(self) -> int:
        '''
        pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        '''
        return self.lst.pop(0) if self.lst else -1

    def size(self) -> int:
        '''
        size: 큐에 들어있는 정수의 개수를 출력한다.
        '''
        return len(self.lst)

    def empty(self) -> int:
        '''
        empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        '''
        return 1 if not self.lst else 0

    def front(self) -> int:
        '''
        front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        '''
        return self.lst[0] if self.lst else -1

    def back(self) -> int:
        '''
        back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        '''
        return self.lst[-1] if self.lst else -1

def main():
    N = int(input())
    queue = Queue()
    for _ in range(N):
        command = input().split()
        if command[0] == 'push':
            queue.push(int(command[1]))
        elif command[0] == 'front':
            print(queue.front())
        elif command[0] == 'back':
            print(queue.back())
        elif command[0] == 'size':
            print(queue.size())
        elif command[0] == 'empty':
            print(queue.empty())
        elif command[0] == 'pop':
            print(queue.pop())

if __name__ == '__main__':
    main()