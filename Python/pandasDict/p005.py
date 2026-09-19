import pandas as pd 

data = {
    "name": ["Maxim","Vika", "Sasha", "Polina"],
    "math": [11, 9, 12, 10],
    "programming": [12, 10, 10, 11],
    "english": [11, 11, 10, 12]
}

frame = pd.DataFrame(data)

#Знайди студента з найбільшим середнім
frame["average"] = (frame["math"] + frame["programming"] + frame["english"]) / 3 #додала колонку з середнім значенням 

print(frame)
print("----------Max---------")

max = frame["average"].max()
print("%.1f" % max)

#Знайди студента з найменшим середнім

print("----------Min---------")

min = frame["average"].min()
print("%.1f" % min)