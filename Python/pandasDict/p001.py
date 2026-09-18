#Створення таблиці 1
import pandas as pd 

data = {
    "name": ["Sasha","Pasha","Masha"],
    "age": [17,18,17],
    "score": [11,2,6]
}

data_frame = pd.DataFrame(data) 

print(data_frame)

