a = {1, 2,3,4,7,8,2}
print(type(a))
print(a)

# empty set
# IMP : This syntax will create empty dictionary and not empty set
b = {}
print(type(b))

# Empty set can create using below syntax:
c = set()
print(type(c))

c.add(4)
c.add(3)
c.add(6)
print(c)
# c.add({4:5}) = cannot add list or directoy to set 

# length of set 
print(len(c))
c.remove(3)# remove value from set 
print(c.pop())# remove randomly
c.union({8,11})
print(c)

