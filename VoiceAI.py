# author: @shival_gupta

# This program is a virtual assitant (example of simple AI without machine learning) It will listen to you and do accordingly
## It will begin with wishing you 'Good Morning / Afternoon / Evening' according to the time of the day
## and then introducing herself as the name of voice 'Zira' 
## then the program will start listening to your default microphone 
## it will store your voice and then convert it into text, and will do what you ask her to 
## Try saying: 'who's your father', 'what's the time', 'search for <---> on wikipedia', 'change to male voice', 'open youtube', 
## 'meow', 'open google', 'open stackoverflow', ... you can even add more to this, just add another {elif} in the end of program


# Run these in terminal or powershell in order to run this program:
# for Mac users replace 'pip' by 'pip3'
'''
pip install pyttsx3
pip install pipwin
pipwin install pyaudio
pip install speechRecognition
pip install wikipedia
'''

# importing libraries aka modules
import random                       # Generates the random output(s)
import pyttsx3                      # Text to speech conversion library
import datetime                     # Gets the time from the system
import speech_recognition as sr     # Library for performing speech recognition, with support for several engines and APIs, online and offline
import wikipedia                    # Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia
import webbrowser                   # Convenient web-browser controller
import os                           # Library full of functions for interacting with the operating system
import smtplib                      # Helps sending the mail through SMPT (Simple Mail Transfer Protocol)
import sys

# Setting up the voice engine and the voice to be used for output
# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init('sapi5')              # SAPI5 is Microsoft Speech API
voices = engine.getProperty('voices')       # Get details of the voices already present in the system
v = 1      # set default index value as 1, try v as 0, 2 or 3, 0 and 1 works in most cases
voiceName = 'bot'

def setVoice(x):
    global v, voiceName
    v = x
    engine.setProperty('voice', voices[v].id)   # Changing the voice to the index 'v'
    voiceName = (((voices[v].name).split())[1]) # returns 2nd word, e.g. 'Zira' from 'Microsoft's Zira'
setVoice(v)

# Speak the text and then waits
def speak(text):
    # print what bot said:
    print(f'{voiceName}: %s' % text)
    # passed text to be spoken
    engine.say(text)
    # run and wait method, it processes the voice commands
    engine.runAndWait()

# Gets voice input from the user and returns the query as string
def inputVoice():
    insist = ["who's your father", "what's the time", 'tell me about Shahrukh khan on wikipedia', 'change to male voice', 'open youtube', 'meow', 'open google', 'open stackoverflow']
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f'\n{voiceName}: Listening...')
        print(f"Try saying '{str(random.choice(insist))}'")
        # r.pause_threshold = 1
        try:
            audio = r.listen(source)
        except Exception as e:
            print(e)
            speak("Sorry, I'm having trouble with your mic")
            speak('Fix it, and try again')
    try:
        # print(f'\n{voiceName}: Recognizing...')
        query = r.recognize_google(audio)
        print(f'\nUser: {query}')
    except Exception as e:
        print(e)
        print('Pardon, Say that again please')
        return 'None'
    return query

# Wishes 'Good Morning / Afternoon / Evening' according to the time of the day
def wishMe():
    currentTime = int(datetime.datetime.now().hour)    # gets the current time from systenm in hours, ranging from [0-23]
    if currentTime<12:              # will say 'Good Morning!' to the user, if current time is between [0-11]
        speak('Good Morning!')
    elif currentTime<18:            # will say 'Good Afternoon!' to the user, if current time is between [12-17]
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')      # will say 'Good Evening!' to the user, if current time is between [18-23]
    
    speak("I am %s. What can I do for you?" % voiceName)

# Sends email with content to recipient
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# Logic begins here
# Main Function
if __name__ == '__main__':
    print()
    wishMe()
    while True:
        query = inputVoice().lower()
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

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'D:\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query or 'open vs code' in query:
            speak('Opening Code')
            os.system('cmd /c "code"')

        elif 'email to recipient' in query:
            try:
                speak("What should I say?")
                content = inputVoice()
                to = "recipientEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")
        
        elif 'meow' in query:
            n = query.split().count('meow') + random.choice([0, 1, 2])
            if n>2: n+=2
            meow = 'meow'
            for i in range(n):
                if i == n-1: meow += f"{random.choice(['?', '!'])}"
                elif i == 0: meow += f"{random.choice(['-', ', '])}" + 'meow'
                elif i == 1: meow = 'meow, meow'
                elif i > 2: meow += f"{random.choice([' ', ', ', '-'])}" + 'meow'
                # meow += 'meow' + f'{random.choice(l)}'
            speak(meow)
        
        elif 'lalla' in query:
            speak('do you mean Yash Lulla?')
            if inputVoice().lower() == 'yes':
                webbrowser.open('instagram.com/yashlulla08')
        
        elif 'subhashis' in query:
            speak('do you mean Subhashis pattanaik?')
            if inputVoice().lower() == 'yes':
                webbrowser.open('instagram.com/_subhashis')
        
        elif 'your father' in query or 'made you' in query or 'your author' in query:
            speak('Shival Gupta! \n He made me in 2022')
            speak('Would you like to visit his instagram?')
            if inputVoice().lower() == 'yes':
                webbrowser.open('instagram.com/shival_gupta')
        
        elif 'female voice' in query:
            if v == 0:
                setVoice(1)
                speak("Hi, I am %s. What can I do for you?" % (((voices[v].name).split())[1]))
            else:
                speak("Rubbish! Do I sound like a boy to you!?")
                speak("I'm a girl")

        elif 'male voice' in query:
            if v == 1:
                setVoice(0)
                speak("Hi, I am %s. What can I do for you?" % (((voices[v].name).split())[1]))
            else:
                speak("Rubbish! Do I sound like a girl to you!!")
                speak("I'm a boy")
        
        # print()