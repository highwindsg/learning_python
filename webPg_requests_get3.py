#!/usr/bin/env python3

import requests

res = requests.get("https://www.gnu.org/licenses/lgpl-3.0.txt")

res.raise_for_status()

downloadFile = open("lesserGPL.txt", "wb")

for text in res.iter_content(100000):
    downloadFile.write(text)

downloadFile.close()

