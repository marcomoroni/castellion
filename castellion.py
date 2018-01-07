from enum import Enum
from colorama import Fore, Back, Style
import random



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



mainPile = []

# create all tiles
newTile = Tile(TileFaction.SEER, TileShape.SQUARE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.SEER, TileShape.CIRCLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.SEER, TileShape.TRIANGLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.CHAMELEON, TileShape.SQUARE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.CHAMELEON, TileShape.CIRCLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.CHAMELEON, TileShape.TRIANGLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.JUGGLER, TileShape.SQUARE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.JUGGLER, TileShape.CIRCLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.JUGGLER, TileShape.TRIANGLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.PYRO, TileShape.SQUARE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.PYRO, TileShape.CIRCLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = Tile(TileFaction.PYRO, TileShape.TRIANGLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1

# shuffle
random.shuffle(mainPile)

# draw some random tiles
i = 0
while i < 10:
    mainPile.pop().print()
    i = i + 1

print()
