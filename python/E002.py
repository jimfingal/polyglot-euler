from collections import deque

def even_fib_gen(max_value):
    
    fib_memo = deque([1, 1])
    next_fib = 2
    
    while next_fib < max_value:
        next_fib = sum(fib_memo)
        fib_memo.popleft()
        fib_memo.append(next_fib)
        if next_fib % 2 == 0:
            yield next_fib


def solution():
    return sum(even_fib_gen(4000000))