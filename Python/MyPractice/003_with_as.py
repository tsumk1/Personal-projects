#With...as
try:
    with open('file2.txt', 'r') as file: # - with..as automatically closes file 
        print(file.open)    
except FileNotFoundError:
    print("Файл не знайдено")
