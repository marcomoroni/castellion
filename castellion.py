from enum import Enum
from colorama import Fore, Back, Style



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

    # print a 1x3 tile
    def print(self):

        # change text colour
        if self.faction == TileFaction.SEER:
            print(Back.CYAN + Fore.BLACK, end="")
        elif self.faction == TileFaction.CHAMELEON:
            print(Back.GREEN + Fore.BLACK, end="")
        elif self.faction == TileFaction.JUGGLER:
            print(Back.RED + Fore.BLACK, end="")
        elif self.faction == TileFaction.PYRO:
            print(Back.MAGENTA + Fore.BLACK, end="")

        # print shape
        if self.shape == TileShape.SQUARE:
            print(' A ', end="")
        elif self.shape == TileShape.CIRCLE:
            print(' B ', end="")
        elif self.shape == TileShape.TRIANGLE:
            print(' C ', end="")

        # reset colour
        print(Style.RESET_ALL, end="")
