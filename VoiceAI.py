# author: @shival_gupta


# This program is a virtual assitant (example of simple AI without machine learning) It will listen to you and do accordingly
## It will begin with wishing you 'Good Morning / Afternoon / Evening' according to the time of the day
## and then introducing herself as the name of voice 'Zira' 
## then the program will start listening to your default microphone 
## it will store your voice and then convert it into text, and will do what you ask her to 
## Try saying: 'who's your father', 'what's the time', 'search for <---> on wikipedia', 'change to male voice', 'open youtube', 
## 'meow', 'open google', 'open stackoverflow', ... you can even add more to this, just add another {elif} in the end of program


# Run these in terminal or powershell in order to run this program:
'''
pip install pyttsx3
pip install pipwin
pipwin install pyaudio
pip install speechRecognition
pip install wikipedia
'''

import random
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
v = 1
engine.setProperty('voice', voices[v].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour<12:
        speak('Good Morning!')
    elif hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    
    speak("I am %s. What can I do for you?" % (((voices[v].name).split())[1]))

def takeCommand():
    l = ["who's your father", "what's the time", 'search for <---> on wikipedia', 'change to male voice', 'open youtube', 'meow', 'open google', 'open stackoverflow']
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        print(f'{random.choice(l)}')
        # r.pause_threshold = 1
        try:
            audio = r.listen(source)
        except Exception as e:
            print(e)
            speak("Sorry, I'm having trouble with your mic")
            speak('Fix it, and try again')
    try:
        print('Recognizing')
        query = r.recognize_google(audio)
        print(f'User said: {query}\n')
    except Exception as e:
        print(e)
        print('Say that again please...')
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        # query = 'Shahrukh khan on wikipedia'

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query.replace('Wikipedia', ''), sentences=1)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak('opening YouTube!')
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'D:\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query or 'open vs code' in query:
            speak('Opening Code')
            os.system('cmd /c "code"')

        elif 'email to recipient' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipientEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")
        
        elif 'meow' in query:
            l=[',','\.','!',':',';','?']
            speak(f'meow{random.choice(l)}'*(len(query.split())+(random.choice([0,1,2]))))
        
        elif 'lalla' in query:
            speak('do you mean Yash Lulla?')
            if takeCommand().lower() == 'yes':
                webbrowser.open('instagram.com/yashlulla08')
        
        elif 'subhashis' in query:
            speak('do you mean Subhashis pattanaik?')
            if takeCommand().lower() == 'yes':
                webbrowser.open('instagram.com/_subhashis')
        
        elif 'your father' in query:
            speak('Shival Gupta')
            speak('Would you like to visit his instagram?')
            if takeCommand().lower() == 'yes':
                webbrowser.open('instagram.com/shival_gupta')
        
        elif 'female voice' in query:
            v = 1
            engine.setProperty('voice', voices[v].id)
            speak("Hi, I am %s. What can I do for you?" % (((voices[v].name).split())[1]))

        elif 'male voice' in query:
            v = 0
            engine.setProperty('voice', voices[v].id)
            speak("Hey, I am %s. What can I do for you?" % (((voices[v].name).split())[1]))