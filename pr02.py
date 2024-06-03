sub1 = int(input("Enter Your DBMS marks:\n"))
sub2 = int(input("Enter Your SPOS marks:\n"))
sub3 = int(input("Enter Your TOC marks:\n"))
sub4 = int(input("Enter Your CNS marks:\n"))
sub5 = int(input("Enter Your SPM marks:\n"))
sum = (sub1 + sub2 + sub3 + sub4 + sub5)/5 

if (sub1<33 or sub2 <33 or sub3<33 or sub4<33 or sub5<33):
    print("You are Fail  bcoz you have less than 33% in one of the subject!!")
    print("your marks is",sum ,"%")

elif( sum <40):
    print("You are fail due to total percentage less than 40 !!")
    print("your marks is",sum ,"%")

else:
    print("Congratulations !! You passed the exam")
    print("your marks is",sum ,"%")

