import pyttsx3
import datetime as d
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(d.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    speak("I am Kelly!, how may I help you?")


def takecommand():
    """It takes microphone imput from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please......")
        return "None"
    return query

if __name__ == "__main__":
    # speak("Atif Salam is a good boy")
    wishme()
    query = takecommand().lower()
    # Logic for searching tasks based on query

    if "wikipedia" in query:
        speak("searching wikipedia....")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)

    elif "open youtube" in query:
        webbrowser.open("youtube.com")


