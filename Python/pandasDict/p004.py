# Робота з даними 2 
import pandas as pd 

data = {
    "name": ["Maxim","Vika", "Sasha", "Polina"],
    "math": [11, 9, 12, 10],
    "programming": [12, 10, 10, 11],
    "english": [11, 11, 10, 12]
}

frame = pd.DataFrame(data)
print(frame)
print("---------------------")

#Знайти середню оцінку з математики
av_m = frame["math"].mean() 
print(av_m)
print("---------------------")

#Знайти середню оцінку з програмування
av_p = frame["programming"].mean() 
print(av_p)
print("---------------------")

#Знайти середню оцінку з англійської
av_e = frame["english"].mean() 
print(av_e)
print("---------------------")

#Знайти максимальну оцінку з кожного предмета 
max_scores_math = frame["math"].max()
max_scores_prog = frame["programming"].max()
max_scores_engl = frame["english"].max()
print("Max:")
print(" Математика: ", max_scores_math, " Програмування: ", max_scores_prog, " Англійська: ", max_scores_engl)
print("---------------------")

#Знайти мінімальну оцінку з кожного предмета 
max_scores_math = frame["math"].min()
max_scores_prog = frame["programming"].min()
max_scores_engl = frame["english"].min()
print("Min:")
print(" Математика: ", max_scores_math, " Програмування: ", max_scores_prog, " Англійська: ", max_scores_engl)
print("---------------------")
