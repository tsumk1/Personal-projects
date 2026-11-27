# Given an array of integers, find the maximum value of:
# numbers[j] - numbers[i]
# where (j > i).
# In other words, the second element must come after the first.
numbers = [7, 1, 5, 3, 6, 4]
l = len(numbers)
max_diff = 0

for i in numbers:
    for j in range(i+1, l):
        diff = numbers[j]-numbers[i]
        if diff>max_diff:
            max_diff = diff
print(max_diff)