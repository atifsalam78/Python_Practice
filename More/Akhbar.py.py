import requests
import json
from pprint import pprint
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == "__main__":
    speak("News for today")
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8e9e0b4fc17f49eeb1bc790352ccf965"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict["articles"]
    pprint(len(arts))
    for index, article in enumerate(arts):        
        speak("according to" + article["author"])
        speak(article["title"])
        if index <= len(arts):
            speak("moving on to the next news, listen carefully")
        else:
            speak("Thanks for listening")