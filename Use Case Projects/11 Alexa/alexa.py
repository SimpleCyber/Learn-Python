import speech_recognition as sr
import pyttsx3

listner = sr.Recognizer()
engine = pyttsx3.init()
engine.say('I am cogno a.i...')
engine.say('How i can help u sir...')
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('Listening....')
        voice = listner.listen(source)
        command = listner.recognize_google_cloud(voice)
        command = command.lower()
        if 'cogno' in command:

            print(command)
except:
    pass