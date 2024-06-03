a = 33
b = "annie"
c= "annie's friend"
c = 'annie"s best friend'  # use this if you have single quotes in string 
print(a,b)                                                       
print(a,b,c)
# print(type(b))

greeting = "good Morning "
name = 'MM'
# print(greeting + name)
#concatenating two string 

d = greeting + name
print(d)
name = 'Clark' # length from 0 to  ie. 5
print (name[0]) 
print (name[1]) 
print (name[2]) 
print (name[3])
print (name[4])
# name[3] = 'f' --> not work 
# string slicing 
print(name[0:3]) # it not include last character 
print(name[0:4]) # it not include last character 
print(name[:4]) # it not include last character 
print(name[1:]) # it not include last character 
print(name[:]) # it not include last character 
print(name[-1]) # it not include last character 
print(name[-5:-1]) # It is as same as [1:4]
print(name[:-1]) # it not include last character 

#slicing with skip value 
channel = "Code with Harry"
print(channel)
d = channel[1::1]# it parsee the character one by one from 1 to 12
d = channel[1::2]# it skip 1 character from 1 to 12
print(d)