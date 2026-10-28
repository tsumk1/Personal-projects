#The Fibonacci sequence is a series of numbers where each number is the sum of the two before it, starting with 0 and 1. 
#The sequence runs: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and continues infinitely
def fib(n):
    if n < 2: #n - індекс елемента послідовності 
        return n
    return fib(n - 1) + fib(n - 2)

print("Enter n: ")
n = int(input())
print(fib(n))
