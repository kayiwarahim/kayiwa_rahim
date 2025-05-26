def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        result = n * factorial(n-1)
        return result
    
print("The factorial of five is:",factorial(5))