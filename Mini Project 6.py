Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... quiz_scores = []
... project_scores = []
... total_score = 0
... 
... print("Please enter scores for 10 quizzes (out of 20):")
... for i in range(10):
...     score = int(input(f"Quiz {i+1}: "))
...     quiz_scores.append(score)
...     total_score += score
... 
... print("\nPlease enter scores for 10 mini-projects (out of 20):")
... for i in range(10):
...     score = int(input(f"Mini-project {i+1}: "))
...     project_scores.append(score)
...     total_score += score
... 
... quiz_avg = sum(quiz_scores) / len(quiz_scores)
... project_avg = sum(project_scores) / len(project_scores)
... overall_avg = total_score / 20
... highest_score = max(quiz_scores + project_scores)
... lowest_score = min(quiz_scores + project_scores)
... 
... print(f"\nQuiz average: {quiz_avg:.2f}")
... print(f"Mini-project average: {project_avg:.2f}")
... print(f"Overall average: {overall_avg:.2f}")
... print(f"Highest score: {highest_score}")
... print(f"Lowest score: {lowest_score}")
