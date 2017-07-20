#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import re

def main():
    artist = raw_input("Artist: ")
    site = requests.get("http://www.allthelyrics.com/lyrics/%s" % artist)
    soup = BeautifulSoup(site.text,"html.parser")
    fobj = open("%s_lyrics.txt" % artist,"w+")
    for entry in soup.find_all('a'):
        if(re.search("/lyrics/%s/" % artist,entry.get('href'))):
            site = requests.get("http://www.allthelyrics.com%s" % entry.get('href'))
            print "http://www.allthelyrics.com%s" % entry.get("href")
            if(site.status_code == 200):
                song_soup = BeautifulSoup(site.text,"html.parser")
                try:
                    fobj.write(song_soup.findAll("div",{"class":"content-text-inner"})[0].text)
                except:
                    pass
    fobj.close()


if __name__ == "__main__":
    main()
