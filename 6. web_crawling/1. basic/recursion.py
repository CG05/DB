# 1 * 2 * 3 * 4 * 5
# def factorial(n):
#     if n == 0:
#         return 1
#     else :
#         return n * factorial(n - 1)
    
# print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))