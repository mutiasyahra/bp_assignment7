numbers = [10, 20, 5, 40, 30, 72, 34]
largest_number = numbers[0]
smallest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number
    if number < smallest_number:
        smallest_number = number

print("The largest number is: ", largest_number)
print("The smallest number is: ", smallest_number)