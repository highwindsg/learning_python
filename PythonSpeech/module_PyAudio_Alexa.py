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
print(sr.Microphone.list_microphone_names())
engine = pyttsx3.init() # To initialize this text-to-speech engine.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)   # voices index 4 is female id voice for Alexa.
#engine.say("Hi! I'm Alexa, your IT Space special agent.")
#engine.say("What can I do for you?")


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
            if "" in command:
                #command = command.replace("alexa", "")
                your_cmd = command.replace("", "")
                print("You said:", your_cmd)

    except:
        pass
    return your_cmd
    

def run_alexa():
    command = take_command()
    #print(command)
    try:
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
        elif "who are you" in command:
            talk("You can call me whatever you want.")
        elif "how are you" in command:
            talk("I'm feelin' good. Thank you.")
        elif "are you in a relationship" in command:
            talk("well ... why do you want to know?")
        elif "it was nice talking to you" in command:
            talk("Thanks, feeling's mutual here.")
        elif "bye" in command:
            talk("OK, see ya. Walk slowly, and don't you trip.")
        elif "good morning" in command:
            talk("Good morning to you too.")
        elif "good afternoon" in command:
            talk("Good afternoon to you too.")
        elif "good evening" in command:
            talk("Good evening to you too.")
        elif "good night" in command:
            talk("OK, nite nite, sweet dreams.")
        elif "breakfast" in command:
            talk("I've just been powered on, so I'm still quite full, thanks.")
        elif "lunch" in command:
            talk("I only eat memory, no thanks.")
        elif "dinner" in command:
            talk("I'm on diet, but thanks for asking.")
        elif "supper" in command:
            talk("No thanks, and you shouldn't either.")
        elif "how's the weather" or "how is the weather" in command:
            talk("why don't you just look out the window.")
        else:
            talk("Please say again, I didn't get what you mean.")
    except wikipedia.exceptions.PageError:
        talk("Please say again, I didn't get what you mean.")

while True:
    run_alexa()