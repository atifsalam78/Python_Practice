from gtts import gTTS
from io import BytesIO
import pygame
import time
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import  os

def speak(text, language='hi'):
	mp3_fo = BytesIO()
	tts = gTTS(text, lang=language)
	tts.write_to_fp(mp3_fo)
	return mp3_fo

def speechSound(sound):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound, 'mp3')
    pygame.mixer.music.play()
    time.sleep(5)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >- 0 and hour < 12:
        sound = speak("good morning Atif!")
        speechSound(sound)
    
    elif hour >= 12 and hour < 15:
        sound = speak("good afternoon Atif!")
        speechSound(sound)

    else:
        sound = speak("good evening Atif")
        speechSound(sound)

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
                sound = speak('Searching Wikipedia...')
                speechSound(sound)
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                print(results)
                sound = speak("According to Wikipedia")
                speechSound(sound)
                sound = speak(results)
                speechSound(sound)

                
            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                sound = speak(f"Sir, the time is {strTime}")
                speechSound(sound)

            elif 'open code' in query:
                codePath = "C:\\Users\\atif.salam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'exit' in query:
                sound = speak('Have a nice day good bye atif')
                speechSound(sound)
                exit()

    else:
        print("Not saying")
        exit()