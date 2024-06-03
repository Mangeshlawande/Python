myDict = {
    "course": " Python ",
    "channel" : "Code With Harry",
    "key" : "value",
    "marks":[ 23,24,25],
"anotherDict": { "Name": "akash"},
1 : 2
}       
# dictionary mehods
print(myDict.keys())
print(myDict.values())
print(type(myDict.keys()))
print(list(myDict.keys()))#['course', 'channel', 'key', 'marks', 'anotherDict', 1]
print(type(myDict.keys()))
print(myDict.items()) # print (key: values ) for all contents of dictionary
print(myDict)
updatedict = {'friend':'vaibhav', 
              'friend2':'akash',
              'friend3':'prakash'
              }
myDict.update(updatedict)
print(myDict)
# print(myDict.get('marks')) # it return none if key is not present.
# print(myDict['marks'])# it throws error if key was not present.
# print(myDict['marks1'])# it throws error if key was not present.
print(myDict.get('marks1')) # it return none if key is not present.



