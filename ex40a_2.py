class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

why_you_so_like_that = Song(["Once upon an island",
                             "a coconut tree or two",
                             "enjoying the breeze"])

love_you = Song(["Now and then, I want to hold you",
                 "in my arms tonight..."
                 "How I wish, that I could tell you",
                 "and make you mine"])

happy_bday.sing_me_a_song()
print("\n")
bulls_on_parade.sing_me_a_song()
print("\n")
why_you_so_like_that.sing_me_a_song()
print("\n")
love_you.sing_me_a_song()
