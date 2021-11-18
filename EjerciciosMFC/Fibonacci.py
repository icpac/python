from typing import Dict
from functools import lru_cache
from typing import Generator
#https://www.manning.com/books/classic-computer-science-problems-in-python?query=Classic%20Computer%20Science%20Problems%20in%20Python#toc

#Algorithms, 4th Edition, by Robert Sedgewick and Kevin Wayne (Addison-Wesley Professional, 2011)
#https://algs4.cs.princeton.edu/home/


def fibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

def fibo(n: int) -> int:
    if n < 2:  # base case
        return n
    return fibo(n-1) + fibo(n-2)



Memo: Dict[int, int] = {0:0, 1:1} # casos base
def fibMemo(n:int)->int:
    if n not in Memo:
        Memo[n] = fibMemo(n-1)+fibMemo(n-2) #memoization
    return Memo[n]
        
@lru_cache(maxsize=None)
def fib4(n: int) -> int:  # same definition as fib2()
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursive case

def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0: yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step

def CualFibonacci(n):
    print(f"El enésimo número de Fibonacci: {n} \n {fibonacci(n)}")

def CualFibo(n):
    print(f"El enésimo número de Fibonacci: {n} \n {fibo(n)}")

def CualFiboMemo(n):
    print(f"El enésimo número de Fibonacci: {n} \n {fibMemo(n)}")

if __name__ == "__main__":
    CualFiboMemo(17)
    print(fib4(5))
    print(fib4(17)) #50))
    print(fib5(5))
    print(fib5(50))

    for i in fib6(50):
        print(i)
