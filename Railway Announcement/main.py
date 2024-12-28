import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename):
    '''Take text and mp3 file and'''
    mytext = str(text)
    language = "hi"
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    '''Return pydub audio segment'''
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    '''Create some part from mp3 file'''
    audio = AudioSegment.from_mp3("railway.mp3")
    # 1 - Generate dihan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 3 - Generate say chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 5 - Generate kay rastay
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 7 - Generate ko jaane wali gaadi
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 9 - Generate khuch hi samay main platform
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 11 - Generate per arahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    '''Take from xlsx file'''
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from city
        textToSpeech(item['from'], "2_hindi.mp3")

        # 4 - Generate via City
        textToSpeech(item['via'], "4_hindi.mp3")

        # 6 - Generate to city
        textToSpeech(item['to'], "6_hindi.mp3")

        # 8 - Generate train number and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10 - Generate Platform number
        textToSpeech(item['platform'], "10_hindi.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")        

if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement")
    generateAnnouncement("announce.xlsx")

