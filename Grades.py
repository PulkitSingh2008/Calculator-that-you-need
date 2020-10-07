def grade_obtained(percentage):
	if (percentage >= 60) :
		print("1st Division")
	elif (percentage >= 50 and percentage <= 59) :
		print("2nd Division")
	elif (percentage >= 40 and percentage <= 49) :
		print("3rd Division")
	else:
		print("Fail")

print("Please enter your marks out of 100")
subject1=float(input("Please enter your marks of subject 1: "))
subject2=float(input("Please enter your marks of subject 2: "))
subject3=float(input("Please enter your marks of subject 3: "))
subject4=float(input("Please enter your marks of subject 4: "))
subject5=float(input("Please enter your marks of subject 5: "))

percentage = (subject1 + subject2 + subject3 + subject4 + subject5) / 500 * 100

grade_obtained(percentage)
