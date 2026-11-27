# 3 , but better 
numbers = [7, 1, 5, 3, 6, 4]

l = len(numbers)
max_diff = 0
min_num = numbers[0] 

for i in numbers:
    diff = i - min_num
    if diff > max_diff:
        max_diff = diff
    if i < min_num:
        min_num = i
            
print(max_diff)