import pandas
data=pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sqs_len=len(data[data["Primary Fur Color"]=="Gray"])
red_sqs_len=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_sqs_len=len(data[data["Primary Fur Color"]=="Black"])

# print(grey_sqs_len)
# print(red_sqs_len)
# print(black_sqs_len)
data_dict={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_sqs_len, red_sqs_len, black_sqs_len]
}

df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")