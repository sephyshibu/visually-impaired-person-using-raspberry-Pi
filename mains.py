import speech_recognition as sr
import pyttsx3 as p
import wikipedia
from gtts import gTTS
import playsound
import wolframalpha
import requests, json

import cv2
import numpy as np
#from infos import *
#import face_recognition
import random
#from infos import *
import os
r1 = sr.Recognizer()
#engine = p.init()
text1 = "hi...my name is tintu mone"
language = 'en'
output1 = gTTS(text=text1,lang=language,slow=False)
output11= "output1.mp3"
output1.save(output11)
playsound.playsound(output11)
os.remove(output11)
with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    print("say something...")
    audio=r1.listen(source)

    try:
        text1=r1.recognize_google(audio)
        print(text1)
    except sr.UnknownValueError:
        print("donot understand")
    except sr.RequestError as e:
        print("blblblaa")
print("lala")
text2 = "what do u want me to do?"
language = 'en'
output2 = gTTS(text=text2,lang=language,slow=False)
output22 = "output2.mp3"
output2.save(output22)
playsound.playsound(output22)
os.remove(output22)
#os.system("start output2.mp3")
print("Instructions please  :")


#giving instruction
r2=sr.Recognizer()
with sr.Microphone() as source1:
    r2.adjust_for_ambient_noise(source1)
    audio2=r2.listen(source1)
    print("kallooo")
    try:
        instructions=r2.recognize_google(audio2)
        print(instructions)
    except sr.UnknownValueError:
        print("donot understand")
    except sr.RequestError as e:
        print("blblblaa")


#instructions
print("keyri")
while True:
    r3 =sr.Recognizer()
    if "wikipedia" in instructions:
        def speechtext():
            r1 = sr.Recognizer()
            mic = sr.Microphone()
                    #engine = p.init()
            text3 = "What do u want to know please ask??"
            language = 'en'
            output3 = gTTS(text=text3, lang=language, slow=False)
            output33='output3.mp3'
            output3.save(output33)
            playsound.playsound(output33)
            os.remove(output33)

            with mic as source:
                r1.adjust_for_ambient_noise(source)
                        #engine.say("Start")
                audio = r1.listen(source)

                try:
                    user = r1.recognize_google(audio)
                    return user

                except sr.UnknownValueError:
                    talkback("Sorry i don't get you, can you come again")
                        #speechtext()
                        #return user
                except sr.RequestError:
                            # Connection/ request error handling
                    print("Sorry it seems you are offline.")

        def wiki(x):
            tokenized = x.split()
            try:

                x = wikipedia.summary(tokenized, sentences=2)
                print(x)
                talkback(x)
            except ConnectionError:
                talkback("Sorry I'm having a problem connecting")


            except Exception as e:
                print(e)

        def talkback(x):
            language='en'
            output4 = gTTS(text=x,lang=language, slow=False)
            output44='output4.mp3'
            output4.save(output44)
            playsound.playsound(output44)
            os.remove(output44)


        print("startingwiki.....")
        while True:
            user = speechtext()
            if str(user) == "quit":
                exit(0)
            else:
                if user is not None:
                    wiki(user)
                else:
                    exit(0)


    r5 = sr.Recognizer()
    if "want to search in deep" in instructions:
        def wool(x):
            appid = "6YRARE-VJL6RLL3PA"
            client = wolframalpha.Client(appid)
            try:
                res = client.query(x)
                answer = next(res.results).text
                talkback(answer)
            except ConnectionError:
                talkback("Sorry I'm having a problem connecting")


            except Exception as e:
                print(e)
        def speechtext():
            r1 = sr.Recognizer()
            mic = sr.Microphone()
                    #engine = p.init()
            text5 = "What do u want to know please ask??"
            language = 'en'
            output5 = gTTS(text=text5, lang=language, slow=False)
            output55='output5.mp3'
            output5.save(output55)
            playsound.playsound(output55)
            os.remove(output55)

            with mic as source:
                r1.adjust_for_ambient_noise(source)
                        #engine.say("Start")
                audio = r1.listen(source)
                print(audio)
                try:
                    user = r1.recognize_google(audio)

                    return user

                except sr.UnknownValueError:
                    talkback("Sorry i don't get you, can you come again")
                        #speechtext()
                        #return user
                except sr.RequestError:
                            # Connection/ request error handling
                    print("Sorry it seems you are offline.")
        def talkback(x):
            language='en'
            output6 = gTTS(text=x,lang=language, slow=False)
            output66='output6.mp3'
            output6.save(output66)
            playsound.playsound(output66)
            os.remove(output66)

        print("startingwolframe.....")
        while True:
                # bot = wiks()
            user = speechtext()
            if str(user) == "quit":
                exit(0)
            else:
                if user is not None:
                    wool(user)
                else:
                    exit(0)

    r4 = sr.Recognizer()
    if "weather" in instructions:
        #print("gulugulu")
        def weather(z):
            apikey = "a17e89ac8e14743c038bdd4780b92e99"
            baseurl = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = baseurl + "appid=" + apikey + "&q=" + z
            response = requests.get(complete_url)
            #weather_data = requests.get(Final_url).json()
            x = response.json()
            print(x)
            if x["cod"] != "404":
                y = x['main']
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                text7 = "current temperature is{},current pressure is{}, current humididty is{},description of" \
                        " weather is {}".format(current_temperature,current_pressure,current_humidiy,weather_description)
                language = 'en'
                output7 = gTTS(text=text7, lang=language, slow=False)
                output77 = 'output7.mp3'
                output7.save(output77)
                playsound.playsound(output77)
                os.remove(output77)
                if weather_description=="haze" or "rain":
                    text10 = "please take your umbrella "
                    language = 'en'
                    output10 = gTTS(text=text10, lang=language, slow=False)
                    output100 = 'output10.mp3'
                    output10.save(output100)
                    playsound.playsound(output100)
                    os.remove(output100)

        def speechtext():
            r1 = sr.Recognizer()
            mic = sr.Microphone()
            # engine = p.init()
            text9 = "please name the city"
            language = 'en'
            output9 = gTTS(text=text9, lang=language, slow=False)
            output99 = 'output9.mp3'
            output9.save(output99)
            playsound.playsound(output99)
            os.remove(output99)

            with mic as source:
                r1.adjust_for_ambient_noise(source)
                # engine.say("Start")
                audio = r1.listen(source)

                try:
                    user = r1.recognize_google(audio)
                    return user

                except sr.UnknownValueError:
                    talkback("Sorry i don't get you, can you come again")
                    # speechtext()
                    # return user
                except sr.RequestError:
                    # Connection/ request error handling
                    print("Sorry it seems you are offline.")


        def talkback(x):
            language = 'en'
            output8 = gTTS(text=x, lang=language, slow=False)
            output88 = 'output6.mp3'
            output8.save(output88)
            playsound.playsound(output88)
            os.remove(output88)


        print("startingweather.....")
        while True:
            # bot = wiks()
            user = speechtext()

            if str(user) == "quit":
                exit(0)
            else:
                if user is not None:
                    weather(user)
                else:
                    exit(0)
    else:
        text11 = "instruction donot understand"
        language = 'en'
        output11 = gTTS(text=text11, lang=language, slow=False)
        output111 = 'output11.mp3'
        output11.save(output111)
        playsound.playsound(output111)
        os.remove(output111)
        exit(0)













