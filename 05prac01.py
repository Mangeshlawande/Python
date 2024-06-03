# Q1. 
myDict ={ 
    "pankha": 'fan',
    'dabba' : 'box',
    'vastu':'item'


}
print('options are :',myDict.keys())
a = input("Enter the hindi word \n")
# print("The meaning of your word is :",myDict[a])
# below line will not throw error  if the key is not present in the directory.
print("The meaning of your word is :",myDict.get(a))

#  
