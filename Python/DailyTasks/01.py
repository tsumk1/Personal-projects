# ---Count Local Peaks---
# An element is a peak if it is strictly greater than both its neighbours.
# Count the number of peaks in an array. Ignore the first and last elements.

numbers = [1, 4, 2, 5, 3, 6, 1]
count = 0 

try:
    for j  in range(1, len(numbers)-1):
        if numbers[j]>numbers[j+1] and numbers[j]>numbers[j-1]:
            count += 1
    print(count)
except Exception:
    print('Error')