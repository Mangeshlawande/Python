# write a program that prompt the user for two number and display the addition, sub, mult, and div between them ;
# num1 = float(input("Enter first num: "));
# num2 = float(input("Enter second number :"));

# add = num1 + num2;
# sub = num1 - num2;
# mult = num1 * num2;
# div = num1  / num2;

# print("addition", add);
# print("subtraction", sub);
# print("Mult", mult);
# print("division", div);

# grades for user 
g1 = float(input("Enter the first grade: "));
g2 = float(input("Enter 2nd grade: "));
g3 = float (input("Enter 3rd grade: "));


mean = (g1 + g2 + g3) / 3;

rounded_mean = round(mean,2);

#  display the result with decimal places

print("Arithmatic mean :", "{:.2f}".format(rounded_mean));
