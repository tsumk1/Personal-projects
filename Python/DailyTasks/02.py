#Given an array and an integer k, rotate the array to the right by k positions.
#Each rotation moves the last element to the beginning
numbers = [1, 2, 3, 4, 5] 
l = len(numbers)
k = int(input("Enter the number of rotations: "))
k = k%l # this cope with k > len of the array
res = numbers[-k:] + numbers[:-k]
print(res)

# numbers[:] - takes all elements 
# numbers[:-k] - takes everything except the last k elements:
# numbers[-k:] - takes onle the last key elements