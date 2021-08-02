import pokepy
import random
from pokepy.resources_v2 import NatureResource, PokemonResource, PokemonSpeciesResource

class Pokedex:
    #Gen8 Compliant
    entries = 898
    api = pokepy.V2Client(cache='in_disk', cache_location="./data")
    
    @staticmethod
    def get_species(pokemon: PokemonResource):
        return Pokedex.api.get_pokemon_species(pokemon.species.name)
    
    @staticmethod
    def get_random_nature() -> NatureResource:
        
        num = random.randint(1,25)
        return Pokedex.api.get_nature(num)
    
    @staticmethod
    def get_random_poke(range: list = None) -> PokemonResource:
        if range:
            n = random.choice(range)
        else:
            n = random.choice(range(1,899))
        
        return Pokedex.api.get_pokemon(n)
    
    @staticmethod
    def random_poke_in_region(region: str) -> PokemonResource:
        if region:
            ranges = {
                'kanto': [x for x in range(1,152)],
                'johto': [x for x in range(152, 252)],
                'hoenn': [x for x in range(252, 387)],
                'sinnoh': [x for x in range(387, 493)],
                'unova': [x for x in range(494, 650)],
                'kalos': [x for x in range(650, 721)],
                'alola': [x for x in range(721, 810)] + [x for x in range(10091, 10093)] + [x for x in range(10100, 10116)],
                'galar': [x for x in range(810, 899)] + [x for x in range(10158, 10178)],
            }
            return Pokedex.get_random_poke(ranges[region])
    
    # TODO: Implement evolutions
    @staticmethod
    def get_evolutions(species: PokemonSpeciesResource, current=None, evs=None):
        chain = Pokedex.get_evolution_chain(species)
        if not current:
            current = chain.chain
        if not evs:
            evs = []
        
        if current.species.name == species.name:
            pass
        
        print(f"{species.name.capitalize()} evolves into {current.evolves_to.species.name.capitalize()}")
    
    @staticmethod
    def get_evolution_chain(species: PokemonSpeciesResource):
        return Pokedex.api.get_evolution_chain(species.evolution_chain.url.split("/")[-2])