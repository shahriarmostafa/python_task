display the sum and average

numbers = []

for i in range(5):
    value = int(input("Enter integer number " + str(i + 1) + ": "))
    numbers.append(value)

print("All the numbers are:", numbers)

largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest number  :", largest)
print("Smallest number :", smallest)

total = 0
for n in numbers:
    total = total + n

average = total / len(numbers)

print("Sum of numbers  :", total)
print("Average         :", average)
