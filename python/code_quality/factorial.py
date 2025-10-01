def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

#Get number
number = int(input())

# print factorial
print(factorial(number))
