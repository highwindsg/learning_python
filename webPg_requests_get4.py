#!/usr/bin/env python3

import requests

res = requests.get("https://account.mojang.com/documents/minecraft_eula")

res.raise_for_status()

downloadFile = open("Mojang.txt", "wb")

for text in res.iter_content(100000):
    downloadFile.write(text)

downloadFile.close()

