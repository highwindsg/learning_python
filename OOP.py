#!/usr/bin/env python3

# https://www.youtube.com/watch?v=ZGWVXUFq220&index=81&t=0s&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx

class Program():

    def __init__(self, *args, **kwargs):

        self.lang = input("What language?: ")
        self.version = float(input("Version?: "))
        self.skill = input("What skill level?: ")

    def upgrade(self):
        new_version = float(input("What version?: "))
        print("We have updated the version for", self.lang)


p1 = Program()
