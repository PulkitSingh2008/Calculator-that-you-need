#defining function (calculation)
def calculation(number1,number2):
  # if statements to perform calculations
  if operator =="+":
    total=number1+number2
    return (total)
  elif operator =="*":
    total=number1*number2
    return (total)
  elif operator =="^":
    total=number1**number2
    return (total)
  elif operator =="**":
    total=number1**number2
    return (total)
  elif operator =="-":
    total=number1-number2
    return (total)
  elif operator =="/":
    total=number1/number2
    return (total)
  else:
    return ("Invalid operation")


number1=float(input("please enter your first number: "))
print(number1)
number2=float(input("please enter your second number: "))
print(number2)
operator=input("Please enter the arithmetic operator: ")
print(operator)
#calling function(calculation)
calculation(number1,number2)
