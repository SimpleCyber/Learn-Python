print("Welcome to my computer quiz !")


if input("Do u want to play my quiz 🐼").lower() == "yes":
    score = 0

    if input("Full form of cpu :").lower() == "central processing unit":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

else:
    print("Nikal Ja ***#**##")


print("Your score is 🤔"+ str(score) +"out of 1.....")