import os
import sys
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import requests
from sites import sites, apps, songs


newsapi = "8d979cddb53c4af78977218e19ab40d5"


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        # speak("Sorry, I didn't understand that. Could you please repeat?")
        return "Some Error Occurred"
    return query


def open_website(site_name, site_url):
    speak(f"Opening {site_name}...")
    webbrowser.open(site_url)


def open_song(song_name, site_url):
    speak(f"Playing {song_name}...")
    webbrowser.open(site_url)



def play_music(music_path):
    os.system(f"start {music_path}")

def open_app(app_name, app_path):
    speak(f"Opening {app_name}...")
    os.startfile(app_path)


if __name__ == '__main__':
    speak("Hey Murtazaa")
    while True:
        query = take_command().lower()


        for site in sites:
            if f"open {site[0]}" in query:
                open_website(site[0], site[1])
                break


        for song in songs:
            if f"play {song[0]}" in query:
                open_song(song[0], song[1])
                break


        if "news" in query:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                news_data = r.json()
                articles = news_data["articles"]

                # Speak out the top 5 headlines
                print("Here are the top 10 news headlines:")
                speak("Here are the top 10 news headlines:")
                for i, article in enumerate(articles[:10]):
                    print(f"Headline {i + 1}: {article['title']}")
                    speak(f"Headline {i + 1}: {article['title']}")
            else:
                speak("Sorry, I couldn't fetch the news at the moment.")


        # elif "play music" in query:
        #     music_path = "C:/Users/rashi/Music/1.mp3"
        #     play_music(music_path)


        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            print(f"Sir, the time is {current_time}")
            speak(f"Sir, the time is {current_time}")


        if "exit" in query or "quit" in query:
            speak("Goodbye! Have a Grate time")
            break

        for app in apps:
            if f"open {app[0]}" in query:
                open_app(app[0], app[1])
                break

