from random import random
from pokepy.resources_v2 import PokemonResource, NatureResource
class Pokemon():
    
    def __init__(
        self,
        species: PokemonResource,
        stats: dict = None,
        status = None,
        boosts = None,
        moves = None,
        ivs = None,
        evs = None,
        nature = None,
        exp = 0):
        
        self.species: NatureResource = species
        self.stats: dict = stats
        
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
        
        self.status = status
        self.boosts = boosts
        self.moves = moves
    
    def calculate_stats():
        
        pass
    
    # TODO: Implement method to generate wild pokemon  
    @staticmethod
    def create_wild(species: PokemonResource, level_range: list = None):
        pass