# Virtual-AI



# Voice Assistant Project

## Overview

This project is a voice-controlled assistant application built in Python. It integrates various functionalities including web browsing, playing music, fetching news headlines, and opening applications. The assistant listens for voice commands, processes them, and performs the corresponding actions.

## Features

- **Voice Commands**: The assistant listens to and processes voice commands.
- **Web Browsing**: Open various websites based on voice commands.
- **Music Playback**: Play specific songs via web links.
- **News Updates**: Fetch and read out the top news headlines.
- **Application Launch**: Open applications installed on your system.

## Requirements

**install all package by run this line **
  -pip install -r .\requirement.txt

- Python 3.x
- `pyttsx3` - Text-to-Speech conversion library
- `speech_recognition` - Recognize speech and convert it to text
- `webbrowser` - Open web pages in the default browser
- `requests` - Make HTTP requests to fetch news data
- `sites.py` - Contains lists of sites, songs, and applications

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   ```

2. Navigate to the project directory:

   ```bash
   cd voice-assistant
   ```

3. Install the required packages:

   ```bash
   pip install pyttsx3 SpeechRecognition requests
   ```

4. Ensure you have the `sites.py` file with the necessary data for sites, songs, and applications.

## Usage

1. Run the main script:

   ```bash
   python main.py
   ```

2. The assistant will greet you and start listening for commands. You can say commands like "open YouTube", "play song", "news", or "the time".

## Configuration

- **News API Key**: Replace `newsapi` with your own News API key in the `main.py` file. You can obtain an API key by signing up at [NewsAPI](https://newsapi.org/).

- **Sites, Songs, and Apps**: Modify the `sites.py` file to add or update the list of sites, songs, and applications.

## Example

- To open a website: "open YouTube"
- To play a song: "play song"
- To get news updates: "news"
- To know the current time: "the time"
- To open an application: "open Visual Studio Code"
- To exit: "exit" or "quit"

## Contributing

Feel free to submit issues, feature requests, or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Requests](https://pypi.org/project/requests/)

```

You can customize the URL in the `git clone` command and any other specifics to match your repository and project details.
