student_scores = input("Input a list of student scores ").split(",")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

##score = max(student_scores)        shorter method using max function
##print(f"The highest score in the class is: {score}")

highest_score = 0
for n in student_scores:
    if n > highest_score:
        highest_score = n
print(f"The highest score in the class is: {highest_score}")
