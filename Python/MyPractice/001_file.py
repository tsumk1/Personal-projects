file = open('file1.txt', 'w') # w - write
file.write('\nHellooooo')

file = open('file1.txt', 'a') # a - append
file.write(' world!\n\n')

data = input('Write smth:')
file.write(data)

file = open('file1.txt', 'r') # r - read
print(file.read()) #  - displaying file in terminal 

file.close()