#!/usr/bin/enn python3

# https://www.youtube.com/watch?v=I46JJYlR0Lg
# https://github.com/ashraf-minhaj/TotLa-a-Talking-Robot-in-Python/blob/master/totla_Bot_v2.py


import pyttsx3
import speech_recognition as sr
import sound
import time


talk = pyttsx3.init()   # initialize pyttsx3


# build a different list of words.
call_list = [
    "javis",
    "hey jarvis",
    "hello jarvis",
    "jar vis",
    "ja vis",
    "javi",
    "ja vi"
]

r_u_there = [
    "are you there",
    "are you their",
    "are you dare",
    "you there",
    "you their"
]

hi_list = [
    "hi",
    "hello",
    "hey",
    "yo",
    "greetings",
]

bye_list = [
    "bye",
    "goodbye",
    "good bye",
    "byebye",
    "bye bye",
    "by by",
    "so long",
    "OK bye",
    "okay bye",
    "got to go",
    "gotta go"
]

question_list = [
    "who are you",
    "what's your name",
    "whats your name",
    "your name",
    "introduce yourself",
    "what are you"
]

response_neg_list = [
    "bad robot",
    "bad boy",
    "you need counselling"
]

slang_list = [
    "eerrr",
    "er",
    "crap",
    "aiyo",
    "walau"
    "wa lau",
    "walauweh",
    "wa lau weh",
    "shit",
    "g g",
    "gee gee"
]

love_list = [
    "love you",
    "loves you",
    "i love you",
    "we love you",
    "we all love you",
    "bless you",
    "you are sweet",
    "you're sweet",
    "you are cute",
    "you're cute",
    "you are gorgeous",
    "you're gorgeous",
    "you are good looking",
    "you're good looking"
]

hate_list = [
    "i hate you",
    "hate you"
    "you are rude",
    "you're rude",
    "screw you",
    "fuck you",
    "chee by",
    "chee bye",
    "chee hong",
    "nah bay",
    "nah buay",
    "nah buey",
    "lick my ass",
    "kill yourself",
]


def Listen():
    """
    Takes users voice as input and converts it to text.
    """
    speech = sr.Recognizer()    # says beep before listening.

    # Takes input from microphone.
    with sr.Microphone() as source:
        #winsound.Beep(frequency = 2500, duration = 100)
        print("Say >>")
        voice = speech.listen(sound)
        text = speech.recognize_google(voice)
        print(text)

    return text # Return what was said.


def Respond(t):
    print(f"Talking the: {t}")  # for debugging

    talk.say(t)
    #talk.setProperty("rate", 90)    # 90 words per minute
    talk.runAndWait()


def Decide(listen):
    """
    Takes decision based on what user says.
    """
    print(f" Command = {listen}.")  # for debugging

    # see what user said is in any of the list or not.
    if listen in hi_list:
        Respond("Hi there, Good to see you.")

    elif listen in bye_list:
        Respond("I liked talking with you, okay take care.")

    elif listen in hate_list:
        Respond("Hate you too.")

    elif listen in question_list:
        Respond("I am talking bot. The talking robot written in Python. My creator Caven is trying to make me start.")

    elif listen in response_neg_list:
        Respond("I am very sorry, I was just joking")

    elif listen in slang_list:
        Respond("You are bad in English")

    elif listen in r_u_there:
        Respond("For, you, always sir")

    else:
        Respond("Sorry, I don't understand. Please say again")

    
while True: # loop forever.
    """
    The robot needs a wakeup command so that it can start listening to it.
    """

    try:
        speech = sr.Recognizer()

        # Take input from microphone
        with sr.Microphone() as source:
            print("Call >>")
            voice = speech.listen(source)
            called = speech.recognize_google(voice)
            print(called)   # print what it heard, debugging only

            if called in call_list:
                comm = Listen() # listen to what user says
                Decide(comm)    # take decision and respond
    
    except: # No wake up word found
        pass
