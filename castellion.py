from enum import Enum



class TileFaction(Enum):
    SEER = 0
    CHAMELEON = 1
    JUGGLER = 2
    PYRO = 3



class TileShape(Enum):
    SQUARE = 0
    CIRCLE = 1
    TRIANGLE = 2



class Tile:

    def __init__(self, faction, shape):
        self.faction = faction
        self.shape = shape
