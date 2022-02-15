import re

# Creates a list where the numbers will be appended
numbers = list()

# Opens the file
with open('regex_sum_1468662.txt', "r") as haystack:
    # For each line in the file
    for line in haystack:
        # Use regex to find numbers. They will be output as a list because of re.findall() functionality
        needles = re.findall('[0-9]+', line)
        # For each number found by regex
        for needle in needles:
            # If regex found any numbers
            if len(needles) != 0:
                # Convert them into integers and append them to the list
                numbers.append(int(needle))
            # If regex didn't find any number, just go to the next line
            else:
                continue

# Print the sum of all the numbers
print(sum(numbers))
