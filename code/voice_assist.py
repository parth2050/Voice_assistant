import pyttsx3
import os
import smtplib
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = datetime.datetime.now().hour
    if 0<=hour<12:
        speak("Good Morning, Sir")
    elif  12<=hour<18:
        speak("Good Afternoon, Sir")
    else:
        speak("Good Evening, Sir")
    speak("I'm virtual assistant!")
    speak("I can help you to put email to your friend, I can answer your any question, Tell me to open browser or Office software, it is not only this, I can do more than this.")
    speak("Hi Sir, I'm Aprth, How can I help you?")


def takecommand():
    #take commmad from microphones and returns string
    r = sr.Recognizer()
    # if text in response:
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 850
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="gu-in")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Can't get it, Can you be specific ?")
        return "None"
    return query


if __name__ == '__main__':
    WishMe()
    flag = True
    while flag:
        query = takecommand().lower()
        try:
            if "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia",'')
                answer = wikipedia.summary(query,sentences=3)
                speak("According to My Data...")
                print(answer)
                speak(answer)

            if "who is" in query:
                speak("Searching Wikipedia...")
                query = query.replace("who is",'')
                answer = wikipedia.summary(query,sentences=3)
                speak("According to My Data...")
                print(answer)
                speak(answer)

            if "tell me about" in query:
                speak("Searching Wikipedia...")
                query = query.replace("tell me about",'')
                answer = wikipedia.summary(query,sentences=3)
                speak("According to My Data...")
                print(answer)
                speak(answer)
        except:
            pass
        if 'open' in query:
            query = query.replace('open ','')
            webbrowser.open(query+".com")

        if 'search google' in query:
            query = query.replace('search google ','')
            os.system(f"start \"\" https://www.google.com/search?q={query}&source=lnms&tbm=nws")

        if 'google' in query:
            query = query.replace('google ','')
            print(query)
            os.system(f"start \"\" https://www.google.com/search?q={query}&source=lnms&tbm=nws")

        if 'youtube' in query:
            query = query.replace('youtube ','')
            os.system(f"start \"\" https://www.youtube.com/results?search_query={query}")

        if 'say about' in query:
            query = query.replace('say about ','')
            webbrowser.open(query+".com")

        if 'play music' in query:
            music_dir = "enter your music directory path"
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,song[0]))

        if 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir, The Time is {strtime}")

        if 'show me powerpoint' in query:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path)

        if 'show me firefox' in query:
            path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(path)

        if 'show me movie' in query:
            path = "Enter movie's absolute path here"
            os.startfile(path)

        

        if 'goodbye' in query:
            speak("Goodbye Sir, Nice to talk you, meet you soon!")
            flag = False
