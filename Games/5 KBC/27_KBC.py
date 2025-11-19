import pyttsx3
import time


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

print("kbc day 27")

# craete a program that is capabe of displaying questions to the usesrs like kbc

# 1)use list datatypes to store questions and answers
# 2)display the final amount is taking after playng the game


price=[10, 1000, 25000 ,100000,1000000 , 1500000 , 5000000 , 10000000, 30000000 ,50000000,70000000 ]
money_won=0


print("Choose the correct options else , for life line enter X ...\n")
speak_test="Choose the correct options else , for life line enter X ..."
speak(speak_test)

question =[
    ["1.What is the capital of France? \n","A) London", "B) Berlin","C) Paris","D) Rome" ,"C","C) Paris"],

    ["\n2.Which planet is known as the \"Red Planet\"? \n", "A) Venus", "B) Mars","C) Jupiter","D) Saturn","B", "B) Mars"],

    ["\n3.What is the largest mammal in the world? \n","A) Elephant","B) Blue Whale","C) Giraffe","D) Gorilla","B","B) Blue Whale"],
    
    ["\n4.Who wrote \"Romeo and Juliet\"? \n","A) Charles Dickens" ,"B) William Shakespeare","C) Jane Austen","D) Mark Twain","B","B) William Shakespeare"],

    ["\n5.In which year did the United States declare its independence?","A) 1765","B) 1776","C) 1789","D) 1801","B","B) 1776"],

    ["\n6.What is the chemical symbol for gold?" ,"A) Au","B) Ag","C) Fe","D) Hg","A","A) Au"],

    ["\n7.Who developed the theory of relativity?","A) Isaac Newton","B) Albert Einstein","C) Galileo Galilei","D) Stephen Hawking","B","B) Albert Einstein"],

    ["\n8.What is the capital of Bhutan?","A) Thimphu","B) Kathmandu","C) Colombo","D) Ulaanbaatar","A","A) Thimphu"],

    ["\n9.Which element has the chemical symbol \"I\"?","A) Iodine","B) Iron","C) Indium","D) Iridium","A","A) Iodine"],

    ["\n10.Who painted the Mona Lisa?","A) Michelangelo","B) Leonardo da Vinci","C) Vincent van Gogh","D) Pablo Picasso","B","B) Leonardo da Vinci"],

    ["\n11.What is the speed of light in a vacuum?","A) 300,000 km/s","B) 500,000 km/s","C) 700,000 km/s","D) 1,000,000 km/s","A","A) 300,000 km/s"],

    ["\n12.Who wrote the play \"Hamlet\"?","A) Christopher Marlowe","B) William Wordsworth","C) William Shakespeare","D) John Milton","C","C) William Shakespeare"]


]


count_money=0
money_won=0
#function to count scores and call life line
def quiz_scores(option):
    global count_money
    global money_won
    global speak_test
    if(option==emlement[5]  or option=="right_ans"):
        print("Sahi Jawab"," money won till now is ",price[count_money])
        if(option=="right_ans"):
            print("Right answer is: ",emlement[6])
        speak_test="Sahi Jawab "
        speak(speak_test)
        
        money_won=price[count_money]
        count_money=count_money+1
        if(count_money==11):
            print("congrotulations you are CrorePatiiiiiiiii.........")
            
            speak_test="congrotulations you are CrorePatiiiiiiiii........."
            speak(speak_test)
            return False
    elif(option=="change"):
        print("Right answer is: ",emlement[6])
    else:
        print("Thnk you for playing the game")
        speak_test="Thnk you for playing the game"
        speak(speak_test)
        print("Total mOney won is rs :",money_won)
        return False
    
life1=True 
life2=True 
life3=True 
life4=True 
lifeline_counter=0



#finction for lifeline
def life_line():
    global life1
    global life2
    global life3
    global life4
     #match case
    if(life1): 
        print("     A)50-50")
    if(life2):
        print("     B)change Questions")
    if(life3):
        print("     C)Phone on friend")
    if(life4):
        print("     D)Audience poll")
    global speak_test
    speak_test="choose options"
    speak(speak_test)
    
    x=input("Choose options :")
    
    match x:
        case "A": 
            if(life1):
                life1=False  
                global lifeline_counter
                lifeline_counter=lifeline_counter+1
                print(emlement[1]) 
                print(emlement[6])
            
                x=input("Enter option:") 
                quiz_scores(x)
                
                        
            else:
                print("lifeline 50-50 used ")
                life_line()
        case "B":
            if(life2):
                life2=False
                
                lifeline_counter=lifeline_counter+1
                quiz_scores("change")
            else:
                print("lifeline change questions is used")
                life_line()
        case "C":
            if(life3):
                life3=False
                
                lifeline_counter=lifeline_counter+1
                quiz_scores("right_ans")
            else:
                print("life line phone on friend used ")
                life_line()
        case "D":
            if(life4):
                life4=False
                
                lifeline_counter=lifeline_counter+1
                quiz_scores("right_ans")
            else:
                print("life line Audience poll used ")
                life_line()

        case _:
            print("Invalid option Please try again")
            life_line()

        
#check answers function
def answers_loop(x):
    
    
    global result
    match x:
        case "A":
            result=quiz_scores("A")
        case "B":
            result=quiz_scores("B")
        case "C":
            result=quiz_scores("C")
        case "D":
            result=quiz_scores("D")
        case "X":
            
            
            if(lifeline_counter !=4):
                result=life_line()
            else:
                print("All life line has been used.")
                print("To QUIET Game Enter Q. , C to continue...")
                end_lifeline=input()
                if(end_lifeline=="Q"):
                    result=quiz_scores("Q")
                if(end_lifeline=="C"):
                    # Repeat the current row
                    for ans in emlement[0:5]:
                        print(ans)
                        speak(ans)
                    #match case 
                    speak_test="Enter Option"
                    speak(speak_test)
                    x=input("Enter option:")
                    answers_loop(x) #------------ call to print the current loop again
        case _:
            result=quiz_scores("WRONG ANS")






#loops to print questions and take answer input 
for emlement in question:    
    for ans in emlement[0:5]:
        print(ans)
        speak(ans)
        #match case 
    speak_test="Enter Option"
    speak(speak_test)
    x=input("Enter option:")
    seconds =time.strftime('%S')
    print (seconds)
    answers_loop(x)#------------ call to print the current loop again
    
    if(result==False):
        break
            

        


    






    

