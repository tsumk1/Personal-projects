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
print("----------ColumnsName----------")
print(frame.columns)
print("----------TypesofColumns----------")
print(frame.dtypes)
print("----------FrameSize----------")
print(frame.shape)

print("\n -----------------------------------------NextLVL-----------------------------------------")

print("----------ChooseColumn----------")
print(frame["nationality"])
print("----------ChooseColumn----------")
print(frame[["name", "car_number"]])

print("\n -----------------------------------------NextLVL-----------------------------------------")

frame["points_per_race"] = (frame["points"] / races).round(2)
print("----------AvPoints----------")
print(frame)