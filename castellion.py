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
    def __str__(self):

        toPrint = ""

        # change text colour
        toPrint = toPrint + Fore.BLACK
        if self.faction == TileFaction.SEER:
            toPrint = toPrint + Back.CYAN
        elif self.faction == TileFaction.CHAMELEON:
            toPrint = toPrint + Back.GREEN
        elif self.faction == TileFaction.JUGGLER:
            toPrint = toPrint + Back.RED
        elif self.faction == TileFaction.PYRO:
            toPrint = toPrint + Back.MAGENTA

        # safe tiles
        if self.safe:
            toPrint = toPrint + Fore.YELLOW

        # print shape
        if self.shape == TileShape.SQUARE:
            toPrint = toPrint + " A "
        elif self.shape == TileShape.CIRCLE:
            toPrint = toPrint + " B "
        elif self.shape == TileShape.TRIANGLE:
            toPrint = toPrint + " C "

        # reset colour
        toPrint = toPrint + Style.RESET_ALL

        return toPrint



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
    print(mainPile.pop(), end=" ")
    i = i + 1
i = 0
while i < 5:
    print(mainPile.pop(), end=" ")
    i = i + 1

print()
