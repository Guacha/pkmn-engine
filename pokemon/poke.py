class Pokemon:
    
    def __init__(self, species, stats, status, boosts, moves):
        self.species = None
        self.stats = {}
        self.status = None
        self.boosts = {}
        self.moves = []
        
    @staticmethod
    def create_wild(species):
        