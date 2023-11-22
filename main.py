import json
import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound
import os
import base64
from requests import post
import requests
import time
import sys
import webbrowser
import pyttsx3
import wikipedia
import pyjokes

def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")

def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        speech("Hi Boss")
#        removes old audio out of mp3 file
        os.remove('./sounds/output.mp3')
        print("Listening.....")
        audio = recorder.listen(source)
        intext = recorder.recognize_google(audio)
        intext = intext.lower()
    return intext

intext = get_audio()
print(intext)
if "on youtube" in intext:
        video = intext.replace("on youtube", '')
        speech("Playing " + intext)
        pywhatkit.playonyt(intext)
elif "joke" in intext:
        speech(pyjokes.get_joke())
elif "google" in intext:
        search = intext.replace("google", '')
        speech("Here is what I found")
        pywhatkit.search(intext)
elif "weather" in intext:
    try:
        city = input('input the city name ')
        print(city)

        print('Displaying Weather report for: ' + city)

        url = 'https://wttr.in/{}'.format(city)
        res = requests.get(url)
        print(res.text)
        speech("Here is the Weather")
    except:
        print("Error")
elif "time" in intext:
    t = time.localtime()
    current_time = time.strftime("%I:%M %p", t)
    speech('Current time is ' + current_time)
elif "who is" in intext:
    person = intext.replace("who is", '')
    info = wikipedia.summary(person, 1)
    print(info)
    speech(info)
else:
    speech("Please say that again.")














