from sys import argv

script, interviewee = argv
ans = "Your answer: "

print(f"Hi, {interviewee}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"What types of movies do you like to watch {interviewee}?")
movies = input(ans)

print(f"What type of seasons do you like to live in {interviewee}?")
seasons = input(ans)

print(f"Which country do you like to go tour in {interviewee}?")
tour = input(ans)

print(f"Favorite music?")
music = input(ans)

print(f"Favorite song?")
song = input(ans)

print(f"Do you like to eat spicy food?")
spicy = input(ans)

print(f"And what's your favorite color?")
color = input(ans)

print(f"What language would you like to learn to speak?")
lang= input(ans)

print(f"""
So here we have {interviewee} with us and today and we
have asked a few questions.
He likes to watch {movies} movies and also likes to live in country with
the {seasons} season year round.
His prefers to listen to {music} and currently likes the
song {song}.")
And when it comes to food, he says {spicy} to spicy stuffs.
Favourite color is {color} and he also would like to
learn to speak in {lang}, which is the language of Scottland.""")

