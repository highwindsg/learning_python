#!/usr/bin/env python3

# The files classMCQApp.py and classMCQ_Questions.py are in the same dir.

# Create a class named Question.
class Question:
    # Define a init func with params self, prompt and answer. Reason
    # being because every quesion will have a prompt and answer.
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

