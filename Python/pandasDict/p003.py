#Вибір рядків 1
import pandas as pd

data = {
    "name": ["Sasha","Pasha","Masha", "Max"],
    "age": [17,18,17,17],
    "score": [11,2,6, 12], 
    "city": ["Kyiv", "Zhitomyr", "London", "Kyiv"]
}

frame = pd.DataFrame(data) 
print(frame)
print("---------------------")

# Знайти студентів яким 17 років
stud_age = frame[frame["age"] ==  17]
print(stud_age)
print("---------------------")

#Знайти студентів з балом вище за 8
stud_score = frame[frame["score"] >= 8]
print(stud_score)
print("---------------------")

#Знайти студентів які живуть в London 
stud_city = frame[frame["city"] == "London"]
print(stud_city)
print("---------------------")

#Знайти студентів віком 17 років і які мають оцінку більше >= 8
stud_age_score = frame[(frame["age"] == 17) & (frame["score"] >= 8)]
print(stud_age_score)
print("---------------------")

#Знайти студента з оцінкою = 8 
stud_score2 = frame[frame["score"] == 8]
print(stud_score2)