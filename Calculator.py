print("CALCULATOR")
#The first number given by the user
num1=float(input("Please enter your first number: "))
print(num1)
#The second number given by the user
num2=float(input("Please enter your second number: "))
print(num2)
#This is the operator given by the user
operator=input("Please enter your arithmetic operator: ")

print("Solution: ")
print(num1)
print(num2)
print(operator)
print("--------------")

# if statements to perform calculations
if operator == "+":
	print(num1+num2)
elif operator =="-":
	print(num1-num2)
elif operator=="*":
	print(num1*num2)
elif operator=="/":
	print(num1/num2)
else :
	print("Answer not found!!")
