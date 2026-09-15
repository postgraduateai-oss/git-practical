name=input("Enter students name: ")
subject1=float(input("Enter first subject mark: "))
subject2=float(input("Enter second subject mark: "))
avg_marks=(subject1+subject2)/2
total_marks=subject1+subject2
if subject1 < 40 or subject2 < 40:
    overall_status = "Failed"
else:
    overall_status = "Passed"
print("Student name: ",name)
print("Total Mark: ",total_marks)
print("Average Mark: ",avg_marks)
print("Result: ",overall_status)
print("=======================")
print("Student")
