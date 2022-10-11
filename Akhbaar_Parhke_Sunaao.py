# Akhbaar Parhke Sunaao
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

if __name__ == '__main__':
    print("News for today... Let's begin")
    url = "https://newsapi.org/v2/top-headlines?country=gb&apiKey=8e9e0b4fc17f49eeb1bc790352ccf965"
    news_pull = requests.get(url).text
    news_dict = json.loads(news_pull)
    # print(news_dict["articles"])
    arts = news_dict["articles"]        
    for article in arts:
        print(article["title"])
        print("Moving on to the next news.....")
    print("Thanks for Reading")