import pandas as pd 

data = {
    "name": ["Oleg","Alex", "Michael", "George"],
    "math": [11, 9, 12, 10],
    "programming": [12, 10, 9, 11],
    "english": [11, 11, 10, 12]
}

frame = pd.DataFrame(data)
frame["average"] = (frame["math"] + frame["programming"] + frame["english"]) / 3 #додала колонку з середнім значенням 

print(frame)
print("------Sorted-----------")

#Відсортуй студентів від найкращого до найгіршого.
top = frame.sort_values(by="average", ascending=False)
print(top)
print("------Sorted-----------")

#Відсортуй за програмуванням у порядку спадання.
prog = frame.sort_values(by="programming", ascending=False)
print(prog)
