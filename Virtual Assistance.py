# Allowing to take screenshot and automate tasks
import pyautogui as pg


# Voice Functionality
# Text to speech

import pyttsx3

engine = pyttsx3.init() #creating object
voices = engine.getProperty('voices')


# print(voices)
# Setting a voice
engine.setProperty('voice', voices[0].id)

# Setting voice speed of L
engine.setProperty('rate',175)

# Speak function 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

# Giving assisstance access to time
import datetime
import time

def wish_user():
    hour = int(datetime.datetime.now().hour)
    
    if hour>0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    
    else:
        speak("Good evening")

    speak("Welcome, I am Virtual assisstant , How can i Help.")


# listening functinality: So that he could hear

# Module to take input from microphone and convert that to string
import speech_recognition as sr

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("assisstant is Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')        
        print("User Said: ",query)
    
    
    except Exception as e:
        print(e)
        print("Say that again...")
        return "None"

    return query

# To access wikipedia stuff
import wikipedia

# Giving access to Web Browser
import webbrowser

# Giving access to system
import os




if __name__== "__main__":

    
    wish_user()
    
    while True:
        query = take_command().lower()
    
    #Enabling assisstance to execute task based on query
    

        # access wikipedia
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
        
        # allowing L to open websites 
        if "open youtube" in query:
            webbrowser.open("Youtube.com")
        
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        
        elif "open linkedin" in query:
            webbrowser.open("linkedin.com")
        
        elif "play music" in query:
 

            music_folder = "D:\\music"
            songs = os.listdir(music_folder)
            print(songs[0])

            os.startfile(music_folder + "\\" + songs[1])
        
        
        elif "the time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M")
            print(str_time)
            speak("The Time is " + str_time)

        elif "open code" in query:
            os.startfile("C:\\Users\\Akanksha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")
    
        # Allowing L to take screenshot
        elif "take screenshot" in query:
            screen_shot = pg.screenshot()
            screen_shot.save('my_screenshot.png')
        
        

        
        