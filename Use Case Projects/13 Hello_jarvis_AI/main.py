import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

s="Hello I am Jarvis AI"
speaker.Speak(s)

def takeCommand():
    r = speaker.Recognizer()
    with speaker.Recognizer() as source:
        r.pause_thresh


