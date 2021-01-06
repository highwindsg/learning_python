#!/usr/bin/env python3

# https://www.youtube.com/watch?v=AWvsXxDtEkU
# Note: Run the script in a separate terminal window.


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer() # To create a listening recognizer as set var.
engine = pyttsx3.init() # To initialize this text-to-speech engine.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)   # voices index 4 is female id voice for Alexa.

def talk(text):
    engine.say(text)
    engine.runAndWait()

#print(sr.Microphone.list_microphone_names())
# Set up a try and except block just in case microphone is not receiving well so that the
# program can try to listen again.

def take_command():
    try:
        with sr.Microphone() as source: # Using microphone as a source,
            #listener.adjust_for_ambient_noise(source)
            #listener.adjust_for_ambient_noise(source,duration=1)
            print("Listening....")
            #voice = listener.listen(source, timeout=10)    # then calling the speech_recognizer to listen to this source.
            voice = listener.listen(source)    # then calling the speech_recognizer to listen to this source.
            command = listener.recognize_google(voice) #  Using the listener's google API, and pass in the voice.
            command = command.lower()
            #if 'alexa' in command:
            if '' in command:
                #command = command.replace("alexa", "")
                command = command.replace("", "")
                print("You said:", command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    #print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        #print(song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "what is" in command:
        thing = command.replace("what is", "")
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())


run_alexa()
