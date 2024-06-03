# Q1. 

letter = '''Dear <|NAME|>,
Greeting from coding house, I am happy to inform you about your selection 
You are selected!
Have a great day ahead !
Thanks and Reards,
Date : <|DATE|>
   '''
name = input( "Enter your name:\n")
letter = letter.replace("<|NAME|>",name)
date = input ("Enter Date:\n")
letter = letter.replace("<|DATE|>",date)
print(letter)