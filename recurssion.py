## RECURRSSION FUNCTION

"""
Example 1: Factorial of a Number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
"""
"""
Example 2: Sum of Numbers (1 to n)

def sum_n(n):
    if n == 0:
        return 1
    else:
        return n+sum_n(n-1)

print(sum_n(5))
"""
"""
Example 3: Fibonacci Series


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))
"""
"""
Power of a number
Write a recursive function to calculate x^n (x raised to the power n).

def power(x, n):
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)

print(power(2, 5))
"""
"""
Count digits in a number
Given a number, use recursion to count how many digits it has.

def count_numbers(n):
    if n == 0:
        return 1
    else:
        return n * count_numbers(n-1)

print(count_numbers(5))
"""
"""
Sum of digits
Use recursion to calculate the sum of all digits in a number (e.g., 123 → 1+2+3 = 6).


def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n%10) + sum_digits(n // 10)

print(sum_digits(123))
"""
"""
Reverse a string
Write a recursive function to reverse a string (without using slicing or built-in reverse).

def reverse_string(S):
    if len(S) == 0:
        return ""
    else:
        return S[-1] + reverse_string(S[:-1])

print(reverse_string("hello"))
"""
"""
Find the maximum element in a list
Use recursion to find the largest number in a list.

def find_max(n):
    if len(n) == 1:
        return n[0]

    else:
        max_rest = find_max(n[1:])
        return n[0] if n[0] > max_rest else max_rest

print(find_max([5, 12, 3, 9, 21, 7]))
"""
"""
Check if a string is palindrome
Recursively check if a string reads the same forward and backward.

def is_palindrome(s):
    if len(s) == 1:
        return True
    else:
        return s[::-1] == s

print(is_palindrome("madam"))
print(is_palindrome("hello"))
"""
"""
Binary Search (Recursion)
Implement binary search recursively to find an element in a sorted list.

def binary_search(arr, low, high, target):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid +1, high, target)

print(binary_search([2, 5, 7, 9, 12, 15, 20], 0,6,12))
"""
"""
Tower of Hanoi
Write a recursive function to solve the Tower of Hanoi problem for n disks.

def tower_of_hanoi(n, source, auxilary, destination):
    if n == 1:
        print(f"move from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, auxilary)
    print(f"Move disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, auxilary, source, destination)


print(tower_of_hanoi(3, 'A', 'B', 'C'))
"""




