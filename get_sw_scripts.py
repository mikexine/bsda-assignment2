#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

original_urls = ["http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html",
                 "http://www.imsdb.com/scripts/Star-Wars-The-Empire-Strikes-Back.html",
                 "http://www.imsdb.com/scripts/Star-Wars-Return-of-the-Jedi.html"]

prequel_urls = ["http://www.imsdb.com/scripts/Star-Wars-The-Phantom-Menace.html",
                "http://www.imsdb.com/scripts/Star-Wars-Attack-of-the-Clones.html",
                "http://www.imsdb.com/scripts/Star-Wars-Revenge-of-the-Sith.html"]

data = {
    "original": {
        "urls": original_urls,
        "filename": "original_trilogy.txt",
        "script": ""
    },
    "prequel": {
        "urls": prequel_urls,
        "filename": "prequel_trilogy.txt",
        "script": ""
    }
}

for trilogy in data:
    for url in data[trilogy]["urls"]:
        print(trilogy + " - " + url)
        soup = BeautifulSoup(urlopen(url).read(), "lxml")
        script = soup.find("td", class_="scrtext")
        data[trilogy]["script"] += script.get_text()
    f = open(data[trilogy]["filename"], 'w')
    f.write(data[trilogy]["script"])

f.close()
