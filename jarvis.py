import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am happy assistant please tell me how may i help you")

def takecommand():
    '''takes microphone input and gives string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
    #print(e)

        print("say that again please...")
        return "None"

    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('devamithra.naresh2020@vitstudent.ac.in','Deva25052002$')
    server.sendmail('jithinmanoj353@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query=query.replace("wikipedia ","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
                music_dir='C:\\Users\\devam\\OneDrive\\Desktop\\songs'
                songs=os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codepath="C:\\Users\\devam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email' in query:
            try:
                speak("what should i say")
                content=takecommand()
                print(content)
                to="jithinmanoj353@gmail.com"
                sendEmail(to,content)
                speak("email has to been sent!")
            except Exception as e:
                #print(e)
                speak("not able to send the email")