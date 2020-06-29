name=input("Enter studnet name")
assignments=[]
quizzes=[]
tests=[]
grade=""

for x in range(4):
    assignments.append(float(input("Enter Assingments Marks:")))
for x in range(3):
    quizzes.append(float(input("Enter Quizzes Marks:")))
for x in range(2):
    tests.append(float(input("Enter Tests Marks:")))

studentProfiles={
    "name":name,
    "assignments":assignments,
    "quizzes":quizzes,
    "tests":tests}

print("Name\t"+studentProfiles["name"])
print("assignments\t")
print(studentProfiles["assignments"])
print("quizzes\t")
print(studentProfiles["quizzes"])
print("tests\t")
print(studentProfiles["tests"])

assignmentAvg=(sum((studentProfiles["assignments"]))/4)
quizAvg=(sum((studentProfiles["quizzes"]))/3)
testAvg=(sum((studentProfiles["tests"]))/2)

print("Assignment Average\t %f" %assignmentAvg)

print("Quizzes Average\t %f"%quizAvg)

print("Tests Average\t %f" %testAvg)

final_score_assignment= assignmentAvg*0.1
final_score_quiz= quizAvg*0.3
final_score_test= testAvg*0.6

final_score = final_score_assignment+final_score_quiz+final_score_test

if final_score >= 90:
   grade="A"
elif final_score >=80:
    grade="B"
elif final_score >=70:
    grade="C"
elif final_score >=60:
    grade="D"
else:
    grade="F"

    

print(grade)






