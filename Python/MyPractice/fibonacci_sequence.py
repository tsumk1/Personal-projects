#The Fibonacci sequence is a series of numbers where each number is the sum of the two before it, starting with 0 and 1. 
#The sequence runs: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and continues infinitely
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ") # а тут н як кількість цифр а не індекс
        a, b= b, a+b
n = int(input())
print(fib(n))
    
