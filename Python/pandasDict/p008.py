#Filtering and sorting
import pandas as pd
from tabulate import tabulate 

data = {
    "name": ["Antonelli","Russell", "Hailton", "Verstappen"],
    "team": ["Mercedes", "Mercedes", "Ferrari", "Red Bull"],
    "nationality":["ITA", "GBR", "GRB", "NED"],
    "car_number": [12, 63, 44, 3],
    "points": [340, 238, 229, 221]
}

races = 24

frame = pd.DataFrame(data)
#print(frame)
print("----------DataFrame----------")
print(tabulate(frame, headers="keys", tablefmt="rounded_grid",showindex=False))




print("\n -----------------------------------------Filtering-----------------------------------------")
print("----------MoreThan230----------")
result = frame[frame["points"] > 230]
print(tabulate(result, headers="keys", tablefmt="rounded_grid",showindex=False))

print("----------McLaren----------")
result = frame[frame["team"] == "McLaren"]
print(tabulate(result, headers="keys", tablefmt="rounded_grid",showindex=False))

print("----------Red Bull----------")
result = frame[frame["team"] == "Red Bull"]
print(tabulate(result, headers="keys", tablefmt="rounded_grid",showindex=False))

print("----------From225To245----------")
result = frame[(frame["points"] >= 225) & (frame["points"] <= 245)]
print(tabulate(result, headers="keys", tablefmt="rounded_grid",showindex=False))




print("\n -----------------------------------------Sorting-----------------------------------------")

print("----------MaxToMin----------")
max = frame.sort_values(by="points", ascending=False) #ascending = False/True - 
print(tabulate(max, headers="keys", tablefmt="rounded_grid",showindex=False))

print("----------MinToMax----------")
min = frame.sort_values(by="points", ascending=True) 
print(tabulate(min, headers="keys", tablefmt="rounded_grid",showindex=False))




print("\n -----------------------------------------Find....-----------------------------------------")
print("----------Max----------")
max_points = frame["points"].max()
print(tabulate(frame[frame["points"] == max_points], headers="keys", tablefmt="rounded_grid",showindex=False))

print("----------Min----------")
min_points = frame["points"].min()
print(tabulate(frame[frame["points"] == min_points], headers="keys", tablefmt="rounded_grid",showindex=False))