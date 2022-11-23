#Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
 
def collectStrings(obj):
    ans=[]
    if len(obj)==0: return
    for key in obj:
      #print(type(obj[key]))
      if type(obj[key]) is dict:
        ans.extend(collectStrings(obj[key]))
      else: 
        if type(obj[key]) is str:
          ans.append(obj[key])
    return ans

print(collectStrings(obj)) # ['foo', 'bar', 'baz']