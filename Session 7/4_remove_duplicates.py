numbers = [1, 2, 3, 4, 2, 3, 5, 6, 1]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)