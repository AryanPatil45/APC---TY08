# 1.	Write a Python program to create a list of five fruits and display the list.

fruits=["Banana","mango","Apple","Pineapple","avacado"]

print("List of fruits:" , fruits)

# 2.	Create a list of five integers. Display:
# •	First element 
# •	Last element 
# •	Third element

integers=[12,24,31,43,22]
print(integers[0])
print(integers[4])
print(integers[2])

# 3.	Create a list of colors. Replace the third color with another color and display the updated list.
colors=["red","green","Yellow","Blue","Orange"]
colors[2]="purple"
print("Updated colors list: ",colors)

# 4.	Create a list of numbers. Add:
# •	One element at the end 
# •	One element at the beginning 
# •	One element at a specified position 
# Display the updated list.
nums=[2,3,4,5]
nums.append(6)
nums.insert(0,1)
nums.insert(2,7)
print("updated list: ",nums)

# 5.	Create a list of student names. Remove:
# •	First student 
# •	Last student 
# •	A specific student by name 
# Display the remaining list.
students=["Sanket","Aditya","Aryan","Rushi","Parshwa"]
students.pop(0)
students.pop()
students.remove("Aditya")
print("Remaining List: ",students)


# 6. Write a program to find the largest and smallest number in a list without using max() or min().

values = [25, 10, 45, 5, 30]

largest = values[0]
smallest = values[0]

for num in values:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)

# ---------------------------------------------------------------------------

# 7. Accept 10 numbers from the user and store them in a list. Calculate:
# •	Sum 
# •	Average 


Numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    Numbers.append(num)

total = 0
for num in Numbers:
    total = total + num

average = total / 10

print("Sum:", total)
print("Average:", average)


# ----------------------------------------------------------------------------

# 8. Store 15 integers in a list. Count how many numbers are:
# •	Even 
# •	Odd

numbers = [10, 15, 22, 33, 40, 51, 64, 77, 80, 91, 12, 25, 36, 49, 50]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)

# ---------------------------------------------------------------------------

# 9. Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

cities = ["Kolhapur", "Pune", "Mumbai", "Banglore", "Delhi", "Hydrabad"]

city = input("Enter City name: ")

if city in cities:
    print("City exists in the list")

else:
    print("City does not exists")

# -----------------------------------------------------------------------------

# 10. Write a program to reverse a list without using the reverse() method.

numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)

# ------------------------------------------------------------------------------

# 11.	Create a list of 10 numbers and display:
# •	First 5 elements 
# •	Last 5 elements 
# •	Middle 4 elements 
# •	Alternate elements 
# •	Reverse list using slicing

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 5 elements:", numbers[:5])

print("Last 5 elements:", numbers[-5:])

print("Middle 4 elements:", numbers[3:7])

print("Alternate elements:", numbers[::2])

print("Reversed list:", numbers[::-1])

# 12.	Display all elements present at even index positions.

num_list=[10,20,30,40,50,60,70,80,90]

for i in range(0, len(num_list), 2):
    print(num_list[i])


# 13.	Accept 10 numbers and sort them in:
# •	Ascending order 
# •	Descending order

numms=[]
for i in range(10):
    my_list=int(input("Enter Number: "))
    numms.append(my_list)

numms.sort()
print("Numbers in ascending order:",numms)

numms.sort(reverse=True)
print("Numbers in descending order:",numms)

# 14. Create a list containing duplicate values and display only unique elements.

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("Unique elements:", unique)

# --------------------------------------------------------------------------

# 15. Find the second largest element in a list.

numbers = [10, 25, 45, 30, 50, 40]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest element:", largest)
print("Second largest element:", second_largest)

# ---------------------------------------------------------------------------

