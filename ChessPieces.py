from ChessBoard import pieces
from ChessBoard import Tile
from ChessBoard import Tiles
from ChessBoard import xytoTiles

class King(pieces):


    def AvailableTiles(self):
        AList = []
        for i in range(-1, 2):
            for y in range(-1, 2):
                if (self.tile.posx + y <= 8 and self.tile.posy + i >= 1 and self.tile.posy + i <= 8 and self.tile.posx + y >= 1):
                    AList.append(Tiles[xytoTiles(self.tile.posx + y, self.tile.posy + i)])
        return AList

class Queen(pieces):
    def AvailableTiles(self):
        
        AList = []

        for i in range(1, 8):

            if (self.tile.posx + i <= 8 and self.tile.posx + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx + i, self.tile.posy)])

        for i in range(-7, 1):

            if (self.tile.posx + i <= 8 and self.tile.posx + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx + i, self.tile.posy)])

        for i in range(1, 8):

            if (self.tile.posy + i <= 8 and self.tile.posy + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx, self.tile.posy + i)])

        for i in range(-7, 1):

            if (self.tile.posy + i <= 8 and self.tile.posy + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx, self.tile.posy + i)])

        for i in range(1, 8):
            if (self.tile.posx + i <= 8 and self.tile.posy + i <= 8 and self.tile.posx + i >= 1 and self.tile.posy + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx + i, self.tile.posy + i)])

            if (self.tile.posx - i <= 8 and self.tile.posy - i <= 8 and self.tile.posx - i >= 1 and self.tile.posy - i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx - i, self.tile.posy - i)])

            if (self.tile.posx - i <= 8 and self.tile.posy + i <= 8 and self.tile.posx - i >= 1 and self.tile.posy + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx - i, self.tile.posy + i)])

            if (self.tile.posx + i <= 8 and self.tile.posy - i <= 8 and self.tile.posx + i >= 1 and self.tile.posy - i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx + i, self.tile.posy - i)])

        return AList
    
class Bishop(pieces):
    def AvailableTiles(self):

        AList = []

        for i in range(1, 8):
            if (self.tile.posx + i <= 8 and self.tile.posy + i <= 8 and self.tile.posx + i >= 1 and self.tile.posy + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx + i, self.tile.posy + i)])

            if (self.tile.posx - i <= 8 and self.tile.posy - i <= 8 and self.tile.posx - i >= 1 and self.tile.posy - i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx - i, self.tile.posy - i)])

            if (self.tile.posx - i <= 8 and self.tile.posy + i <= 8 and self.tile.posx - i >= 1 and self.tile.posy + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx - i, self.tile.posy + i)])

            if (self.tile.posx + i <= 8 and self.tile.posy - i <= 8 and self.tile.posx + i >= 1 and self.tile.posy - i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx + i, self.tile.posy - i)])

        return AList
    
class Rook(pieces):
    def AvailableTiles(self):
        
        AList = []

        for i in range(-7, 8):
            if (self.tile.posx + i <= 8 and self.tile.posx + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx + i, self.tile.posy)])

        for i in range(-7, 8):
            if (self.tile.posy + i <= 8 and self.tile.posy + i >= 1):
                AList.append(Tiles[xytoTiles(self.tile.posx, self.tile.posy + i)])

        return AList
    
class Knight(pieces):
    def AvailableTiles(self):

        AList = []

        if self.tile.posy + 1 >= 1 and self.tile.posy + 1 <= 8:

            if self.tile.posx + 2 >= 1 and self.tile.posx + 2 <= 8:
                AList.append(Tiles[xytoTiles(self.tile.posx + 2, self.tile.posy + 1)])
            if self.tile.posx - 2 >= 1 and self.tile.posx - 2 <= 8:
                AList.append(Tiles[xytoTiles(self.tile.posx - 2, self.tile.posy + 1)])

        if self.tile.posy - 1 >= 1 and self.tile.posy - 1 <= 8:

            if self.tile.posx + 2 >= 1 and self.tile.posx + 2 <= 8:
                AList.append(Tiles[xytoTiles(self.tile.posx + 2, self.tile.posy - 1)])
            if self.tile.posx - 2 >= 1 and self.tile.posx - 2 <= 8:
                AList.append(Tiles[xytoTiles(self.tile.posx - 2, self.tile.posy - 1)])

        if self.tile.posy + 2 >= 1 and self.tile.posy + 2 <= 8:
            
            if self.tile.posx + 1 >= 1 and self.tile.posx + 1 <= 8:
                AList.append(Tiles[xytoTiles(self.tile.posx + 1, self.tile.posy + 2)])
            if self.tile.posx - 1 >= 1 and self.tile.posx - 1 <= 8:
                AList.append(Tiles[xytoTiles(self.tile.posx - 1, self.tile.posy + 2)])

        if self.tile.posy - 2 >= 1 and self.tile.posy - 2 <= 8:

            if self.tile.posx + 1 >= 1 and self.tile.posx + 1 <= 8:
                AList.append(Tiles[xytoTiles(self.tile.posx + 1, self.tile.posy - 2)])
            if self.tile.posx - 1 >= 1 and self.tile.posx - 1 <= 8:
                AList.append(Tiles[xytoTiles(self.tile.posx - 1, self.tile.posy - 2)])
            
        return AList

class Pawn(pieces):
    def AvailableTiles(self):

        AList = []

        if self.hasmoved == False:
            if self.colour == "White" and Tiles[xytoTiles(self.tile.posx, self.tile.posy + 2)].GetVispos() == None:
                AList.append(Tiles[xytoTiles(self.tile.posx, self.tile.posy + 2)])
            if self.colour == "Black" and Tiles[xytoTiles(self.tile.posx, self.tile.posy - 2)].GetVispos() == None:
                AList.append(Tiles[xytoTiles(self.tile.posx, self.tile.posy - 2)])
        
        if self.colour == "White" and Tiles[xytoTiles(self.tile.posx, self.tile.posy + 1)].GetVispos() == None:
            AList.append(Tiles[xytoTiles(self.tile.posx, self.tile.posy + 1)])

        if self.colour == "Black" and Tiles[xytoTiles(self.tile.posx, self.tile.posy - 1)].GetVispos() == None:
            AList.append(Tiles[xytoTiles(self.tile.posx, self.tile.posy - 1)])

        try:   
            if self.colour == "White" and Tiles[xytoTiles(self.tile.posx + 1, self.tile.posy + 1)].GetVispos() != None:
                AList.append(Tiles[xytoTiles(self.tile.posx + 1, self.tile.posy + 1)])
        except:
            pass
        try:
            if self.colour == "White" and Tiles[xytoTiles(self.tile.posx - 1, self.tile.posy + 1)].GetVispos() != None:
                AList.append(Tiles[xytoTiles(self.tile.posx - 1, self.tile.posy + 1)])
        except:
            pass
        try:
            if self.colour == "Black" and Tiles[xytoTiles(self.tile.posx - 1, self.tile.posy - 1)].GetVispos() != None:
                AList.append(Tiles[xytoTiles(self.tile.posx - 1, self.tile.posy - 1)])
        except:
            pass
        try:
            if self.colour == "Black" and Tiles[xytoTiles(self.tile.posx + 1, self.tile.posy - 1)].GetVispos() != None:
                AList.append(Tiles[xytoTiles(self.tile.posx + 1, self.tile.posy - 1)])
        except:
            pass

        return AList
