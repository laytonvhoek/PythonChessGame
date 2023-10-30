
class Tile:

    isOcc = False

    def __init__(self, posx: int, posy: int):
        self.Vispos = None 
        self.posx = posx
        self.posy = posy
        self.posxp = 75 + 50 * posx
        self.posyp = 525 - 50 * posy
        

    def GetPosx(self) -> int:
        return self.posx
    
    def GetPosy(self) -> int:
        return self.posy

    def IsBlack(self) -> bool:
        if (self.posx + self.posy) % 2 == 0:
            return True
        else:
            return False
    def IsOcc(self) -> bool:
        return self.isOcc
        
    def IsWhite(self) -> bool:
        if (self.posx + self.posy) % 2 != 0:
            return True
        else:
            return False
        
        
    def GetVispos(self):
        return self.Vispos
    
    def SetVispos(self, a):
        if a == "off":
            self.Vispos = None
        self.Vispos = a

       
def xytoTiles(x: int, y: int):
    if x in range(1, 9) and y in range(1, 9):
        if y == 1:
            return (x-1)
        else:
            return ((y-1)*8)+(x-1)
    else:
        return 64

Tiles = []
for i in range(1, 9):
    for j in range(1, 9):
        Tiles.append(Tile(j, i))


class pieces:
    def __init__(self, tile: Tile, Colour):
        self.tile = tile
        self.hasmoved = False
        tile.isOcc = True
        self.colour = Colour
        self.check = False
        self.checkfrom = []
        self.pinnedpieces = []

    def GetTile(self):
        return self.tile
    
    def SetTile(self, tile: Tile):
        self.tile = tile

    
    def SetPinnedPiece(self, piece):
        if not piece in self.pinnedpieces:
            self.pinnedpieces.append(piece)

    def RemovePinnedPiece(self, piece):
        try:
            self.pinnedpieces.remove(piece)
        except:
            pass
        

    def MovePeice(self, movetotile: Tile):
        self.hasmoved = True
        self.tile.isOcc = False
        movetotile.isOcc = True
        movetotile.SetVispos(self.tile.GetVispos())
        self.tile.Vispos = None
        self.SetTile(movetotile)

        

        
        
    

        
