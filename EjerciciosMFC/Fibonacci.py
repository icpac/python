from typing import Dict
#https://www.manning.com/books/classic-computer-science-problems-in-python?query=Classic%20Computer%20Science%20Problems%20in%20Python#toc

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
        

def CualFibonacci(n):
    print(f"El enésimo número de Fibonacci: {n} \n {fibonacci(n)}")

def CualFibo(n):
    print(f"El enésimo número de Fibonacci: {n} \n {fibo(n)}")

def CualFiboMemo(n):
    print(f"El enésimo número de Fibonacci: {n} \n {fibMemo(n)}")

if __name__ == "__main__":
    CualFiboMemo(17)