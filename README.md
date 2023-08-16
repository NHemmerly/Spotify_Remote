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

### Server and Pi Pico

#### The .env

In order to adapt code to a user besides myself, a unique ```.env``` file will need to be created and placed in the same directory where the ```spotifyremote.py``` file is running from. The .env file should look something like this:

    #.env

    SPOTIPY_CLIENT_ID = {spotipy client id}
    SPOTIPY_CLIENT_SECRET = {spotipy client secret}
    USER_TOKEN = {Spotify User ID}
    SPOTIPY_REDIRECT_URI = http://localhost

Replacing everything after the '=' with the corresponding value, which can be found by creating a Spotify app using the steps on the ['getting started' page for the Spotify API](https://developer.spotify.com/documentation/web-api/tutorials/getting-started). 

#### The Server

The server is any computer that will be running the ```spotifyremote.py``` code. In order to properly run ```spotifyremote.py``` a proper ```.env``` and the ```server_socket.py``` files will need to exist in the same directory. Note that the ```server_socket.py``` file will need to be altered to include the IPv4 address that is assigned to the host computer. As long as all of the above requirements are met, the ```spotifyremote.py``` file will successfully run on the host computer with the commands:

    python spotifyremote.py

or 

    python3 spotifyremote.py

Running the code will open a socket for communication from any computer on the network with a corresponding socket.

#### The Pico

Exporting code to the Raspberry Pi Pico is a little more complicated than a regular computer. In order to export micropython code I followed the steps detailed [Here](https://www.tomshardware.com/how-to/raspberry-pi-pico-setup) to install micropython as well as the Thonny IDE which is used to write micropython code to a supported micro controller like the Pi Pico W. 

After installing the micropython firmware to the Pico and connecting the Pico to your computer in 'run' mode, open both the ```main.py``` and ```callSpot.py``` files in Thonny.

First, 'save as' while the ```main.py``` code is opened on thonny and a prompt should open that asks to save on either 'this computer' or the name of the connected microcontroller. Note that the 'ssid' and 'password' in the ```main.py``` file should be changed to an available wifi network's information. After the ```main.py``` files is saved to the microcontroller, the ```callSpot.py``` file should also be saved to the microcontroller in the same fashion, also note that the 'HOST' variable in ```callSpot.py``` should be changed to the same IP address that is assigned to the server running ```server_socket.py```