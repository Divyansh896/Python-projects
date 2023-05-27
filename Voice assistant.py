import speech_recognition as sr
from datetime import date
import pyttsx3
import os
import datetime
import time
import wikipedia
import socket
import random
import smtplib
from email.message import EmailMessage
import pyautogui



engine=pyttsx3.init('sapi5') # microsoft speech api (SAPI5)is the technology for voice recognition and synthesis provided by microsoft
voice=engine.getProperty('voices')
engine.setProperty('rate',190)

try:
    engine.setProperty('voice',voice[1].id)

except:
    engine.setProperty('voice',voice[0].id)






def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def internet():
    # Program will check if internet is connected
    try:
        socket.create_connection(('Google.com',80))
        print('connected to internet')
        speak("connected to internet")
        import pywhatkit as kit
        global kit


    except OSError:
        print("no internet connection")
        speak("no internet connection, my functions will not work, sorry.")
        quit()




def wishme():
    # program will wish according to the time

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('good morning sir ')
        #playsound.playsound("introduction.mp3")

    elif hour >= 12 and hour < 22:
        speak("good afternoon sir")
        #playsound.playsound("introduction.mp3")


    else:
        speak('good evening sir ')
        #playsound.playsound("introduction.mp3")


    speak(" i am jarvis , how may i help you!")






def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300 # Represents the energy level threshold for sounds.
        #Values below this threshold are considered silence, and values above this
        # threshold are considered speech

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in' )
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



def read_pdf():
    pass

# to send email
def send_email(receiver,subject,body):
    server = smtplib.SMTP('smtp.gmail.com',587 )
    server.starttls()
    server.login('divyansh3838@gmail.com', 'divyansh008')
    email=EmailMessage()
    email['from']='divyansh3838@gmail.com'
    email['To']=receiver
    email['subject']=subject
    email.set_content(body)
    server.send_message(email)

def get_email_info():
    speak("to whom i send mail")
    name=takeCommand().lower()
    receiver=email_list[name]
    print(receiver)
    speak('what is the  subject sir')
    subject=takeCommand().lower()
    speak('tell me the body of the mail.')
    body=takeCommand().lower()
    send_email(receiver,subject,body)



# commands that program will execute

def commands():


        query=takeCommand().lower()

        if "open google" in query:
            kit.search("google")

        elif 'play video on youtube' in query:
            speak("what should i play")
            kit.playonyt(takeCommand().lower())
            speak("opening youtube")

        elif "pause video" in query :
            pyautogui.press("space")

        elif 'forward video' in query :
            pyautogui.press("right")

        elif "volume up" in query:
            pyautogui.press("volumeup", 6, 0.5)

        elif "volume down" in query :
            pyautogui.press("volumedown", 6, 0.5)

        elif ' open chrome' in query:
            os.startfile(os.path.join("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            speak("opening chrome")

        elif 'play music' in query:
            songs = os.listdir('F:\\songs')
            os.startfile(os.path.join('F:\\songs', random.choice(songs)))
            speak("playing music")

        elif 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=5)
            print(result)
            speak(result)

        elif "send a message"in query:
            x = int(time.strftime("%H"))
            y = int(time.strftime("%M"))
            speak("what should i send sir")

            kit.sendwhatmsg("+917658035218", takeCommand().lower(), 4, 47, wait_time=10)
            speak("message send successfully ")

        elif 'what is the time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif'what is the date' in query:
            x = date.today()
            speak(f"sir the date is {x}")

        elif'send email'in query:
            get_email_info()


        elif 'what is temperature in phagwara' in query:
            pass


        elif 'exit' in query:
            speak("exiting sir have a nice day")
            quit()

if __name__ == '__main__':

    wishme()
    internet()
    while True:
        commands()

'''
 #   playsound.playsound('Jarvis Startup .mp3')
    while True:
        query=takeCommand().lower()
        if "   " in query:
            query=takeCommand().lower()
        if "jarvis" or "javed" in query:
            playsound.playsound("sound.mp3") or speak('yes sir')
            functions()
          '''

