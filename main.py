import os
import sys
import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Speech recognition library
import webbrowser  # For opening web pages
import datetime  # For fetching the current date and time
import requests  # For making HTTP requests
import aiohttp  # For asynchronous HTTP requests
import asyncio  # For running asynchronous functions
from sites import sites, apps, songs  # Custom module containing lists of sites, apps, and songs

# API keys for News API and Weather API
newsapi_key = ["Your api Key"]
weatherapi_key = ["Your api Key"]

def speak(text):
    """Convert the given text to speech."""
    try:
        engine = pyttsx3.init()  # Initialize the text-to-speech engine
        engine.setProperty('rate', 150)  # Set speech speed
        engine.setProperty('volume', 0.9)  # Set volume level
        voices = engine.getProperty('voices')  # Get available voices
        engine.setProperty('voice', voices[0].id)  # Set the voice to the first available voice
        engine.say(text)  # Speak the given text
        engine.runAndWait()  # Wait for the speech to complete
    except Exception as e:
        print(f"Error in speak function: {e}")

def take_command():
    """Listen for a voice command and return the recognized text."""
    r = sr.Recognizer()  # Initialize the speech recognizer
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)  # Capture audio from the microphone
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")  # Recognize speech using Google's API
        print(f"User said: {query}")
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError as e:
        return f"Sorry, there was an error with the speech recognition service: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    return query.lower()

def listen_for_wake_word():
    """Listen for the wake word 'Hey Assistant'."""
    while True:
        query = take_command()
        if "hey jarvis" in query:
            # speak("Yes, how can I help you?")
            return True  # Wake word detected, return control to main command processing

def open_website(site_name, site_url):
    """Open the specified website and provide voice feedback."""
    try:
        speak(f"Opening {site_name}...")
        webbrowser.open(site_url)  # Open the website in the default browser
    except Exception as e:
        speak(f"Sorry, I couldn't open {site_name}.")
        print(f"Error in open_website function: {e}")

def open_song(song_name, site_url):
    """Play the specified song from the web and provide voice feedback."""
    try:
        speak(f"Playing {song_name}...")
        webbrowser.open(site_url)  # Open the song URL in the default browser
    except Exception as e:
        speak(f"Sorry, I couldn't play {song_name}.")
        print(f"Error in open_song function: {e}")

def play_music(music_path):
    """Play a music file located on the local system."""
    try:
        os.system(f"start {music_path}")  # Use the OS command to start the music file
    except Exception as e:
        speak(f"Sorry, I couldn't play the music file.")
        print(f"Error in play_music function: {e}")

def open_app(app_name, app_path):
    """Open the specified application and provide voice feedback."""
    try:
        speak(f"Opening {app_name}...")
        os.startfile(app_path)  # Open the application using its file path
    except Exception as e:
        speak(f"Sorry, I couldn't open {app_name}.")
        print(f"Error in open_app function: {e}")

def get_news():
    """Fetch and speak out the top 10 news headlines."""
    try:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi_key}")
        r.raise_for_status()  # Raise an exception for HTTP errors
        news_data = r.json()
        articles = news_data["articles"]
        speak("Here are the top 10 news headlines:")
        for i, article in enumerate(articles[:10]):
            headline = f"Headline {i + 1}: {article['title']}"
            print(headline)
            speak(headline)
    except requests.exceptions.RequestException as e:
        speak("Sorry, I couldn't fetch the news at the moment.")
        print(f"Error in get_news function: {e}")

def get_weather(location):
    """Fetch and speak out the current weather for the given location."""
    try:
        r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weatherapi_key}&q={location}")
        r.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = r.json()
        location_name = weather_data['location']['name']
        temperature = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        weather_report = f"The current weather in {location_name} is {temperature}°C with {condition}."
        print(weather_report)
        speak(weather_report)
    except requests.exceptions.RequestException as e:
        speak("Sorry, I couldn't fetch the weather at the moment.")
        print(f"Error in get_weather function: {e}")

async def fetch_joke():
    """Fetch a random joke asynchronously from JokeAPI."""
    url = "https://v2.jokeapi.dev/joke/Any"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            joke_data = await response.json()
            if joke_data["type"] == "single":
                return joke_data["joke"]
            else:
                return f"{joke_data['setup']} - {joke_data['delivery']}"

async def tell_joke():
    """Speak out a random joke."""
    joke = await fetch_joke()
    print(joke)
    speak(joke)

def set_reminder(reminder_time, reminder_text):
    """Set a reminder for a specific time."""
    try:
        current_time = datetime.datetime.now()
        reminder_datetime = datetime.datetime.strptime(reminder_time, "%H:%M")
        reminder_datetime = current_time.replace(hour=reminder_datetime.hour, minute=reminder_datetime.minute, second=0, microsecond=0)

        if reminder_datetime < current_time:
            reminder_datetime += datetime.timedelta(days=1)

        while datetime.datetime.now() < reminder_datetime:
            pass

        speak(f"Reminder: {reminder_text}")
        print(f"Reminder: {reminder_text}")
    except Exception as e:
        speak("Sorry, I couldn't set the reminder.")
        print(f"Error in set_reminder function: {e}")

if __name__ == '__main__':
    speak("Hey Boss, How can I help you today!")  # Initial greeting

    while True:
        # Wait for the wake word "Hey Assistant" before processing further commands
        listen_for_wake_word()

        query = take_command()

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
            get_news()

        # Check if the command is to get the current time
        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M")  # Get the current time
            print(f"Sir, the time is {current_time}")
            speak(f"Sir, the time is {current_time}")

        # Check if the command is to get the weather
        elif "weather" in query:
            location = query.replace("weather", "").strip()
            if location:
                get_weather(location)
            else:
                speak("Please specify a location.")

        # Check if the command is to set a reminder
        elif "reminder" in query:
            parts = query.split("at")
            if len(parts) == 2:
                reminder_time = parts[1].strip()
                reminder_text = parts[0].replace("reminder", "").strip()
                set_reminder(reminder_time, reminder_text)
            else:
                speak("Please specify the time and the reminder text.")

        # Check if the command is to tell a joke
        elif "joke" in query:
            asyncio.run(tell_joke())

        # Check if the command is to exit the program
        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a great time!")  # Farewell message
            break

        # Check if the command is to open an application
        for app in apps:
            if f"open {app[0]}" in query:
                open_app(app[0], app[1])
                break
