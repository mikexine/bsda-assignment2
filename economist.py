#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from create_wordcloud import create_wordcloud

urls = set()

collects = ["https://medium.com/_/api/users/bea61c20259e/profile/stream?limit=8&to=1474663670380&source=overview&page=1",
            "https://medium.com/_/api/users/bea61c20259e/profile/stream?limit=8&to=1474663670380&source=overview&page=2",
            "https://medium.com/_/api/users/bea61c20259e/profile/stream?limit=8&to=1474576184617&source=overview&page=3",
            "https://medium.com/_/api/users/bea61c20259e/profile/stream?limit=8&to=1473454645225&source=overview&page=4",
            "https://medium.com/_/api/users/bea61c20259e/profile/stream?limit=8&to=1471337098113&source=overview&page=5",
            "https://medium.com/_/api/users/bea61c20259e/profile/stream?limit=8&to=1470303824634&source=overview&page=6",
            "https://medium.com/_/api/users/bea61c20259e/profile/stream?limit=8&to=1470299346289&source=overview&page=7"]

# collects = ["https://medium.com/_/api/users/bea61c20259e/profile/stream?limit=8&to=1474663670380&source=overview&page=1"]

for c in collects:
    raw = requests.get(c).text
    raw = raw.replace("])}while(1);</x>", "")
    data = json.loads(raw)
    try:
        post = data["payload"]["references"]["Post"]
    except:
        pass
    for p in post:
        urls.add(post[p]["uniqueSlug"])

text = ""
c = 0

for u in urls:
    target = "https://medium.com/the-economist/" + u + "?format=json"
    raw = requests.get(target).text
    raw = raw.replace("])}while(1);</x>", "")
    data = json.loads(raw)
    try:
        paragraphs = data["payload"]["value"]["content"]["bodyModel"]["paragraphs"]
        c += 1
        for p in paragraphs:
            text = text + p["text"] + " "
    except:
        print("err")

    

# print(text)
print(c)

f = open("economist.txt", 'w')
f.write(text)


# f = open("economist.txt", "r")
# text = f.read()


create_wordcloud(text, "masks/economist_mask.png", "results/economist.png")
f.close()
