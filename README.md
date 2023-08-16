# Spotify_Remote
## A macropad that interfaces with the Spotify API.

### Overview

The idea behind this remote is to have a dedicated way to modify my Spotify playback while I'm busy doing other things. I've been playing a lot of computer games recently and having to tab out of my game to mess around with Spotify really breaks my immersion. Although my solution proved to cost several days of work and a handful of change, I'm happy with what I've learned and the functional gadget I was able to create.

### Features

Below are each of the features that the remote is able to control: 

- Pause/Play toggle
- Next Song
- Previous Song
- Shuffle toggle
- Repeat settings
- A reset button that should rerun the ```main.py``` file on the Pico.

### Materials

- Raspberry Pi Pico W (Around $15 for the kit I found on Amazon)
- Mechanical switches and caps
- Breadboard jumper cables
- Soldering iron + solder tin
- A computer with access to python3 and adequate I/O ports

### Software and Libraries

- Thonny IDE (To write micropython code and export to microcontroller)
- Python3, Micropython
- Spotipy (A Python library for contacting Spotify API)
- Python Dotenv library

## Installation 

### Installing Python and Libraries

The below steps will need to be followed for any machine that is testing or running the included code. 

Installing Python on a Linux operating system will be quite easy, simply run the code:

    sudo apt update && sudo apt upgrade

To update and upgrade existing packages on your machine, and then run:

    sudo apt-get install python3

For Ubuntu-based distributions or:

    sudo dnf install python3

For RedHat-based distributions such as Fedora. 

Verify that Python is installed by running the command:

    python3 --version

Installing Python on Windows is similar to installing any software on Windows. Visit the Microsoft store or the official Python website. Newer versions of Python should come with the 'pip' installer which is required for the next steps.

#### **Installing Spotipy**

Spotipy is the Python library that sends commands to the Spotify API. In a command line (Powershell, CMD, or Linux terminal) run the following command:

    pip install spotipy

or

    pip3 install spotipy

Click [Here](https://spotipy.readthedocs.io/en/2.22.1/) for Spotipy documentation, and click [Here](https://developer.spotify.com/documentation/web-api) for the Spotify API documentation. 

#### **Installing Python-dotenv**

Python-dotenv is a library that allows Python to import environment variables from a ```.env``` file from some directory on the host computer. The ```spotifyremote.py``` file makes use of python-dotenv to import unique client ID, client secret, user ID, and redirect URL variables to the running code. Python-dotenv is a good practice for hiding values that should be kept secret, such as the client secret API token. Install python-dotenv using pip with:

    pip3 install python-dotenv

or

    pip install python-dotenv

