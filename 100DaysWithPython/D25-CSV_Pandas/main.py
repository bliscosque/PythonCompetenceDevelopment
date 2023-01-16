# with open("./weather_data.csv") as f:
#     lines=f.readlines()
#     print(lines)

# import csv

# with open("./weather_data.csv") as f:
#     data=csv.reader(f)
#     temperatures=[]
#     for row in data:
#         #print(row)
#         if row[1]!='temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


# https://pandas.pydata.org/docs/
import pandas
data=pandas.read_csv("./weather_data.csv")
#print(data["temp"])
# data_dict=data.to_dict()
# print(data_dict)
temps=data["temp"]
# sum=0
# for temp in temps:
#     sum+=temp
# print(sum/len(temps))
#print(temps.mean())
# print(temps.max())
# print(data["condition"])
# print(data.condition)
# print(data[data.day=="Monday"])

print(data[data.temp==temps.max()])

data_dict={
    "students": ["s1", "s2", "s3"],
    "scores": [100,99,90]
}
data=pandas.DataFrame(data_dict)
print(data)