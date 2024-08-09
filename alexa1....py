# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:28:02 2022

@author: lenovo
"""

import pyttsx3
import speech_recognition as sr
import datetime
import screen_brightness_control as srcpipnever
import wikipedia
import webbrowser
import os
import smtplib
import phonenumbers
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alexa Sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 550
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
            speak("please enter password to access Alexa")
            Name = input("Enter Password : ")
            if Name == 'never':
                speak(' Welcome  Master..., Please tell me how may I help you')
                while True:
                        query = takeCommand().lower()
                        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                        if 'wikipedia' in query:
                            speak('Searching Wikipedia...')
                            query = query.replace("wikipedia", "")
                            results = wikipedia.summary(query, sentences=2)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)

                        elif 'open youtube' in query:
                            webbrowser.open("youtube.com")

                        elif 'open Facebook' in query:
                            webbrowser.open("facebook.com")

                        elif 'open google' in query:
                            webbrowser.open("google.com")

                        elif 'open stack overflow' in query:
                            webbrowser.open("stackoverflow.com")

                        elif 'play music' in query:
                            music_dir = 'C:\\Users\\SAI SUDEEP\\Music'
                            songs = os.listdir(music_dir)
                            print(songs)
                            os.startfile(os.path.join(music_dir, songs[0]))

                        elif 'the time' in query:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak(f"Sir, the time is {strTime}")

                        elif 'open code' in query:
                            codePath = "C:\\Program Files\\Sublime Text\\sublime_text.exe"
                            os.startfile(codePath)

                        elif 'stop' in query:
                            break


                        elif 'day brightness' in query:
                            src.fade_brightness(0)
                            src.fade_brightness(95, start=0)
                            speak("Brightness is adjusted  , enjoy the day screen light master")

                        elif 'night brightness' in query:
                            src.fade_brightness(0)
                            src.fade_brightness(25, start=0)
                            speak("Brightness is adjusted , Take care,yourself master")


                        elif 'current location' in query:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            city = data['city']
                            location = data['loc'].split(',')
                            latitude = location[0]
                            longitude = location[1]
                            print("Latitude : ", latitude)
                            speak("Latitude" + latitude)
                            print("Longitude : ", longitude)
                            speak("Longitude" + longitude)
                            print("City : ", city)
                            speak("City" + city)
