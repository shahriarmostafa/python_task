
numbers = []

for i in range(5):
    number = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(number)

print("Largest: " + str(max(numbers)))
print("Smallest: " + str(min(numbers)))
print("Sum: " + str(sum(numbers)))
print("Average: " + str(sum(numbers) / len(numbers)))
