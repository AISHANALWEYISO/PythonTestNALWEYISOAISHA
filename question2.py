# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F


student_score = int(input("Enter the student_score in percentage: "))

if student_score >= 90:
        print("Grade A") 

elif student_score >= 80:
        print("Grade B")   

elif student_score >=70:
        print("Grade C") 

elif student_score >=60:
        print("Grade D")        

elif student_score >=40:
        print("Grade E")    
else:
        print("Grade F")    