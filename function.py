# 1. Greeting Function
# Write a function greet(name) that takes a name as input and prints:
# Hello, <name>! Welcome to Python.

#/def greet(name):
    #print(f"Hello, {name}, Welcome to Python")

#greet("Roshani")

# 2. Square & Cube
# Write a function power(num) that takes a number and returns its square and cube.
# (Hint: return two values)
"""
def power(num):
    square = num ** 2
    cube = num ** 3
    return square,cube
s,c = power(10)
print("Square is:",s)
print("Cube is:",c)

"""

""" 3. Maximum of Three
Write a function find_max(a, b, c) that returns the largest of the three numbers.

def find_max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(find_max(8,5,6))
"""

""" 4. Check Even or Odd
Write a function is_even(num) that returns True if the number is even, otherwise False.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
print(is_even(7))
"""

""" 5. Sum of List
Write a function sum_list(numbers) that takes a list of numbers and returns their sum.
(Don’t use sum() built-in for this one — use a loop.)


def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(sum_list([5,8,9,7,6,5]))
"""
"""  Factorial
Write a function factorial(n) that returns the factorial of a number (e.g., 5! = 5×4×3×2×1).


def factorial(n):
    total = 0
    for i in range(1, 1+n):
        total += i
    return total

print(factorial(5))

"""

""" 7. Palindrome Check
Write a function is_palindrome(word) that checks if a given word is the same forwards and backwards.
(Example: "madam" → True)


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome("madam"))
"""