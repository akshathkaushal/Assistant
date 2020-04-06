import pyttsx3, datetime, pyaudio, sys
import speech_recognition as sr


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[14].id)
engine.setProperty('rate', 140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=3)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio)

    except sr.UnknownValueError:
        print('Say that again please.')
        return 'None'
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning sir.')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon sir.')
    else:
        speak('Good evening sir.')


if __name__ == "__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()
        speak(query)

        if query == 'exit':
            sys.exit()
