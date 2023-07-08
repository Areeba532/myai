import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import pyttsx3
import openai
import os


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    pass

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    message = "hello I am Areeba's A I. how can i help you?"
    print(message)
    speak(message)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("recognizing...")
        query =  r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please..")
        return "none"
    return query

def myai():
    openai.api_key = "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"

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)

    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    conversation = ""
    user_name = "Dan"
    bot_name = "John"

    while True:
        with mic as source:
            print("\n Listening...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
        print("no longer listening")

        try:
            user_input = r.recognize_google(audio)
            if user_input == 'exit':
                break
            print(f"user said: {user_input}\n")
        except:
            continue

        prompt = user_name + ":" + user_input + "\n" + bot_name + ":"
        conversation += prompt

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=conversation,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(
            user_name + ":", 1)[0].split(bot_name + ":", 1)[0]

        conversation += response_str + "\n"
        print(response_str)

        engine.say(response_str)
        engine.runAndWait()


if __name__ == '__main__':
    wishme()
    while True:
       query = takeCommand().lower()
       if 'wikipedia' in query:
           speak('searching wikipedia')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("according to wikipedia")
           print(results)
           speak(results)


       elif 'open youtube' in query:
           webbrowser.open("youtube.com")

       elif 'open google' in query:
           webbrowser.open("google.com")

       elif 'play music' in query:
           music = "music"
           songs = os.listdir(music)
           print(songs)
           os.startfile(os.path.join(music,songs[0]))

       elif 'the time' in query:
           strtime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strtime)
           speak(f"the time is {strtime}")

       elif 'open code' in query:
           path = "C:\\Users\\TTC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(path)

       elif 'my ai' in query:
           myai()
