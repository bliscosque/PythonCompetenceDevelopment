sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words=sentence.split()
result={word:sentence.count(word) for word in sentence.split()}
result={word:len(word) for word in sentence.split()}


print(result)