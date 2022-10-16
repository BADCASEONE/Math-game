def gameQuest():
    a = randint(0, 90)
    b = randint(0, 90)
    print()
    print(f"How much {a} + {b} ?")
    x = int(input("Enter your password! ----> "))
    if x == a+b:
        print("win! :)")
    else:
        print("lose! :(")
    gameQuest()


gameQuest()
