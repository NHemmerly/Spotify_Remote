import network
import machine
import callSpot
import gc

# Client will connect to the server IP in practice

# Connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Enter ssid and password for local wifi network
ssid=''
password=''
wlan.connect(ssid, password)

# Declaring each pin object 
nextSong = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
pauseTogg = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
prevSong = machine.Pin(13, machine.Pin.IN,machine.Pin.PULL_DOWN)
shuffleTogg = machine.Pin(12, machine.Pin.IN,machine.Pin.PULL_DOWN)
repeatTogg = machine.Pin(11, machine.Pin.IN,machine.Pin.PULL_DOWN)

# Action loop, if any key is detected, send value to server 
# and garbage collect memory before listening to more 

while True:
    if nextSong.value():
        command = '0'
    elif pauseTogg.value():
        command = '1'
    elif prevSong.value():
        command = '2'
    elif shuffleTogg.value():
        command = '3'
    elif repeatTogg.value():
        command = '4'

    callSpot.callSpot(command)
    gc.collect()
    gc.mem_free()
        
    