name=input("Enter your name:")
Math_score=int(input("Enter your Math score:"))
Physics_score=int(input("Enter your Physics score:"))
programming_score=int(input("Enter your Programming score:"))

Total_score=Math_score+Physics_score+programming_score
Average_score=Total_score/3

if Average_score>=80:
    print(name,"You have passed the exam with an average score of",Average_score)
elif Average_score>=60:
    print(name,"You have passed the exam with an average score of",Average_score)
elif Average_score>=40:
    print(name,"You have passed the exam with an average score of",Average_score)
else:
    print(name,"You have failed the exam with an average score of",Average_score)
