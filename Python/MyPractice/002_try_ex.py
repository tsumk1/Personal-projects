# Винятки 
num = None
while num is None:
    try: 
        num = int(input("Enter number: "))
        num += 10
        print(num)
    except ValueError:
        print("Ви ввели щось не те")
    else:
        print("Умнічка")

print("\n----------------------------------\n")

num2 = 0 
while num2 == 0:
    try:
        a = 80
        num2 = int(input("Enter number: "))
        result = a/num2
        print(result)
    except ValueError:
        print("Можливо ви ввели щось не те")
    except ZeroDivisionError:
        print("На нуль ділити не можна!")
