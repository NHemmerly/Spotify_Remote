import network
import machine
import callSpot
import gc

# Client will connect to the server IP in practice

# Connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid='loveisland(uk)'
password='EatSleepSnog123'
wlan.connect(ssid, password)

nextSong = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
pauseTogg = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
prevSong = machine.Pin(13, machine.Pin.IN,machine.Pin.PULL_DOWN)
shuffleTogg = machine.Pin(12, machine.Pin.IN,machine.Pin.PULL_DOWN)
repeatTogg = machine.Pin(11, machine.Pin.IN,machine.Pin.PULL_DOWN)

while True:
    if nextSong.value():
        command = '0'
        callSpot.callSpot(command)
        gc.collect()
        gc.mem_free()
    elif pauseTogg.value():
        command = '1'
        callSpot.callSpot(command)
        gc.collect()
        gc.mem_free()
    elif prevSong.value():
        command = '2'
        callSpot.callSpot(command)
        gc.collect()
        gc.mem_free()
    elif shuffleTogg.value():
        command = '3'
        callSpot.callSpot(command)
        gc.collect()
        gc.mem_free()
    elif repeatTogg.value():
        command = '4'
        callSpot.callSpot(command)
        gc.collect()
        gc.mem_free()
        
    