#coin flip or dice game
def coin_flip():
    right = 0
    wrong = 0
    play = "Yes"
    import random
    while play == "Yes" or play == "yes":
      answer = input("Head or Tail?")  
      result = random.randint(0, 1)
      if result == 0 and answer == "Head":
        right = right + 1
        print("Head, you won! You won "+str(right)+ "times and you lost "+str(wrong)+"times")
      if result == 0 and answer == "Tail":
        wrong = wrong + 1
        print("Head, you lost! You won "+str(right)+ "times and you lost "+str(wrong)+"times")
      if result == 1 and answer == "Head":
        wrong = wrong + 1
        print("Tail, you lost! You won "+str(right)+ "times and you lost "+str(wrong)+"times")
      if result == 1 and answer == "Tail":
        right = right + 1
        print("Tail, you won! You won "+str(right)+ "times and you lost "+str(wrong)+"times")
      play = input("Do you want to play again?")

def roll_dice():
    right = 0
    wrong = 0
    play = "Yes"
    import random
    while play == "Yes" or play == "yes":
        answer = int(input("choose your number from 1 to 6"))
        result = random.randint(0, 6)
        if answer > 6:
            print("Your number should be from 1 to 6")
        for i in range(6):
            if result == i:
                right = right + 1
                print("You won! You won "+str(right)+ "times and you lost "+str(wrong)+"times")
                break
            else:
                wrong = wrong + 1
                print("You lost! You won "+str(right)+ "times and you lost "+str(wrong)+"times")
                break
        play = input("Do you want to play again?")


game_choice = input("do you want to play: a)coin flip or b)roll dice?")
if game_choice == "a":
    coin_flip()
else:
    roll_dice()

