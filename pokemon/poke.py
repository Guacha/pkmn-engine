import random, sys, math
sys.path.append(".")
from dex import Pokedex, exp_for_lvl
from pokepy.resources_v2 import PokemonResource, NatureResource

class Pokemon():
    
    def __init__(
        self,
        species: PokemonResource,
        lvl: int,
        exp = None, 
        nick = None,
        stats: dict = None,
        status = None,
        boosts = None,
        moves = None,
        ivs = None,
        evs = None,
        nature = None,
        shiny = False
        ) -> 'Pokemon':
        
        self.species: PokemonResource = species
        self.lvl = lvl
        self.nick = nick
        if exp:
            self.exp: int = exp
        else:
            self.exp = exp_for_lvl(Pokedex.get_species(self.species).growth_rate.name, self.lvl)
        
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
            self.nature = Pokedex.get_random_nature()
        
        if stats:
            self.stats: dict = stats
        else:
            self.stats: dict = self.calculate_stats()
        self.status = status
        self.boosts = boosts
        self.moves = moves
        self.shiny = shiny
    
    def calculate_stats(self) -> dict:
        base = self.species.stats
        iv = self.ivs
        ev = self.evs
        new_stats = {}
        
        # Hp is calculated on a different formula
        # Exception for shedinja
        if self.species.name == 'shedinja':
            new_stats['hp'] = 1
        else:
            new_stats['hp'] = ((2 * base[0].base_stat + iv['hp'] + ev['hp']//4) * self.lvl)//100 + 10 + self.lvl
        
        # Calculate other stats
        for num, stat, long_stat in ((1, 'atk', 'attack'), (2, 'def', 'defense'), (3, 'spa', 'special-attack'), (4, 'spd', 'special-defense'), (5, 'spe', 'speed')):
            new_stats[stat] = ((2*base[num].base_stat + iv[stat] + ev[stat]//4) * self.lvl)//100 + 5
            try:
                if self.nature.increased_stat.name == long_stat:
                    new_stats[stat] = math.floor(new_stats[stat] * 1.1)
                
                if self.nature.decreased_stat.name == long_stat:
                    new_stats[stat] = math.floor(new_stats[stat] * 0.9)
            except Exception:
                pass
        
        return new_stats
            
    
    # TODO: Implement method to generate wild pokemon  
    @classmethod
    def create_wild(species: PokemonResource, level_range: list = None) -> 'Pokemon':
        if level_range is None:
            lvl = random.randint(2,80)
        else:
            lvl = random.choice(level_range)
        return Pokemon(species, lvl)
