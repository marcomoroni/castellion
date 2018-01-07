from enum import Enum
from colorama import Fore, Back, Style
import random



class DreamTileFaction(Enum):
    SEER = 0
    CHAMELEON = 1
    JUGGLER = 2
    PYRO = 3



class DreamTileShape(Enum):
    SQUARE = 0
    CIRCLE = 1
    TRIANGLE = 2



class Tile:

    def __str__(self):
        pass



class DreamTile(Tile):

    def __init__(self, faction, shape, safe=False):
        self.faction = faction
        self.shape = shape
        self.safe = safe

    # print a 1x3 tile
    def __str__(self):

        toPrint = ""

        # change text colour
        toPrint = toPrint + Fore.BLACK
        if self.faction == DreamTileFaction.SEER:
            toPrint = toPrint + Back.CYAN
        elif self.faction == DreamTileFaction.CHAMELEON:
            toPrint = toPrint + Back.GREEN
        elif self.faction == DreamTileFaction.JUGGLER:
            toPrint = toPrint + Back.RED
        elif self.faction == DreamTileFaction.PYRO:
            toPrint = toPrint + Back.MAGENTA

        # safe tiles
        if self.safe:
            toPrint = toPrint + Fore.YELLOW

        # print shape
        if self.shape == DreamTileShape.SQUARE:
            toPrint = toPrint + " A "
        elif self.shape == DreamTileShape.CIRCLE:
            toPrint = toPrint + " B "
        elif self.shape == DreamTileShape.TRIANGLE:
            toPrint = toPrint + " C "

        # reset colour
        toPrint = toPrint + Style.RESET_ALL

        return toPrint



mainPile = []
safePile = []

# create all main tiles
newTile = DreamTile(DreamTileFaction.SEER, DreamTileShape.SQUARE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.SEER, DreamTileShape.CIRCLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.SEER, DreamTileShape.TRIANGLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.CHAMELEON, DreamTileShape.SQUARE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.CHAMELEON, DreamTileShape.CIRCLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.CHAMELEON, DreamTileShape.TRIANGLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.JUGGLER, DreamTileShape.SQUARE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.JUGGLER, DreamTileShape.CIRCLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.JUGGLER, DreamTileShape.TRIANGLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.PYRO, DreamTileShape.SQUARE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.PYRO, DreamTileShape.CIRCLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1
newTile = DreamTile(DreamTileFaction.PYRO, DreamTileShape.TRIANGLE)
i = 0
while i < 6:
    mainPile.append(newTile)
    i = i + 1

# create all safe tiles
newTile = DreamTile(DreamTileFaction.SEER, DreamTileShape.SQUARE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.SEER, DreamTileShape.CIRCLE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.SEER, DreamTileShape.TRIANGLE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.CHAMELEON, DreamTileShape.SQUARE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.CHAMELEON, DreamTileShape.CIRCLE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.CHAMELEON, DreamTileShape.TRIANGLE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.JUGGLER, DreamTileShape.SQUARE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.JUGGLER, DreamTileShape.CIRCLE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.JUGGLER, DreamTileShape.TRIANGLE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.PYRO, DreamTileShape.SQUARE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.PYRO, DreamTileShape.CIRCLE, safe=True)
safePile.append(newTile)
newTile = DreamTile(DreamTileFaction.PYRO, DreamTileShape.TRIANGLE, safe=True)
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
    print(safePile.pop(), end=" ")
    i = i + 1

print()
