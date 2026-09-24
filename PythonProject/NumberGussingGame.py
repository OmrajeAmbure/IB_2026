import random

while True:
    print("Loding....")
    print("Can You Start To Play ? [Y/N] : ")
    inp1 = input()
    GUSSING_NUMBER = random.randint(1,10)
    SCORE = 100
    if inp1 == "Y" or inp1 == "y":
        print("---------------Start For Playing-----------------------")
        print(
        """Rule:
    1. You Must Be Guess The Number Between 1 TO 10
    2. You Have TOtal 5 Attempt
    3. If YOu Guess The Correct Number Score Will Increse
    4. Inital Point Will Be 100
    5. Correct Case ScorePoint and wrong Case :
        Attempt 1 -> If worong Dcrease 20
        Attempt 2 -> If worong Dcrease 20
        Attempt 3 -> If worong Dcrease 20
        Attempt 4 -> If worong Dcrease 20
        """)
        # logic
        for i in range(1,5):
            if i == 1:
                print(f"Enter The Number for Attempt {i}")
                n1 = int(input())
                if n1 == GUSSING_NUMBER:
                    print(f"Your Attempt {i} Guess Was Correct ")
                    SCORE += 100
                    break
                else:
                    print(f"Your Attempt {i} was Fail")
                    loss_point = SCORE // 5
                    SCORE = SCORE - loss_point
                print(f"Score : {SCORE}")
            elif i == 2:
                print(f"Enter The Number for Attempt {i}")
                n2 = int(input())
                if n2 == GUSSING_NUMBER:
                    print(f"Your Attempt {i} Gussing Was Correct ")
                    SCORE += 70
                    break
                else:
                    print(f"Your Attempt {i} was Fail")
                    loss_point = SCORE // 4
                    SCORE = SCORE - loss_point
                print(f"Score : {SCORE}")
            elif i == 3:
                print(f"Enter The Number for Attempt {i}")
                n3 = int(input())
                if n3 == GUSSING_NUMBER:
                    print(f"Your Attempt {i} Gussing Was Correct ")
                    SCORE += 50
                    break
                else:
                    print(f"Your Attempt {i} was Fail")
                    loss_point = SCORE // 3
                    SCORE = SCORE - loss_point
                print(f"Score : {SCORE}")
            elif i == 4:
                print(f"Enter The Number for Attempt {i}")
                n3 = int(input())
                if n3 == GUSSING_NUMBER:
                    print(f"Your Attempt {i} Gussing Was Correct ")
                    break
                else:
                    print(f"Your Attempt {i} was Fail")
                    SCORE = 0
                print(f"Score : {SCORE}")
        print(f"YOur Gussing Number : {GUSSING_NUMBER} Your Score is {SCORE}")
        if SCORE <= 20:
            print("You Have Lost The Game")
        elif SCORE > 20:
            print("Congratulations Your WOn The Game")
        print("---------------End The Game -----------------------")
        
    elif inp1 == "N" or inp1 == "n":
        break
    print("Do You Wnat Continue Play [Y/N] : ")
    inp2 = input()
    if inp2 == "Y" or inp2 == "y":
        pass;
    elif inp2 == "N" or inp2 == "n":
        print("Game Over Thank You")
        break
