import random


# ============================================================
#                    COLOR CODES
# ============================================================



RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"


# ============================================================
#                    MAIN GAME
# ============================================================

while True:

    print(CYAN + BOLD)
    print("╔══════════════════════════════════════════════════════╗")
    print("║                                                      ║")
    print("║              🎯 NUMBER GUESSING GAME                ║")
    print("║                                                      ║")
    print("║                  Guess Number 1 - 10                 ║")
    print("║                                                      ║")
    print("╚══════════════════════════════════════════════════════╝")
    print(RESET)

    print(YELLOW + "Loading...." + RESET)

    print(BLUE + "\nCan You Start To Play ? [Y/N] : " + RESET)

    inp1 = input()

    GUSSING_NUMBER = random.randint(1, 10)

    SCORE = 100

    if inp1 == "Y" or inp1 == "y":

        # ====================================================
        #                    GAME START
        # ====================================================

        print(GREEN + BOLD)
        print("╔══════════════════════════════════════════════════════╗")
        print("║                                                      ║")
        print("║             🎮 START FOR PLAYING 🎮                 ║")
        print("║                                                      ║")
        print("╚══════════════════════════════════════════════════════╝")
        print(RESET)

        print(BLUE + BOLD)
        print("╔══════════════════════════════════════════════════════╗")
        print("║                    📜 GAME RULES                     ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                                                      ║")
        print("║  1. You Must Guess Number Between 1 TO 10            ║")
        print("║  2. You Have Total 5 Attempts                        ║")
        print("║  3. Initial Point Will Be 100                        ║")
        print("║  4. Wrong Guess → Score Will Decrease                ║")
        print("║  5. You Will Get HIGH / LOW Hint                     ║")
        print("║                                                      ║")
        print("╚══════════════════════════════════════════════════════╝")
        print(RESET)


        # ====================================================
        #                    GAME LOGIC
        # ====================================================

        for i in range(1, 6):

            # ------------------------------------------------
            #                    ATTEMPT 1
            # ------------------------------------------------

            if i == 1:

                print(CYAN + "\n────────────────────────────────────────────────────────" + RESET)

                print(
                    YELLOW +
                    f"🎯 Enter The Number For Attempt {i}" +
                    RESET
                )

                n1 = int(input())

                if n1 == GUSSING_NUMBER:

                    print(
                        GREEN +
                        f"✅ Your Attempt {i} Guess Was Correct!" +
                        RESET
                    )

                    SCORE += 100

                    break

                else:

                    print(
                        RED +
                        f"❌ Your Attempt {i} Was Fail!" +
                        RESET
                    )

                    # -------------------------------
                    # HIGH / LOW HINT
                    # -------------------------------

                    if n1 < GUSSING_NUMBER:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO LOW!" +
                            RESET
                        )

                    else:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO HIGH!" +
                            RESET
                        )

                    loss_point = SCORE // 5
                    SCORE = SCORE - loss_point

                print(MAGENTA + f"⭐ Score : {SCORE}" + RESET)


            # ------------------------------------------------
            #                    ATTEMPT 2
            # ------------------------------------------------

            elif i == 2:

                print(CYAN + "\n────────────────────────────────────────────────────────" + RESET)

                print(
                    YELLOW +
                    f"🎯 Enter The Number For Attempt {i}" +
                    RESET
                )

                n2 = int(input())

                if n2 == GUSSING_NUMBER:

                    print(
                        GREEN +
                        f"✅ Your Attempt {i} Guessing Was Correct!" +
                        RESET
                    )

                    SCORE += 70

                    break

                else:

                    print(
                        RED +
                        f"❌ Your Attempt {i} Was Fail!" +
                        RESET
                    )

                    # -------------------------------
                    # HIGH / LOW HINT
                    # -------------------------------

                    if n2 < GUSSING_NUMBER:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO LOW!" +
                            RESET
                        )

                    else:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO HIGH!" +
                            RESET
                        )

                    loss_point = SCORE // 4
                    SCORE = SCORE - loss_point

                print(MAGENTA + f"⭐ Score : {SCORE}" + RESET)


            # ------------------------------------------------
            #                    ATTEMPT 3
            # ------------------------------------------------

            elif i == 3:

                print(CYAN + "\n────────────────────────────────────────────────────────" + RESET)

                print(
                    YELLOW +
                    f"🎯 Enter The Number For Attempt {i}" +
                    RESET
                )

                n3 = int(input())

                if n3 == GUSSING_NUMBER:

                    print(
                        GREEN +
                        f"✅ Your Attempt {i} Guessing Was Correct!" +
                        RESET
                    )

                    SCORE += 50

                    break

                else:

                    print(
                        RED +
                        f"❌ Your Attempt {i} Was Fail!" +
                        RESET
                    )

                    # -------------------------------
                    # HIGH / LOW HINT
                    # -------------------------------

                    if n3 < GUSSING_NUMBER:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO LOW!" +
                            RESET
                        )

                    else:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO HIGH!" +
                            RESET
                        )

                    loss_point = SCORE // 3
                    SCORE = SCORE - loss_point

                print(MAGENTA + f"⭐ Score : {SCORE}" + RESET)


            # ------------------------------------------------
            #                    ATTEMPT 4
            # ------------------------------------------------

            elif i == 4:

                print(CYAN + "\n────────────────────────────────────────────────────────" + RESET)

                print(
                    YELLOW +
                    f"🎯 Enter The Number For Attempt {i}" +
                    RESET
                )

                n4 = int(input())

                if n4 == GUSSING_NUMBER:

                    print(
                        GREEN +
                        f"✅ Your Attempt {i} Guessing Was Correct!" +
                        RESET
                    )
                    SCORE += 30
                    break

                else:

                    print(
                        RED +
                        f"❌ Your Attempt {i} Was Fail!" +
                        RESET
                    )

                    # -------------------------------
                    # HIGH / LOW HINT
                    # -------------------------------

                    if n4 < GUSSING_NUMBER:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO LOW!" +
                            RESET
                        )

                    else:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO HIGH!" +
                            RESET
                        )

                    loss_point = SCORE // 2
                    SCORE = SCORE - loss_point

                print(MAGENTA + f"⭐ Score : {SCORE}" + RESET)

            # ------------------------------------------------
            #                    ATTEMPT 5
            # ------------------------------------------------

            elif i == 5:

                print(CYAN + "\n────────────────────────────────────────────────────────" + RESET)

                print(
                    YELLOW +
                    f"🎯 Enter The Number For Attempt {i}" +
                    RESET
                )

                n5 = int(input())

                if n5 == GUSSING_NUMBER:

                    print(
                        GREEN +
                        f"✅ Your Attempt {i} Guessing Was Correct!" +
                        RESET
                    )
                    SCORE += 20
                    break

                else:

                    print(
                        RED +
                        f"❌ Your Attempt {i} Was Fail!" +
                        RESET
                    )

                    # -------------------------------
                    # HIGH / LOW HINT
                    # -------------------------------

                    if n5 < GUSSING_NUMBER:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO LOW!" +
                            RESET
                        )

                    else:

                        print(
                            YELLOW +
                            "💡 Hint: Your Number Is TOO HIGH!" +
                            RESET
                        )

        
                    loss_point = SCORE // 1
                    SCORE = SCORE - loss_point

                print(MAGENTA + f"⭐ Score : {SCORE}" + RESET)

        # ====================================================
        #                    FINAL RESULT
        # ====================================================

        print(CYAN + "\n╔══════════════════════════════════════════════════════╗" + RESET)
        print(CYAN + "║                  🏆 GAME RESULT                      ║" + RESET)
        print(CYAN + "╚══════════════════════════════════════════════════════╝" + RESET)

        print(
            MAGENTA +
            f"🎯 Your Guessing Number : {GUSSING_NUMBER}" +
            RESET
        )

        print(
            MAGENTA +
            f"⭐ Your Score : {SCORE}" +
            RESET
        )

        if SCORE <= 20:

            print(RED + BOLD)
            print("💀 You Have Lost The Game")
            print(RESET)

        elif SCORE > 20:

            print(GREEN + BOLD)
            print("🎉 Congratulations! You Won The Game")
            print(RESET)

        print(CYAN + "\n--------------- End The Game -----------------------" + RESET)


    # ========================================================
    #                    DON'T START
    # ========================================================

    elif inp1 == "N" or inp1 == "n":

        print(RED + "\nGame Over! Thank You 👋" + RESET)

        break


    # ========================================================
    #                    CONTINUE
    # ========================================================

    print(YELLOW + "\nDo You Want Continue Play [Y/N] : " + RESET)

    inp2 = input()

    if inp2 == "Y" or inp2 == "y":

        pass

    elif inp2 == "N" or inp2 == "n":

        print(GREEN + "\n🎮 Game Over! Thank You For Playing!" + RESET)

        break