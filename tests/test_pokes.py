import unittest, sys
sys.path.append(".")

from pokemon import Pokemon
from dex import Pokedex

class TestPokes(unittest.TestCase):
    
    def setUp(self):
        self.test_species = Pokedex.api.get_pokemon("eevee")
        
    def test_pkmn_generation(self):
        cases = [
            {
                "ivs": {
                    "hp": 0,
                    "atk": 0,
                    "def": 0,
                    "spa": 0,
                    "spd": 0,
                    "spe": 0
                },
                "evs": {
                    "hp": 0,
                    "atk": 0,
                    "def": 0,
                    "spa": 0,
                    "spd": 0,
                    "spe": 0
                },
                "expected":{
                    "hp": 20,
                    "atk": 10,
                    "def": 10,
                    "spa": 9,
                    "spd": 11,
                    "spe": 10
                },
                "lvl": 5,
                "nature": Pokedex.api.get_nature(1) # Hardy nature
            },
            {
                "ivs": {
                    "hp": 31,
                    "atk": 31,
                    "def": 31,
                    "spa": 31,
                    "spd": 31,
                    "spe": 31
                },
                "evs": {
                    "hp": 0,
                    "atk": 0,
                    "def": 0,
                    "spa": 0,
                    "spd": 0,
                    "spe": 0
                },
                "expected":{
                    "hp": 22,
                    "atk": 10,
                    "def": 12,
                    "spa": 11,
                    "spd": 13,
                    "spe": 12
                },
                "lvl": 5,
                "nature": Pokedex.api.get_nature(2) # Bold nature
            },
            {
                "ivs": {
                    "hp": 31,
                    "atk": 31,
                    "def": 31,
                    "spa": 31,
                    "spd": 31,
                    "spe": 31
                },
                "evs": {
                    "hp": 252,
                    "atk": 120,
                    "def": 0,
                    "spa": 120,
                    "spd": 0,
                    "spe": 0
                },
                "expected":{
                    "hp": 162,
                    "atk": 99,
                    "def": 70,
                    "spa": 80,
                    "spd": 85,
                    "spe": 67
                },
                "lvl": 50,
                "nature": Pokedex.api.get_nature("brave") # Brave nature
            }
        ]
        for case in cases:
            poke = Pokemon(self.test_species, case["lvl"], ivs=case["ivs"], evs=case["evs"], nature=case["nature"])
            for stat, value in poke.stats.items():
                self.assertEqual(value, case["expected"][stat], f"{stat.capitalize()} does not match expected value")
    
    def test_wild_pkmn_generation(self):
        expected_stats = {
            "bot": {
                "hp": 14,
                "atk": 6,
                "def": 6,
                "spa": 5,
                "spd": 6,
                "spe": 6
            },
            "top": {
                "hp": 14,
                "atk": 7,
                "def": 7,
                "spa": 7,
                "spd": 8,
                "spe": 7  
            }
        }
        poke: Pokemon = Pokemon.create_wild(self.test_species, [2])
        for stat, val in poke.stats.items():
            assert expected_stats["bot"][stat] <= val <= expected_stats["top"][stat], f"{stat.capitalize()} should be value between {expected_stats['bot'][stat]} and {expected_stats['top'][stat]}"
        
        self.assertEqual(poke.lvl, 2, "Pokémon lvl should be 2")
        self.assertEqual(poke.exp, 8)
        
    
    def tearDown(self):
        pass
    
if __name__ == "__main__":
    unittest.main()