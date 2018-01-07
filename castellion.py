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

    def __init__(self, faction, shape, safe=False):
        self.faction = faction
        self.shape = shape
        self.safe = safe

    # print a 1x3 tile
    def print(self):

        # change text colour
        print(Fore.BLACK, end="")
        if self.faction == TileFaction.SEER:
            print(Back.CYAN, end="")
        elif self.faction == TileFaction.CHAMELEON:
            print(Back.GREEN, end="")
        elif self.faction == TileFaction.JUGGLER:
            print(Back.RED, end="")
        elif self.faction == TileFaction.PYRO:
            print(Back.MAGENTA, end="")

        # safe tiles
        if self.safe:
            print(Fore.YELLOW, end="")

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
safePile = []

# create all main tiles
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

# create all safe tiles
newTile = Tile(TileFaction.SEER, TileShape.SQUARE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.SEER, TileShape.CIRCLE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.SEER, TileShape.TRIANGLE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.CHAMELEON, TileShape.SQUARE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.CHAMELEON, TileShape.CIRCLE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.CHAMELEON, TileShape.TRIANGLE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.JUGGLER, TileShape.SQUARE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.JUGGLER, TileShape.CIRCLE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.JUGGLER, TileShape.TRIANGLE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.PYRO, TileShape.SQUARE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.PYRO, TileShape.CIRCLE, safe=True)
safePile.append(newTile)
newTile = Tile(TileFaction.PYRO, TileShape.TRIANGLE, safe=True)
safePile.append(newTile)

# shuffle
random.shuffle(mainPile)
random.shuffle(safePile)

# draw some random tiles
i = 0
while i < 5:
    mainPile.pop().print()
    i = i + 1
i = 0
while i < 5:
    safePile.pop().print()
    i = i + 1

print()
