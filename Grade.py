vocareum_grades = []
for x in range(13):
    if x == 12:
        prompt = "What is your grade for Vocareum assignments 49-50? "
    else:
        prompt = "What is your grade for Vocareum assignments {}-{}? ".format(x*4+1, x*4+4)
    grade = int(input(prompt))
    vocareum_grades.append(grade)

quiz_grades = []
for x in range(12):
    prompt = "What is your grade for quiz {}? ".format(x+1)
    grade = int(input(prompt))
    quiz_grades.append(grade)

lowest_quiz1 = min(quiz_grades)
quiz_grades.remove(lowest_quiz1)
lowest_quiz2 = min(quiz_grades)
quiz_grades.remove(lowest_quiz2)

hand_trace_grades = []
for x in range(10):
    prompt = "What is your grade for hand trace {}? ".format(x+1)
    grade = int(input(prompt))
    hand_trace_grades.append(grade)
hand_trace_grades = sorted(hand_trace_grades)[2:]

mini_project_grades = []
for x in range(12):
    prompt = "What is your grade for mini-project {}? ".format(x+1)
    grade = int(input(prompt))
    mini_project_grades.append(grade)

lowest_mini_project1 = min(mini_project_grades)
mini_project_grades.remove(lowest_mini_project1)
lowest_mini_project2 = min(mini_project_grades)
mini_project_grades.remove(lowest_mini_project2)

test_scores = []
for x in range(3):
    prompt = "What was your score on test {}? ".format(x+1)
    score = int(input(prompt))
    test_scores.append(score)

vocareum_points = sum(vocareum_grades)
quiz_points = sum(quiz_grades)
hand_trace_points = sum(hand_trace_grades)
mini_project_points = sum(mini_project_grades)
test_points = sum(test_scores)

total_points_earned = vocareum_points + quiz_points + hand_trace_points + mini_project_points + test_points
total_possible_points = 1200

semester_grade = (total_points_earned / total_possible_points) * 100

if semester_grade >= 90:
    letter_grade = "A!"
elif semester_grade >= 85:
    letter_grade = "A-"
elif semester_grade >= 80:
    letter_grade = "B+"
elif semester_grade >= 75:
    letter_grade = "B"
elif semester_grade >= 70:
    letter_grade = "B-"
elif semester_grade >= 65:
    letter_grade = "C+"
elif semester_grade >= 60:
    letter_grade = "C"
elif semester_grade >= 50:
    letter_grade = "D"
else:
    letter_grade = "F"

print("CALCULATING YOUR SEMESTER GRADE...")
print("Lowest two quizzes: {}, {}".format(lowest_quiz1, lowest_quiz2))
print("Lowest two mini-projects: {}, {}".format(lowest_mini_project1, lowest_mini_project2))
print("Total points earned: {}".format(total_points_earned))
print("Total possible points: {} <-- Note this is the 1200 shown in the syllabus".format(total_possible_points))
print("Percent grade: {:.1f} <-- or {:.2f} or {:.3f}".format(semester_grade, semester_grade, semester_grade))
print("You earned a(n) {}".format(letter_grade))
