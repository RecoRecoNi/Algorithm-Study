import sys
from collections import deque

input = sys.stdin.readline

class Deque:
    """
    Deque wrapper class for BOJ 10866
    """
    def __init__(self) -> None:
        """
        생성자 : deque 인스턴스 생성
        """
        self.deque = deque()
    
    def size(self) -> None:
        """
        size: 덱에 들어있는 정수의 개수를 출력한다.
        """
        print(len(self.deque))
    
    def empty(self) -> None:
        """
        empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
        """
        print(1) if len(self.deque)==0 else print(0)

    def empty_check(self) -> bool:
        """
        임의 메서드 : 덱이 비어있으면 1을, 아니면 0을 반환 한다.
        """
        return True if len(self.deque)==0 else False
    
    def push_front(self, x: int) -> None:
        """
        push_front X: 정수 X를 덱의 앞에 넣는다.
        """
        self.deque.appendleft(x)

    def push_back(self, x: int) -> None:
        """
        push_back X: 정수 X를 덱의 뒤에 넣는다.
        """
        self.deque.append(x)

    def pop_front(self) -> None:
        """
        pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
        만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        print(self.deque.popleft()) if not self.empty_check() else print(-1)

    def pop_back(self) -> None:
        """
        pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 
        만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        print(self.deque.pop()) if not self.empty_check() else print(-1)

    def front(self) -> None:
        """
        front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        print(self.deque[0]) if not self.empty_check() else print(-1)

    def back(self) -> None:
        """
        back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        """
        print(self.deque[-1]) if not self.empty_check() else print(-1)

def main():
    덱 = Deque()

    for _ in range(int(input())):
        ops = input().rstrip().split()

        if len(ops) == 2:
            eval(f"덱.{ops[0]}({ops[1]})")      # eval : 문자열을 코드라인으로 변환
        else:
            eval(f"덱.{ops[0]}()")
        
if __name__ == '__main__':
    main()