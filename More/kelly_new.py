from gtts import gTTS
from io import BytesIO
import pygame
import time
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import  os
import platform
import cpuinfo
from bs4 import BeautifulSoup
import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def find_weather(city_name):
   city_name = city_name.replace(" ", "+")
 
   try:
       res = requests.get(
           f'https://www.google.com/search?q={city_name}&oq={city_name}&aqs=chrome.1.69i57j0i512j0i433i512j46i199i465i512j0i512l4j46i512j0i512.3636j1j15&sourceid=chrome&ie=UTF-8', headers=headers)
      
       print("Loading...")
 
       soup = BeautifulSoup(res.text, 'html.parser')
       location = soup.select('#wob_loc')[0].getText().strip()       
       info = soup.select('#wob_dc')[0].getText().strip()
       temperature = soup.select('#wob_tm')[0].getText().strip()  
       
       weather_info = (f"The current temperature for {location} is {temperature} °C and {info}")
       sound = speak(weather_info)
       speechSound(sound) 
   except:
       print("Please enter a valid city name")

uname = platform.uname()
def speak(text, language='en'):
	mp3_fo = BytesIO()
	tts = gTTS(text, lang=language, tld='co.in')
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
        sound = speak("good morning")
        speechSound(sound)
    
    elif hour >= 12 and hour < 15:
        sound = speak("good afternoon")
        speechSound(sound)

    else:
        sound = speak("good evening")
        speechSound(sound)

    sound = speak("how may I help you?")
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
                results = wikipedia.summary(query, sentences=2)
                print(results)
                sound = speak("According to Wikipedia")
                speechSound(sound)
                sound = speak(results)
                speechSound(sound)
                
            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%-I:%M:%p")
                sound = speak(f"the time is {strTime}")
                speechSound(sound)

            elif 'open code' in query:
                codePath = "C:\\Users\\atif.salam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            
            elif "system" in query:                
                sound = speak("what information you required from your system?")
                speechSound(sound)
                query = takeCommand().lower()

                if "operating" in query:
                    os_name = (f"you have {uname.system} operating system installed in your machine")
                    print(os_name)
                    sound = speak(os_name)
                    speechSound(sound)

                elif "processor" in query:
                    processor_name = (f"your machine have {cpuinfo.get_cpu_info()['brand_raw']} processor")
                    print(processor_name)
                    sound = speak(processor_name)
                    speechSound(sound)

                elif "release" in query:
                    os_release = (f"your operating system have release {uname.release}")
                    print(os_release)
                    sound = speak(os_release)
                    speechSound(sound)

                elif "version" in query:
                    os_version = (f"your operating system have {uname.version} version")
                    print(os_version)
                    sound = speak(os_version)
                    speechSound(sound)

                elif "complete" in query:
                    complete_info = (f"you have {uname.system} operating system {uname.version} version and {uname.release} installed in your {uname.machine} machine")
                    print(complete_info)
                    sound = speak(complete_info)
                    speechSound(sound)

            elif "weather" in query:
                sound = speak("For which city's weather you want to know?")
                speechSound(sound)
                query = takeCommand().lower()
                city_name = query
                city_name = city_name + " weather"
                find_weather(city_name)

            elif 'exit' in query:
                sound = speak("Have a nice day good bye")
                speechSound(sound)
                exit()
    else:
        print("Not saying")
        exit()