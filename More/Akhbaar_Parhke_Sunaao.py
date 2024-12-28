import requests
import json


def speak(str):
    """Taking string as an argument and convert into audio"""
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)


if __name__ == '__main__':

    print("News for today... Let's begin")
    url = "https://newsapi.org/v2/top-headlines?country=gb&apiKey=8e9e0b4fc17f49eeb1bc790352ccf965"
    news_pull = requests.get(url).text
    news_dict = json.loads(news_pull)
    arts = news_dict["articles"]
    for article in arts:
        print(article["title"])
        speak(article["title"])
        speak("Moving on to the next news.....")
    speak("Thanks for Listening")
