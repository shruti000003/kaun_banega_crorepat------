print("kaun banega crore pati game")

questions = [
    [
"A man pushes his car to a  hotel and loses all his money. Wny?", "His car broke down.", "He was robbed.", 
"He sold his car.","He is playing a game.", 4
    ],
    [
"If you have me, you want to share me. If you share me, you don't have me.What am I?", "Money", "Idea", "Love",  "Secret", 4
    ],
    [
     "What will come next? J,F,M,A,M,J,J,A,S,O,N,", "D", "J", "F", "A", 4
     ],
     [
         "Find the missing number: 3,9,27,81?", "162", "300", "200", "243", 4
     ],
     [
         "If CAT=24, DOG=26, then BAT=?", "21", "25", "22", "23", 4
     ],
]


levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000] 
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"a. {question[1]}       b.{question[2]}")
    print(f"c. {question[3]}       d.{question[4]}")

    reply= int(input("enter your answer(1-4)"))
    if(reply == question[-1]):
        print(f"Correct answer, You have won Rs. {levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i==14):
            money= 10000000
    else:
        print("wrong answer!")
        break

print(f"Your take home money is {money}")