import random

def ScoreAndGrade():
    print "Scores and Grades"
    for i in range(0, 10):
        score = random.randint(60, 100)

        if score <= 100 and score >= 90:
            grade = "A"
        elif score <= 89 and score >=80:
            grade = "B"
        elif score <= 79 and score >=70:
            grade = "C"
        elif score <= 69 and score >=60:
            grade = "D"
        else:
            grade = "F"
    
        print ("Score: " + str(score) +"; Your grade is " + grade)
    print("End of the program. Bye!")

ScoreAndGrade()