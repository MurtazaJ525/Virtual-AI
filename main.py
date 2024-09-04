import os
import sys
import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Speech recognition library
import webbrowser  # For opening web pages
import datetime  # For fetching the current date and time
import requests  # For making HTTP requests
from sites import sites, apps, songs  # Custom module containing lists of sites, apps, and songs

# API key for News API
newsapi = "Your News api key"

def speak(text):
    """
    Convert the given text to speech.
    """
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.setProperty('rate', 150)  # Set speech speed
    engine.setProperty('volume', 0.9)  # Set volume level
    voices = engine.getProperty('voices')  # Get available voices
    engine.setProperty('voice', voices[0].id)  # Set the voice to the first available voice
    engine.say(text)  # Speak the given text
    engine.runAndWait()  # Wait for the speech to complete

def take_command():
    """
    Listen for a voice command and return the recognized text.
    """
    r = sr.Recognizer()  # Initialize the speech recognizer
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)  # Capture audio from the microphone
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")  # Recognize speech using Google's API
        print(f"User said: {query}")
    except Exception as e:
        # Return an error message if speech recognition fails
        return "Some Error Occurred"
    return query

def open_website(site_name, site_url):
    """
    Open the specified website and provide voice feedback.
    """
    speak(f"Opening {site_name}...")
    webbrowser.open(site_url)  # Open the website in the default browser

def open_song(song_name, site_url):
    """
    Play the specified song from the web and provide voice feedback.
    """
    speak(f"Playing {song_name}...")
    webbrowser.open(site_url)  # Open the song URL in the default browser

def play_music(music_path):
    """
    Play a music file located on the local system.
    """
    os.system(f"start {music_path}")  # Use the OS command to start the music file

def open_app(app_name, app_path):
    """
    Open the specified application and provide voice feedback.
    """
    speak(f"Opening {app_name}...")
    os.startfile(app_path)  # Open the application using its file path

if __name__ == '__main__':
    speak("Hey Murtazaa")  # Initial greeting
    while True:
        query = take_command().lower()  # Convert the spoken command to lowercase for easier processing

        # Check if the command is to open a website
        for site in sites:
            if f"open {site[0]}" in query:
                open_website(site[0], site[1])
                break

        # Check if the command is to play a song
        for song in songs:
            if f"play {song[0]}" in query:
                open_song(song[0], song[1])
                break

        # Check if the command is to fetch news headlines
        if "news" in query:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:  # If the request is successful
                news_data = r.json()
                articles = news_data["articles"]

                # Speak out the top 10 headlines
                print("Here are the top 10 news headlines:")
                speak("Here are the top 10 news headlines:")
                for i, article in enumerate(articles[:10]):
                    print(f"Headline {i + 1}: {article['title']}")
                    speak(f"Headline {i + 1}: {article['title']}")
            else:
                speak("Sorry, I couldn't fetch the news at the moment.")

        # Check if the command is to get the current time
        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M")  # Get the current time
            print(f"Sir, the time is {current_time}")
            speak(f"Sir, the time is {current_time}")

        # Check if the command is to exit the program
        if "exit" in query or "quit" in query:
            speak("Goodbye! Have a Grate time")  # Farewell message
            break

        # Check if the command is to open an application
        for app in apps:
            if f"open {app[0]}" in query:
                open_app(app[0], app[1])
                break
