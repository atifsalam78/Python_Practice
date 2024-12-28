# espeak "This is linus torvalds the creator of linux" -k28 -p58 -s140 -v f5
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import  os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
engine.setProperty('voice',voices[1])

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >- 0 and hour < 12:
        speak("good morning Atif!")
    elif hour >= 12 and hour < 15:
        speak("good afternoon Atif!")
    else:
        speak("good evening Atif!")

def takeCommand():
    '''Will takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening......")

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query


if __name__ == '__main__':
    query = takeCommand().lower()
    if "hello" in query:
        wishMe()
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\atif.salam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'exit' in query:
                exit()

    else:
        print("Not saying")
        exit()