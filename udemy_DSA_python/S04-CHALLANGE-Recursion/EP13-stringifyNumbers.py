#Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. 

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

def stringifyNumbers(obj):
    if len(obj)==0: return
    for key in obj:
      if type(obj[key]) is dict:
        stringifyNumbers(obj[key])
      else: 
        if type(obj[key]) is int:
          obj[key]=str(obj[key])
    return obj



 
print(stringifyNumbers(obj))
 
#{'num': '1', 
# 'test': [], 
# 'data': {'val': '4', 
#          'info': {'isRight': True, 'random': '66'}
#          }
#}