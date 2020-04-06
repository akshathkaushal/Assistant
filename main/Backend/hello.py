import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

engine.setProperty('voice', voices[14].id)
engine.setProperty('rate', 140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Hello! This is python 3, talking to, Electron J S")

