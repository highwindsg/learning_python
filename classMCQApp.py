#!/usr/bin/env python3

# The files classMCQApp.py and classMCQ_Questions.py are in the same dir.
# Building a multiple choice quiz.

# Import the Question class module from the file classMCQ_Questions.py
from classMCQ_Questions import Question

# Create a question_prompts list.
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# Create a questions list with the respective correct answers that matches
# the questions_prompts list above.
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

# Define a func named run_test with the questions list as the param.
def run_test(questions):
    score = 0   # To start with, set a var score to zero first.
    for per_question in questions:  # For each question in the questions
                                    # list, do the below.
        answer = input(per_question.prompt) # Get user to give an input to the
                                            # question asked with a prompt. Obj
                                            # prompt is from the Question module.
                                            # And then assign it to var answer.
        if answer == per_question.answer:   # And if the answer in per_question is
                                            # the same as in var answer,
            score += 1  # then increase the correct score by 1.
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

# Client call the run_test function with the questions list as the param.
run_test(questions)

