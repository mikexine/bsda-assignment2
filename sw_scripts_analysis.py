#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from create_wordcloud import create_wordcloud
import string


# data source
original_urls = ["http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html",
                 "http://www.imsdb.com/scripts/Star-Wars-The-Empire-Strikes-Back.html",
                 "http://www.imsdb.com/scripts/Star-Wars-Return-of-the-Jedi.html"]

prequel_urls = ["http://www.imsdb.com/scripts/Star-Wars-The-Phantom-Menace.html",
                "http://www.imsdb.com/scripts/Star-Wars-Attack-of-the-Clones.html",
                "http://www.imsdb.com/scripts/Star-Wars-Revenge-of-the-Sith.html"]


# necessary data for text processing
data = {
    "original": {
        "urls": original_urls,
        "filename": "original_trilogy.txt",
        "script": "",
        "clean_script": "",
        "cleaner": [["Luke's", "Luke"], ["Vader's", "Vader"],
                    ["Artoo's", "Artoo"], ["Leia's", "Leia"],
                    ["Int", ""], ["Ext", ""]],
        "mask": "masks/sw_original_mask.png",
        "target_file": "results/original_wordcloud.png"
    },
    "prequel": {
        "urls": prequel_urls,
        "filename": "prequel_trilogy.txt",
        "script": "",
        "clean_script": "",
        "cleaner": [["Luke's", "Luke"], ["Vader's", "Vader"],
                    ["Artoo's", "Artoo"], ["Leia's", "Leia"],
                    ["Int", ""], ["Ext", ""], ["Wan's", "Wan"]],
        "mask": "masks/sw_prequel_mask.png",
        "target_file": "results/prequel_wordcloud.png"
    }
}


# gathering the scripts and creating the two text files
for d in data:
    for url in data[d]["urls"]:
        print(d + " - " + url)
        soup = BeautifulSoup(urlopen(url).read(), "lxml")
        script = soup.find("td", class_="scrtext")
        data[d]["script"] += script.get_text()
    f = open(data[d]["filename"], 'w')
    f.write(data[d]["script"])

    # clean the script (capitalize all words)
    data[d]["clean_script"] = string.capwords(data[d]["script"])

    # remove "custom" stopwords
    for word in data[d]["cleaner"]:
        data[d]["clean_script"] = data[d]["clean_script"].replace(word[0], word[1])

    # create the wordcloud
    create_wordcloud(data[d]["clean_script"], data[d]["mask"], data[d]["target_file"])
