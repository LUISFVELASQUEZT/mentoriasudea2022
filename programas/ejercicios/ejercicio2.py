"""
    Ejercicio 2
    
"""

import sys
from turtle import title
import requests
import json

authors = ["Juanes","Cohen","Springsteen"]

class Track():
    def __init__(self,author,title, album):
        self.author = author
        self.title = title
        for album in album:
            self.album.append[album]
            
class Song():
    def __init__(self, author,title,album):
        self.author = author
        self.title = title
        self.album = album


def main(author):
    author=author
    req=build_request(author)
    run_request(req)
    
def build_request(author):
    req = "https://itunes.apple.com/" 
    req+= "search?term="
    req+=author
    req+="&limit=100"
    req+="&media=music"
    #req="https://itunes.apple.com/search?term=shakira&limit=200&media=music"
    print(req)
    return req

def run_request(req):
    resp = requests.get(req)
    o = resp.json()
    for result in o["results"]:
        try:
            artist=result["artistName"]
            song=result["trackName"]
            album=result["collectionName"]
        except KeyError:
            print(" Missing Data")
        else:
            song.artist = artist
            song.album = album
            song.title = title
            store_title(song)           
            print(f' Artist: {artist} Song: {song} Album:{album}')

def store_song(song):
        
                
if __name__ == "__main__":
    song = Song()
    for author in authors:
        main(author)        