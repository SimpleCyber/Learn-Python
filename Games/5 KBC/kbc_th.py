import tkinter as tk
import pyttsx3
import time

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Function to speak text using pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()


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


# Function to handle answer submission
def submit_answer():
    user_answer = answer_entry.get().strip().upper()
    answers_loop(user_answer)

# Function to handle lifeline usage
def use_lifeline(lifeline):
    if lifeline == "50-50":
        speak("Using 50-50 lifeline")
        # Implement 50-50 lifeline logic
    elif lifeline == "Change Question":
        speak("Changing the question")
        # Implement logic to change the question
    elif lifeline == "Phone a Friend":
        speak("Phoning a friend")
        # Implement logic to phone a friend
    elif lifeline == "Audience Poll":
        speak("Using audience poll")
        # Implement audience poll logic

# Initialize tkinter
root = tk.Tk()
root.title("KBC Game")

# Create GUI components
question_label = tk.Label(root, text="", wraplength=500)
question_label.pack()

options_label = tk.Label(root, text="")
options_label.pack()

answer_entry = tk.Entry(root)
answer_entry.pack()

submit_button = tk.Button(root, text="Submit Answer", command=submit_answer)
submit_button.pack()

lifeline_buttons = []
for lifeline_text in ["50-50", "Change Question", "Phone a Friend", "Audience Poll"]:
    lifeline_button = tk.Button(root, text=lifeline_text, command=lambda l=lifeline_text: use_lifeline(l))
    lifeline_button.pack()
    lifeline_buttons.append(lifeline_button)

# Initialize variables
current_question_index = 0

# Function to update the GUI with the current question
def update_question():
    global current_question_index
    question, options = question_list[current_question_index][0], question_list[current_question_index][1:5]
    question_label.config(text=question)
    options_label.config(text='\n'.join(options))
    speak(question)

# Start the game
update_question()

# Run the tkinter event loop
root.mainloop()
