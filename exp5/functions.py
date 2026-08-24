# 1. Write a function factorial(n) that accepts an integer and returns its factorial.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))


# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


n = int(input("Enter a number: "))
print(check_even_odd(n))


# 3. Define a function that accepts two numbers and returns the greater number.

def greater(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = greater(num1, num2)
print("Greater number is:", result)


# 4. Create a function simple_interest(p, r, t) to calculate simple interest.

def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time(year(s)): "))

result = simple_interest(p, r, t)

print("Simple Interest =", result)


# 5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

print(is_prime(n))


# 6. Define a function to calculate the area of a circle using its radius.

import math

def circle_area(r):
    area = math.pi * r * r
    return area

radius = float(input("Enter radius: "))

result = circle_area(radius)

print("Area of circle =", result)


# 7. Write a function that accepts n and returns the sum of the first n natural numbers.

def sum_natural(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))

result = sum_natural(n)

print("Sum =", result)


# 8. Create a function power(base, exponent) to calculate the value of base raised to exponent.

def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = power(base, exponent)

print("Result =", result)


# 9. Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.

def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

numbers = [10, 25, 7, 45, 18]

result = find_largest(numbers)

print("Largest element =", result)


# 10. Define a function that accepts a string and returns the number of vowels present in it.

def count_vowels(string):
    count = 0

    for ch in string:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count

text = input("Enter a string: ")

result = count_vowels(text)

print("Number of vowels =", result)


# 11. Write a function that accepts a string and returns its reverse.

def reverse_string(string):
    reverse = ""

    for ch in string:
        reverse = ch + reverse

    return reverse

text = input("Enter a string: ")

result = reverse_string(text)

print("Reversed string =", result)


# 12. Create a function that checks whether a given string or number is a palindrome.

def is_palindrome(value):
    value = str(value)

    reverse = ""

    for ch in value:
        reverse = ch + reverse

    return value == reverse

value = input("Enter a string or number: ")

if is_palindrome(value):
    print("Palindrome")
else:
    print("Not Palindrome")


# 13. Write a function that accepts a list of numbers and returns their average.

def calculate_average(numbers):
    total = 0

    for num in numbers:
        total = total + num

    average = total / len(numbers)

    return average

numbers = [10, 20, 30, 40, 50]

result = calculate_average(numbers)

print("Average =", result)


# 14. Define a function that accepts a list and an element and returns the number of times that element occurs.

def count_occurrences(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count = count + 1

    return count

numbers = [10, 20, 10, 30, 10, 40]
element = int(input("Enter element to search: "))

result = count_occurrences(numbers, element)

print("Number of occurrences =", result)


# 15. Write a function that accepts a list and returns a new list containing only unique elements.

def unique_elements(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique

numbers = [10, 20, 10, 30, 20, 40, 10]

result = unique_elements(numbers)

print("Unique elements =", result)


# 16. Create a function to find the second-largest number in a list.

def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

numbers = [10, 25, 7, 45, 18]

result = second_largest(numbers)

print("Second largest =", result)

#17.Write a function that accepts n and returns the first n Fibonacci numbers.
