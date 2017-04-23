import time
import urllib.request

"""This would refer to the house ID"""
thing = "00001"

"""Count to populate thingspace"""
count = 1

"""Acts as two IoT devices and sends them using the Device Messaging API"""
while count < 30:
    connection = urllib.request.urlopen("https://thingspace.io/dweet/for/" + thing + "?Status=" + str(count % 3) + "&Device=Nest")
    time.sleep(3)
    connection = urllib.request.urlopen("https://thingspace.io/dweet/for/" + thing + "?Status=" + str(count % 4) + "&Device=FIOS_ONT")
    print("Sent device status.")
    time.sleep(3)
    count += 1
