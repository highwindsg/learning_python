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
