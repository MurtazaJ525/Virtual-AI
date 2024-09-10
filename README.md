
```markdown
# Virtual-AI

## Voice Assistant Project

### Overview

This project is a voice-controlled assistant application built in Python. It integrates various functionalities including web browsing, playing music, fetching news headlines, opening applications, and setting reminders. The assistant listens for voice commands, processes them, and performs the corresponding actions.

### Features

- **Voice Commands**: The assistant listens to and processes voice commands.
- **Web Browsing**: Open various websites based on voice commands.
- **Music Playback**: Play specific songs via web links.
- **News Updates**: Fetch and read out the top news headlines.
- **Weather Updates**: Get current weather information for a specified location.
- **Application Launch**: Open applications installed on your system.
- **Jokes**: Fetch and tell random jokes.
- **Reminders**: Set reminders for specific times.

### Requirements

**Install all packages by running this line:**

```bash
pip install -r requirements.txt
```

- Python 3.x
- `pyttsx3` - Text-to-Speech conversion library
- `speech_recognition` - Recognize speech and convert it to text
- `webbrowser` - Open web pages in the default browser
- `requests` - Make HTTP requests to fetch news and weather data
- `aiohttp` - For asynchronous HTTP requests
- `asyncio` - For running asynchronous functions
- `sites.py` - Contains lists of sites, songs, and applications

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MurtazaJ525/voice-assistant.git
   ```

2. Navigate to the project directory:

   ```bash
   cd voice-assistant
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the `sites.py` file with the necessary data for sites, songs, and applications.

### Usage

1. Run the main script:

   ```bash
   python main.py
   ```

2. The assistant will greet you and start listening for commands. You can say commands like "open YouTube", "play song", "news", "weather in [location]", "the time", "joke", or "open [application]".

### Configuration

- **News API Key**: Replace `newsapi` with your own News API key in the `main.py` file. You can obtain an API key by signing up at [NewsAPI](https://newsapi.org/).

- **Weather API Key**: Replace `weatherapi_key` with your own Weather API key in the `main.py` file. You can obtain an API key by signing up at [WeatherAPI](https://www.weatherapi.com/).

- **Sites, Songs, and Apps**: Modify the `sites.py` file to add or update the list of sites, songs, and applications.

### Example Commands

- To open a website: "open YouTube"
- To play a song: "play song"
- To get news updates: "news"
- To know the current time: "the time"
- To get the weather: "weather in [location]"
- To set a reminder: "reminder [text] at [time]"
- To tell a joke: "joke"
- To open an application: "open Visual Studio Code"
- To exit: "exit" or "quit"

### Contributing

Feel free to submit issues, feature requests, or pull requests. Contributions are welcome!

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Requests](https://pypi.org/project/requests/)
- [aiohttp](https://pypi.org/project/aiohttp/)
```
