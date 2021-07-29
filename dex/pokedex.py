import requests, sys, json
import pokepy

class Pokedex:
    
    def __init__(self):
        self.entries = 0
        self.species = []
        self.abilities = []
        self.api = pokepy.V2Client(cache='in_disk', cache_location="../data")