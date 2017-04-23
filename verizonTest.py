import json
import urllib.request

"""This would refer to the house ID"""
thing = "00001"

"""Outputs status for the latest device report or history of device reports"""
def outputStatus(js):
    for thing in js["with"]:
        if len(thing["content"]) >= 2:
            print(thing["thing"], "--", thing["content"]["Status"])
            if thing["content"]["Status"] == 0:
                print("Connected IoT device,", thing["content"]["Device"] + ", is currently down!")
            else:
                print("Connected IoT device,", thing["content"]["Device"] + ", is running.")
        elif len(thing["content"]) < 2:
            print(thing["thing"], "--", thing["content"])


"""Request latest"""
def checkLatest():
    connection = urllib.request.urlopen("https://thingspace.io/get/latest/dweet/for/" + thing).read()
    js = json.loads(connection)
    outputStatus(js)

"""Returns past 24 device reports"""
def checkHistory():
    connection2 = urllib.request.urlopen("https://thingspace.io/get/dweets/for/" + thing).read()
    js = json.loads(connection2)
    outputStatus(js)

print("Check History")
checkHistory()
print("Check Latest")
checkLatest()
