import unittest, sys

sys.path.append(".")

from dex import Pokedex, exp_for_lvl

class TestDex(unittest.TestCase):
    
    def setUp(self):
        self.pokemon_id = 133
        self.pokemon_name = "eevee"
    
    def test_API_Pokemon(self):
        """Test that will try the API for Pokémon data"""
        poke = Pokedex.api.get_pokemon(self.pokemon_id)
        self.assertEqual(poke.name, self.pokemon_name)
    
    def test_API_species(self):
        """Test that will try the API for Pokémon species data"""
        poke = Pokedex.api.get_pokemon_species(self.pokemon_id)
        self.assertEqual(poke.name, self.pokemon_name)
        
    def test_exp_formulas(self):
        """Test that will try the exp method for Pokemon EXP calculations"""
        cases = {
            1: {
                "exp_group": "erratic",
                "lvl": 17,
                "expected_exp": 8155
            },
            2: {
                "exp_group": "fast",
                "lvl": 34,
                "expected_exp": 31443
            },
            3: {
                "exp_group": "medium-fast",
                "lvl": 69,
                "expected_exp": 328509
            },
            4: {
                "exp_group": "medium-slow",
                "lvl": 88,
                "expected_exp": 710266
            },
            5: {
                "exp_group": "slow",
                "lvl": 1,
                "expected_exp": 0
            },
            6: {
                "exp_group": "slow",
                "lvl": 56,
                "expected_exp": 219520
            },
            7: {
                "exp_group": "fluctuating",
                "lvl": 78,
                "expected_exp": 673863
            },
        }
        for test in cases.values():
            group = test["exp_group"]
            lvl = test["lvl"]
            self.assertEqual(exp_for_lvl(group, lvl), test["expected_exp"])
    
        

if __name__ == "__main__":
    unittest.main()