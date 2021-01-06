#!/usr/bin/env python3

# https://www.youtube.com/watch?v=AWvsXxDtEkU

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer() # To create a listening recognizer as set var.
engine = pyttsx3.init() # To initialize this text-to-speech engine.
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[4].id)   # voices index 4 is female id voice for Alexa.
engine.say("Hi! I'm Alexa, your IT Space special agent.")
engine.say("What can I do for you?")
engine.runAndWait()

print(sr.Microphone.list_microphone_names())
# Set up a try and except block just in case microphone is not receiving well so that the
# program can try to listen again.

try:
    with sr.Microphone() as source: # Using microphone as a source,
        # listener.adjust_for_ambient_noise(source)
        listener.adjust_for_ambient_noise(source,duration=1)
        print("Listening....")
        voice = listener.listen(source, timeout=10)    # then calling the speech_recognizer to listen to this source.
        command = sr.recognize_google(voice) #  Using the listener's google API, and pass in the voice.
        command = command.lower()
        if 'alexa' in command:
            print(command)


except:
    pass
