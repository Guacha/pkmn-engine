import random, sys, math
sys.path.append(".")
from dex import Pokedex
from pokepy.resources_v2 import PokemonResource, NatureResource

class Pokemon():
    
    def __init__(
        self,
        species: PokemonResource,
        lvl: int,
        stats: dict = None,
        status = None,
        boosts = None,
        moves = None,
        ivs = None,
        evs = None,
        nature = None,
        exp = 0):
        
        self.species: NatureResource = species
        self.lvl = lvl
        
        # Setting default IVs if necessary
        if ivs:
            self.ivs: dict = ivs
        else:
            self.ivs: dict = {
                'hp': random.randint(0,31),
                'atk': random.randint(0,31),
                'def': random.randint(0,31),
                'spa': random.randint(0,31),
                'spd': random.randint(0,31),
                'spe': random.randint(0,31)
            }
        
        # Setting default EVs if necessary
        if evs:
            self.evs: dict = evs
        else:
            self.evs: dict = {
                'hp': 0,
                'atk':0,
                'def':0,
                'spa':0,
                'spd':0,
                'spe':0,            
            }
        
        if nature:
            self.nature = nature
        else:
            nature = Pokedex.get_random_nature()
        
        if stats:
            self.stats: dict = stats
        else:
            self.stats: dict = self.calculate_stats()
        self.status = status
        self.boosts = boosts
        self.moves = moves
    
    def calculate_stats(self) -> dict:
        base = self.species
        iv = self.ivs
        ev = self.evs
        new_stats = {}
        new_stats['hp'] = ((2 * base[0].base_stat + iv['hp'] + ev['hp']//4) * self.lvl)//100 + 10 + self.lvl
        for num, stat, long_stat in ((1, 'atk', 'attack'), (2, 'def', 'defense'), (3, 'spa', 'special-attack'), (4, 'spd', 'special-defense'), (5, 'spe', 'speed')):
            new_stats[stat] = (2*base[num].base_stat + iv[stat] + ev[stat]//4 * self.lvl)//100 + 5
            if self.nature.increased_stat == long_stat:
                new_stats = math.floor(new_stats[stat] * 1.1)
            
            if self.nature.decreased_stat == long_stat:
                new_stats = math.floor(new_stats[stat] * 0.9)
        
        return new_stats
            
    
    # TODO: Implement method to generate wild pokemon  
    @staticmethod
    def create_wild(species: PokemonResource, level_range: list = None):
        lvl = random.randint(2,75)
        return Pokemon(species, lvl)