import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pickle
import pywhatkit
import pyglet
import pyjokes

print(56)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
animation = pyglet.image.load_animation('original.gif')
animSprite = pyglet.sprite.Sprite(animation)

w = animSprite.width
h = animSprite.height

window = pyglet.window.Window(width=w, height=h)



@window.event
def on_draw():
    window.clear()
    animSprite.draw()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def bootup():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")
    speak("Lets Go... You can start by saying help")


def listen():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    pyglet.app.run()
    bootup()
    while True:
        # if 1:
        query = listen().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")


        elif 'play music' in query:
            music_dir = '//path to music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")



        elif 'exit' in query:
            speak("Adios. See you Next time")
            exit(0)

        elif 'what is' in query:
            speak("searching on google");
            com = query;
            com.replace(" ", "+")
            webbrowser.open("https://www.google.com/search?q=" + com);

        elif 'play' in query:
            speak("Sorry I didn't get it. Please repeat what to play on youtube...")
            command=listen()
            pywhatkit.playonyt(command)

        elif ('vdc' in query or 'visual design and communication' in query or "dpp" in query or "design" in query or "design process and perspectives") and "class" in query:
            webbrowser.open("https://zoom.us/j/91084981889?pwd=VEhJYlhRTE95WFdJNHEzNG5hcld6dz09")

        elif ('ap' in query or 'Advanced Programming' in query or "advance programming" in query) and "class" in query:
            webbrowser.open("https://meet.google.com/oiv-hidw-xgn")

        elif ('os' in query or 'operating system' in query) and "class" in query:
            webbrowser.open("https://meet.google.com/yvh-jdiq-jyi")

        elif ('dm' or "discrete maths" in query or "discrete mathematics" in query) and "class" in query:
            webbrowser.open("https://zoom.us/meeting/register/tJUlf-qhpzorHNYto-CKZqxWijrLONiFZQMx")

        elif 'classroom' in query:
            webbrowser.open("https://classroom.google.com/u/0/h")
        elif 'whatsapp' in query:
            contacts = {"Mesg": "+918800603149", "shrey": "+918700114640"}
            speak("Sure! What's the message?")
            content = listen()
            pywhatkit.sendwhatmsg(contacts["shrey"], content, int(datetime.datetime.now().strftime("%H")), int(datetime.datetime.now().strftime("%M"))+2)
            print("Successfully Sent!")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'handwrit' in query:
            speak("Ok, what do you want written")
            text=listen()
            pywhatkit.text_to_handwriting(text, rgb=[0, 0, 0])

        query=''
