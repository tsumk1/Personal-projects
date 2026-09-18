#Інформація про таблицю 1
import pandas as pd

data = {
    "name": ["Sasha","Pasha","Masha", "Max"],
    "age": [17,18,17,17],
    "score": [11,2,6, 12]
}

frame = pd.DataFrame(data) 

print(frame)
print("---------------------")

sp = frame.shape # .shape це атрибут (властивість). Звертається  напряму до об'єкта таблиця.форма (рядок, стовпці)
cl = frame.columns # назви стовпців 
dt = frame.dtypes # типи даних 
hd = frame.head(2) # перші 2 рядки 
tl = frame.tail(2) # останні 2 рядки 
print("---------------------")
print(sp)
print("---------------------")
print(cl)
print("---------------------")
print(dt)
print("---------------------")
print(hd)
print("---------------------")
print(tl)
