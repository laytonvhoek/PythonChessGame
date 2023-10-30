import pygame 
import time
from ChessBoard import Tiles
from ChessBoard import xytoTiles
from ChessPieces import King
from ChessPieces import Queen
from ChessPieces import Bishop
from ChessPieces import Rook
from ChessPieces import Knight
from ChessPieces import Pawn
from ChessPieces import Tile
from ChessBoard import pieces
from ChessPieces import King
from ChessPieces import Queen
from ChessPieces import Bishop
from ChessPieces import Rook
from ChessPieces import Knight
import time

HorsebImage = pygame.image.load("images/Chess_ndt60.png")
RookbImage = pygame.image.load("images/Chess_rdt60.png")
BishopbImage = pygame.image.load("images/Chess_bdt60.png")
QueenbImage = pygame.image.load("images/Chess_qdt60.png")
KingbImage = pygame.image.load("images/Chess_kdt60.png")
PawnbImage = pygame.image.load("images/Chess_pdt60.png")
PawnwImage = pygame.image.load("images/Chess_plt60.png")
HorsewImage = pygame.image.load("images/Chess_nlt60.png")
RookwImage = pygame.image.load("images/Chess_rlt60.png")
BishopwImage = pygame.image.load("images/Chess_blt60.png")
QueenwImage = pygame.image.load("images/Chess_qlt60.png")
KingwImage = pygame.image.load("images/Chess_klt60.png")

board_width = 1024
board_height = 1024
FPS = 30

AllPeices = []

screen = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Chess")
WhitePieces = []

WKing = King(Tiles[4], "White")
WhitePieces.append(WKing)
WQueen = Queen(Tiles[3], "White")
WhitePieces.append(WQueen)
WBishop1 = Bishop(Tiles[2], "White")
WhitePieces.append(WBishop1)
WBishop2 = Bishop(Tiles[5], "White")
WhitePieces.append(WBishop2)
WKnight1 = Knight(Tiles[1], "White")
WhitePieces.append(WKnight1)
WKnight2 = Knight(Tiles[6], "White")
WhitePieces.append(WKnight2)
WRook1 = Rook(Tiles[0], "White")
WhitePieces.append(WRook1)
WRook2 = Rook(Tiles[7], "White")
WhitePieces.append(WRook2)
for i in range(8):
    WhitePieces.append(Pawn(Tiles[8 + i], "White"))

BlackPieces = []
BKing = King(Tiles[60], "Black")
BlackPieces.append(BKing)
BQueen = Queen(Tiles[59], "Black")
BlackPieces.append(BQueen)
BBishop1 = Bishop(Tiles[58], "Black")
BlackPieces.append(BBishop1)
BBishop2 = Bishop(Tiles[61], "Black")
BlackPieces.append(BBishop2)
BKnight1 = Knight(Tiles[57], "Black")
BlackPieces.append(BKnight1)
BKnight2 = Knight(Tiles[62], "Black")
BlackPieces.append(BKnight2)
BRook1 = Rook(Tiles[56], "Black")
BlackPieces.append(BRook1)
BRook2 = Rook(Tiles[63], "Black")
BlackPieces.append(BRook2)

for i in range(8):
    BlackPieces.append(Pawn(Tiles[48 + i], "Black"))

def ValidSquares(piece: pieces, List: list,):
    VSlist = []
    Fsquares = []

    for i in range(len(List)):
        if List[i].GetPosx() != piece.tile.GetPosx() or List[i].GetPosy() != piece.tile.GetPosy():
            VSlist.append(List[i])
    
    
    for vs in VSlist:
        for bp in BlackPieces:
            if bp.tile == vs:
                if piece.colour == "Black":
                    Fsquares.append(vs)

        for wp in WhitePieces:
            if wp.tile == vs:
                if piece.colour == "White":
                    Fsquares.append(vs)


    for i in range(1,9):
        try:
            if Tiles[xytoTiles(piece.tile.GetPosx() + i, piece.tile.GetPosy() + i)].GetVispos() != None:
                #print(f"Tile At {piece.tile.GetPosx() + i}, {piece.tile.GetPosy() + i} Is Occ.")
                #print(piece)
                for f in range(i+1, 8):
                    try:
                        VSlist.remove(Tiles[xytoTiles(piece.tile.GetPosx() + f, piece.tile.GetPosy() + f)])
                    except:
                        continue
                
        except:
            break
    for i in range(1,9):
        try:
            if Tiles[xytoTiles(piece.tile.GetPosx() - i, piece.tile.GetPosy() - i)].GetVispos() != None:
                #print(f"Tile At {piece.tile.GetPosx() - i}, {piece.tile.GetPosy() - i} Is Occ.")
                #print(piece)
                for f in range(i+1, 8):
                    try:
                        VSlist.remove(Tiles[xytoTiles(piece.tile.GetPosx() - f, piece.tile.GetPosy() - f)])
                    except:
                        continue

        except:
            break
    for i in range(1,9):
        try:
            if Tiles[xytoTiles(piece.tile.GetPosx() - i, piece.tile.GetPosy() + i)].GetVispos() != None:
                #print(f"Tile At {piece.tile.GetPosx() - i}, {piece.tile.GetPosy() + i} Is Occ.")
                #print(piece)
                for f in range(i+1, 8):
                    try:
                        VSlist.remove(Tiles[xytoTiles(piece.tile.GetPosx() - f, piece.tile.GetPosy() + f)])
                    except:
                        continue
        except:
            break
    for i in range(1,9):
        try:
            if Tiles[xytoTiles(piece.tile.GetPosx() + i, piece.tile.GetPosy() - i)].GetVispos() != None:
                #print(f"Tile At {piece.tile.GetPosx() + i}, {piece.tile.GetPosy() - i} Is Occ.")
                #print(piece)
                for f in range(i+1, 8):
                    try:
                        VSlist.remove(Tiles[xytoTiles(piece.tile.GetPosx() + f, piece.tile.GetPosy() - f)])
                    except:
                        continue
        except:
            break
    for i in range(1,9):
        try:
            if Tiles[xytoTiles(piece.tile.GetPosx(), piece.tile.GetPosy() - i)].GetVispos() != None:
                #print(f"Tile At {piece.tile.GetPosx()}, {piece.tile.GetPosy() - i} Is Occ.")
                #print(piece)
                for f in range(i+1, 8):
                    try:
                        VSlist.remove(Tiles[xytoTiles(piece.tile.GetPosx(), piece.tile.GetPosy() - f)])
                    except:
                        continue
        except:
            break
    for i in range(1,9):
        try:
            if Tiles[xytoTiles(piece.tile.GetPosx(), piece.tile.GetPosy() + i)].GetVispos() != None:
                #print(f"Tile At {piece.tile.GetPosx()}, {piece.tile.GetPosy() + i} Is Occ.")
                #print(piece)
                for f in range(i+1, 8):
                    try:
                        VSlist.remove(Tiles[xytoTiles(piece.tile.GetPosx(), piece.tile.GetPosy() + f)])
                    except:
                        continue
        except:
            break
    for i in range(1,9):
        try:
            if Tiles[xytoTiles(piece.tile.GetPosx() + i, piece.tile.GetPosy())].GetVispos() != None:
                #print(f"Tile At {piece.tile.GetPosx() + i}, {piece.tile.GetPosy()} Is Occ.")
                #print(piece)
                for f in range(i+1, 8):
                    try:
                        VSlist.remove(Tiles[xytoTiles(piece.tile.GetPosx() + f, piece.tile.GetPosy())])
                    except:
                        continue
        except:
            break
    for i in range(1,9):
        try:
            if Tiles[xytoTiles(piece.tile.GetPosx() - i, piece.tile.GetPosy())].GetVispos() != None:
                #print(f"Tile At {piece.tile.GetPosx() - i}, {piece.tile.GetPosy()} Is Occ.")
                #print(piece)
                for f in range(i+1, 8):
                    try:
                        VSlist.remove(Tiles[xytoTiles(piece.tile.GetPosx() - f, piece.tile.GetPosy())])
                    except:
                        continue
        except:
            break
        

    for friendly in Fsquares:
        try:
            VSlist.remove(friendly)
        except:
            continue



    return VSlist



def ShowAvailableSquares(peice: pieces, screen, king: King):
    ListA = []
    Circles = []
    ListA = ValidSquares(peice, peice.AvailableTiles())

    if peice in king.pinnedpieces:
        for lista in ListA:
            try:
                print(f"x: {king.checkfrom[0].tile.GetPosx()} y: {king.checkfrom[0].tile.GetPosy()} CODE: X001")
            except:
                continue
            if len(king.checkfrom) == 1 and lista == king.checkfrom[0].tile:
                    circle = pygame.draw.circle(screen, (255, 0, 0), (lista.posxp, lista.posyp), 10)
                    Circles.append(circle)


        return Circles

    if king.check == True and type(peice) != King and len(king.checkfrom) < 2:
        for l in king.checkfrom:
            for lista in ListA:
                if lista == l.tile:
                    circle = pygame.draw.circle(screen, (255, 0, 0), (lista.posxp, lista.posyp), 10)
                    Circles.append(circle)
            for lista in ListA:
                for a in ValidSquares(l, l.AvailableTiles()):
                    if l.tile.GetPosx() > king.tile.GetPosx():
                        if (a.GetPosx() in range(king.tile.GetPosx(), l.tile.GetPosx())) and (a.GetPosy() in range(l.tile.GetPosy(), king.tile.GetPosy())):
                            if lista == a:
                                circle = pygame.draw.circle(screen, (192, 192, 192), (lista.posxp, lista.posyp), 10)
                                Circles.append(circle)
                    else:
                        if (a.GetPosx() in range(l.tile.GetPosx(), king.tile.GetPosx())) and (a.GetPosy() in range(l.tile.GetPosy(), king.tile.GetPosy())):
                            if lista == a:
                                circle = pygame.draw.circle(screen, (192, 192, 192), (lista.posxp, lista.posyp), 10)
                                Circles.append(circle)

                    if l.tile.GetPosx() > king.tile.GetPosx():
                        if (a.GetPosy() in range(king.tile.GetPosx(), l.tile.GetPosx())) and (a.GetPosy() in range(king.tile.GetPosy(), l.tile.GetPosy())):
                            if lista == a:
                                circle = pygame.draw.circle(screen, (192, 192, 192), (lista.posxp, lista.posyp), 10)
                                Circles.append(circle)
                    else:
                        if (a.GetPosx() in range(l.tile.GetPosx(), king.tile.GetPosx())) and (a.GetPosy() in range(king.tile.GetPosy(), l.tile.GetPosy())):
                            if lista == a:
                                circle = pygame.draw.circle(screen, (192, 192, 192), (lista.posxp, lista.posyp), 10)
                                Circles.append(circle)

                        

        return Circles
    
    if king.check == True and type(peice) == King:
        for checkingpiece in king.checkfrom:
            for a in ValidSquares(checkingpiece, checkingpiece.AvailableTiles()):
                for lista in ListA:
                    if lista == a:
                        ListA.remove(a)
                        
    for things in ListA:
        circle = pygame.draw.circle(screen, (192, 192, 192,), (things.posxp, things.posyp), 10)
        if things.IsOcc():
            circle = pygame.draw.circle(screen, (255, 0, 0), (things.posxp, things.posyp), 10)
        Circles.append(circle)
    
    return Circles

def RemoveAvailableSqaures(Circles):
        for tile in Tiles:
            for circle in Circles:
                if circle.center == ((tile.posxp, tile.posyp)):
                    if tile.IsWhite():
                        pygame.draw.circle(screen, (255,255,255), circle.center, 10)
                    if tile.IsBlack():
                        pygame.draw.circle(screen, (142,142,142), circle.center, 10)


def reprint(piece: pieces, VisualTile: Tile):
    if piece.colour == "Black":
        if type(piece) == King:
            Placeking(VisualTile, VisualTile.GetVispos(), "Black")
        if type(piece) == Rook:
            Placerook(VisualTile, VisualTile.GetVispos(), "Black")
        if type(piece) == Bishop:
            Placebishop(VisualTile, VisualTile.GetVispos(), "Black")
        if type(piece) == Knight:
            Placehorse(VisualTile, VisualTile.GetVispos(), "Black")
        if type(piece) == Queen:
            Placequeen(VisualTile, VisualTile.GetVispos(), "Black")
        if type(piece) == Pawn:
            Placepawn(VisualTile, VisualTile.GetVispos(), "Black")
    else:
        if type(piece) == King:
            Placeking(VisualTile, VisualTile.GetVispos(), "White")
        if type(piece) == Rook:
            Placerook(VisualTile, VisualTile.GetVispos(), "White")
        if type(piece) == Bishop:
            Placebishop(VisualTile, VisualTile.GetVispos(), "White")
        if type(piece) == Knight:
            Placehorse(VisualTile, VisualTile.GetVispos(), "White")
        if type(piece) == Queen:
            Placequeen(VisualTile, VisualTile.GetVispos(), "White")
        if type(piece) == Pawn:
            Placepawn(VisualTile, VisualTile.GetVispos(), "White")

def CanCastleLeft(King: King):
    if King.hasmoved == True:
        return False
    if King.colour == "White":
        if  not (Tiles[xytoTiles(King.tile.GetPosx() - 1, King.tile.GetPosy())].IsOcc() or Tiles[xytoTiles(King.tile.GetPosx() - 2, King.tile.GetPosy())].IsOcc() or Tiles[xytoTiles(King.tile.GetPosx() - 3, King.tile.GetPosy())].IsOcc()):
            for wp in WhitePieces:
                if type(wp) == Rook and wp.tile == Tiles[xytoTiles(King.tile.GetPosx() - 4, King.tile.GetPosy())]:
                    return True
    if King.colour == "Black":
        if  not (Tiles[xytoTiles(King.tile.GetPosx() -1, King.tile.GetPosy())].IsOcc() or Tiles[xytoTiles(King.tile.GetPosx() -2, King.tile.GetPosy())].IsOcc() or Tiles[xytoTiles(King.tile.GetPosx() - 3, King.tile.GetPosy())].IsOcc()):
            for wp in BlackPieces:
                if type(wp) == Rook and wp.tile == Tiles[xytoTiles(King.tile.GetPosx() - 4, King.tile.GetPosy())]:
                    return True
                
    return False

def CanCastleRight(King: King):
    if King.hasmoved == True:
        return False
    if King.colour == "White":
        if  not (Tiles[xytoTiles(King.tile.GetPosx() + 1, King.tile.GetPosy())].IsOcc() or Tiles[xytoTiles(King.tile.GetPosx() + 2, King.tile.GetPosy())].IsOcc()):
            for wp in WhitePieces:
                if type(wp) == Rook and wp.tile == Tiles[xytoTiles(King.tile.GetPosx() + 3, King.tile.GetPosy())]:
                    return True
    if King.colour == "Black":
        if  not (Tiles[xytoTiles(King.tile.GetPosx() + 1, King.tile.GetPosy())].IsOcc() or Tiles[xytoTiles(King.tile.GetPosx() + 2, King.tile.GetPosy())].IsOcc()):
            for wp in BlackPieces:
                if type(wp) == Rook and wp.tile == Tiles[xytoTiles(King.tile.GetPosx() + 3, King.tile.GetPosy())]:
                    return True
    return False


def IsCheckMate(piece: pieces):
    if len(ValidSquares(piece, piece.AvailableTiles())) == 0:
        return True
    
    else:
        return False

def Placerook(Tile: Tile, rect, colour):
        Rookb1 = rect
        if colour == "White":
            StretchHorseb = pygame.transform.scale(RookwImage,(45,45))
            screen.blit(StretchHorseb, Rookb1)

        if colour == "Black":
            StretchHorseb = pygame.transform.scale(RookbImage,(45,45))
            screen.blit(StretchHorseb, Rookb1)

        Tile.SetVispos(Rookb1)
        return Rookb1

def Placehorse(Tile: Tile, rect, colour):
        Horseb1 = rect
        if colour == "White":
            StretchHorseb = pygame.transform.scale(HorsewImage,(45,45))
            screen.blit(StretchHorseb, Horseb1)

        if colour == "Black":
            StretchHorseb = pygame.transform.scale(HorsebImage,(45,45))
            screen.blit(StretchHorseb, Horseb1)

        Tile.SetVispos(Horseb1)
        return Horseb1

def Placebishop(Tile: Tile, rect, colour):
        Bishopb1 = rect
        if colour == "White":
            StretchHorseb = pygame.transform.scale(BishopwImage,(45,45))
            screen.blit(StretchHorseb, Bishopb1)

        if colour == "Black":
            StretchHorseb = pygame.transform.scale(BishopbImage,(45,45))
            screen.blit(StretchHorseb, Bishopb1)
        Tile.SetVispos(Bishopb1)
        return Bishopb1

def Placequeen(Tile: Tile, rect, colour):
        Queenb1 = rect
        if colour == "White":
            StretchHorseb = pygame.transform.scale(QueenwImage,(45,45))
            screen.blit(StretchHorseb, Queenb1)

        if colour == "Black":
            StretchHorseb = pygame.transform.scale(QueenbImage,(45,45))
            screen.blit(StretchHorseb, Queenb1)
        Tile.SetVispos(Queenb1)
        return Queenb1

def Placeking(Tile: Tile, rect, colour):
        Kingb1 = rect
        if colour == "White":
            StretchHorseb = pygame.transform.scale(KingwImage,(45,45))
            screen.blit(StretchHorseb, Kingb1)

        if colour == "Black":
            StretchHorseb = pygame.transform.scale(KingbImage,(45,45))
            screen.blit(StretchHorseb, Kingb1)
        Tile.SetVispos(Kingb1)
        return Kingb1

def Placepawn(Tile: Tile, rect, colour):
        Pawnw = rect
        if colour == "White":
            StretchHorseb = pygame.transform.scale(PawnwImage,(45,45))
            screen.blit(StretchHorseb, Pawnw)

        if colour == "Black":
            StretchHorseb = pygame.transform.scale(PawnbImage,(45,45))
            screen.blit(StretchHorseb, Pawnw)
        Tile.SetVispos(Pawnw)
        return Pawnw


def main():
    conts = 0
    for i in range(1, 65):
        square = pygame.Rect(100 + (i % 8)*50, 100 + 50*conts, 50, 50)
        if (i + conts) % 2:
            pygame.draw.rect(screen, (142,142,142), square)
        else:
            pygame.draw.rect(screen, (255,255,255), square)
        if i % 8 == 0:
            conts+=1

    conts = 0
    for i in range (1, 65):
        if i == 1:
            Rookb1 =  pygame.Rect(100, 100, 50, 50)
            StretchRookb = pygame.transform.scale(RookbImage,(45,45))
            screen.blit(StretchRookb, Rookb1)
            AllPeices.append(Rookb1)
            Tiles[55+i].SetVispos(Rookb1)

        if i == 2: 
            Horseb1 = pygame.Rect(150, 100, 50, 50)
            StretchHorseb = pygame.transform.scale(HorsebImage,(45,45))
            screen.blit(StretchHorseb, Horseb1)
            AllPeices.append(Horseb1)
            Tiles[55+i].SetVispos(Horseb1)

        if i == 3:
            Bishopb1 = pygame.Rect(200, 100, 50, 50)
            StretchBishopb = pygame.transform.scale(BishopbImage,(45,45))
            screen.blit(StretchBishopb, Bishopb1)
            AllPeices.append(Bishopb1)
            Tiles[55+i].SetVispos(Bishopb1)
        if i == 4:
            Queenb1 = pygame.Rect(250, 100, 50, 50)
            StretchQueenb = pygame.transform.scale(QueenbImage,(48,46))
            screen.blit(StretchQueenb, Queenb1)
            AllPeices.append(Queenb1)
            Tiles[55+i].SetVispos(Queenb1)
        if i == 5:
            Kingb1 = pygame.Rect(300, 100, 50, 50)
            StretchKingb = pygame.transform.scale(KingbImage,(48,46))
            screen.blit(StretchKingb, Kingb1)
            AllPeices.append(Kingb1)
            Tiles[55+i].SetVispos(Kingb1)
        if i == 6:
            Bishopb2 = pygame.Rect(350, 100, 50, 50)
            StretchBishopb = pygame.transform.scale(BishopbImage,(45,45))
            screen.blit(StretchBishopb, Bishopb2)
            AllPeices.append(Bishopb2)
            Tiles[55+i].SetVispos(Bishopb2)
        if i == 7:
            Horseb2 = pygame.Rect(400, 100, 50, 50)
            StretchHorseb = pygame.transform.scale(HorsebImage,(45,45))
            screen.blit(StretchHorseb, Horseb2)
            AllPeices.append(Horseb2)
            Tiles[55+i].SetVispos(Horseb2)
        if i == 8:
            Rookb2 =  pygame.Rect(450, 100, 50, 50)
            StretchRookb = pygame.transform.scale(RookbImage,(45,45))
            screen.blit(StretchRookb, Rookb2)
            AllPeices.append(Rookb2)
            Tiles[55+i].SetVispos(Rookb2)
        if i == 57:
            Rookw1 =  pygame.Rect(100, 100 +50*7, 50, 50)
            StretchRookw = pygame.transform.scale(RookwImage,(45,45))
            screen.blit(StretchRookw, Rookw1)
            AllPeices.append(Rookw1)
            Tiles[-57+i].SetVispos(Rookw1)
        if i == 58: 
            Horsew1 = pygame.Rect(150, 100 +50*7, 50, 50)
            StretchHorsew = pygame.transform.scale(HorsewImage,(45,45))
            screen.blit(StretchHorsew, Horsew1)
            AllPeices.append(Horsew1)
            Tiles[-57+i].SetVispos(Horsew1)
        if i == 59:
            Bishopw1 = pygame.Rect(200, 100 +50*7, 50, 50)
            StretchBishopw = pygame.transform.scale(BishopwImage,(45,45))
            screen.blit(StretchBishopw, Bishopw1)
            AllPeices.append(Bishopw1)
            Tiles[-57+i].SetVispos(Bishopw1)
        if i == 60:
            Queenw1 = pygame.Rect(250, 100 +50*7, 50, 50)
            StretchQueenw = pygame.transform.scale(QueenwImage,(45,45))
            screen.blit(StretchQueenw, Queenw1)
            AllPeices.append(Queenw1)
            Tiles[-57+i].SetVispos(Queenw1)
        if i == 61:
            Kingw1 = pygame.Rect(300, 100 +50*7, 50, 50)
            StretchKingw = pygame.transform.scale(KingwImage,(45,45))
            screen.blit(StretchKingw, Kingw1)
            AllPeices.append(Kingw1)
            Tiles[-57+i].SetVispos(Kingw1)
        if i == 62:
            Bishopw2 = pygame.Rect(350, 100 +50*7, 50, 50)
            StretchBishopw = pygame.transform.scale(BishopwImage,(45,45))
            screen.blit(StretchBishopw, Bishopw2)
            AllPeices.append(Bishopw2)
            Tiles[-57+i].SetVispos(Bishopw2)
        if i == 63:
            Horsew2 = pygame.Rect(400, 100 +50*7, 50, 50)
            StretchHorsew = pygame.transform.scale(HorsewImage,(45,45))
            screen.blit(StretchHorsew, Horsew2)
            AllPeices.append(Horsew2)
            Tiles[-57+i].SetVispos(Horsew2)
        if i == 64:
            Rookw2 =  pygame.Rect(100 + 7*50, 100 +50*7, 50, 50)
            StretchRookw = pygame.transform.scale(RookwImage,(45,45))
            screen.blit(StretchRookw, Rookw2)
            AllPeices.append(Rookw2)
            Tiles[-57+i].SetVispos(Rookw2)


        if(i == 48):
            for j in range(8):
                Pawnw =  pygame.Rect(100 + j%8*50, 100 + 300, 50, 50)
                StretchPawnw = pygame.transform.scale(PawnwImage,(45,45))
                screen.blit(StretchPawnw, Pawnw)
                AllPeices.append(Pawnw)
                Tiles[8+j].SetVispos(Pawnw)


        if(i == 8):
            for j in range(8):
                Pawnb =  pygame.Rect(100 + j%8*50, 100 + 50, 50, 50)
                StretchPawnb = pygame.transform.scale(PawnbImage,(45,45))
                screen.blit(StretchPawnb, Pawnb)
                AllPeices.append(Pawnb)
                Tiles[56-i+j].SetVispos(Pawnb)
        
    ShownTiles = []
    clock = pygame.time.Clock()
    run = True
    clicked = True
    WhiteTurn = True


    while run:
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                MousePos = event.pos
                

                if not clicked:
                    RemoveAvailableSqaures(ShownTiles)
                    for stile in ShownTiles:                        
                        if stile.collidepoint(MousePos):
                            for VisualTile in Tiles:
                                if stile.center == ((VisualTile.posxp, VisualTile.posyp)):
                 
                                    print(f"lastpiece: {type(lastpiece).__name__} at x: {lastpiece.tile.GetPosx()} y: {lastpiece.tile.GetPosy()} of colour Black: {lastpiece.tile.IsBlack()} of colour White: {lastpiece.tile.IsWhite()} , moving to: {VisualTile.GetPosx()}, {VisualTile.GetPosy()}")
                                    square = pygame.Rect(lastpiece.tile.posxp -25, lastpiece.tile.posyp -25, 50, 50)


                                    if lastpiece.tile.IsBlack():
                                        colour = (142,142,142)

                                    if lastpiece.tile.IsWhite():
                                        colour = (255,255,255)

                                    if VisualTile.IsBlack():
                                        VTcolour = (142,142,142)

                                    if VisualTile.IsWhite():
                                        VTcolour = (255,255,255)

                                    if VisualTile.GetVispos() != None:
                                        squarefortakingp = pygame.Rect(VisualTile.posxp - 25, VisualTile.posyp - 25, 50, 50)
                                        for bp in BlackPieces:
                                            if bp.tile  == VisualTile:
                                                pygame.draw.rect(screen, VTcolour, squarefortakingp)
                                                AllPeices.remove(VisualTile.GetVispos())
                                                BlackPieces.remove(bp)
                                        for wp in WhitePieces:
                                            if wp.tile == VisualTile:
                                                pygame.draw.rect(screen, VTcolour, squarefortakingp)
                                                AllPeices.remove(VisualTile.GetVispos())
                                                WhitePieces.remove(wp)
  
                                    lastpiece.MovePeice(VisualTile)
                                    lastpiece.tile.GetVispos().left = VisualTile.posxp
                                    lastpiece.tile.GetVispos().top = VisualTile.posyp
                                    LastTile = lastpiece.tile.GetVispos()
                                    LastTile.left += -25
                                    LastTile.top += -25




                                    if type(lastpiece) == King:
                                        Placeking(VisualTile, lastpiece.tile.GetVispos(), lastpiece.colour)
                                    if type(lastpiece) == Rook:
                                        Placerook(VisualTile, lastpiece.tile.GetVispos(), lastpiece.colour)
                                    if type(lastpiece) == Bishop:
                                        Placebishop(VisualTile, lastpiece.tile.GetVispos(), lastpiece.colour)
                                    if type(lastpiece) == Knight:
                                        Placehorse(VisualTile, lastpiece.tile.GetVispos(), lastpiece.colour)
                                    if type(lastpiece) == Queen:
                                        Placequeen(VisualTile, lastpiece.tile.GetVispos(), lastpiece.colour)
                                    if type(lastpiece) == Pawn:
                                        Placepawn(VisualTile, lastpiece.tile.GetVispos(), lastpiece.colour)

     
                                    WhiteTurn = not WhiteTurn
                                    
                                  
                                    pygame.draw.rect(screen, colour, square)

                                    if type(lastpiece) == Pawn:
                                        if lastpiece.colour == "White":
                                            if VisualTile.posy == 8:
                                                pygame.draw.rect(screen, VTcolour, squarefortakingp)
                                                WhitePieces.remove(lastpiece)
                                                newqueen = Queen(VisualTile, lastpiece.colour)
                                                WhitePieces.append(newqueen)
                                                Placequeen(VisualTile, squarefortakingp, lastpiece.colour)
                                                AllPeices.append(squarefortakingp)

                                                
                                        if lastpiece.colour == "Black":
                                            if VisualTile.posy == 1:
                                                
                                                pygame.draw.rect(screen, VTcolour, squarefortakingp)
                                                BlackPieces.remove(lastpiece)
                                                newqueen = Queen(VisualTile, lastpiece.colour)
                                                BlackPieces.append(newqueen)
                                                Placequeen(VisualTile, VisualTile.GetVispos(), lastpiece.colour)
                                                AllPeices.append(squarefortakingp)
 
                                    

                    
                    clicked = True

  
                                    
                    # print(f"{WKing.pinnedpieces} pinned by WhiteKing")
                    # print(f"{BKing.pinnedpieces} pinned by BlackKing")
                    # for i in range(len(Tiles)):
                    #     print(f"Tile #{i+1}: {Tiles[i].GetVispos()}")
                    # print(f"White King pinned pieces: {WKing.pinnedpieces}")
                    # print(f"Black King pinned pieces: {BKing.pinnedpieces}")
                    # for p in range(len(AllPeices)):
                    #     print(f"Piece #{p+1}: {AllPeices[p]}")
                    for s in range(len(WhitePieces)):
                        print(f"White Object #{s+1}: check:{WhitePieces[s].check}")
                    for s in range(len(BlackPieces)):
                        print(f"Black Object #{s+1}: check:{BlackPieces[s].check}")
                    

                    # print("-------------DONE-----------------")
                    # print("White Can Castle Left: ", CanCastleLeft(WKing))
                    # print("Black Can Castle Left: ", CanCastleLeft(BKing))
                    # print("White Can Castle Right: ", CanCastleRight(WKing))
                    # print("Black Can Castle Right: ", CanCastleRight(BKing))


                if clicked:
                    if WhiteTurn:
                        for piece in AllPeices:
                            if piece.collidepoint(MousePos):
                                for tile in Tiles:
                                    if piece == tile.GetVispos():
                                        for whitepiece in WhitePieces:
                                            if whitepiece.GetTile() == tile:
                                                ShownTiles = ShowAvailableSquares(whitepiece, screen, WKing)
                                                # print(type(whitepiece))
                                                # print(whitepiece.colour)
                                                # print(f"{tile.posx}, {tile.posy}")
                                                # print(f"{whitepiece.GetTile().posx}, {whitepiece.GetTile().posy}")
                                                lastpiece = whitepiece
                                                clicked = False

                    else:
                        for piece in AllPeices:
                            if piece.collidepoint(MousePos):
                                for tile in Tiles:
                                    if piece == tile.GetVispos():
                                        for blackpiece in BlackPieces:
                                            if blackpiece.GetTile() == tile:
                                                ShownTiles = ShowAvailableSquares(blackpiece, screen, BKing)
                                                # print(type(blackpiece))
                                                # print(blackpiece.colour)
                                                # print(f"{tile.posx}, {tile.posy}")
                                                # print(f"{blackpiece.GetTile().posx}, {whitepiece.GetTile().posy}")
                                                lastpiece = blackpiece
                                                clicked = False


                                                
                    for p in WhitePieces:
                        checklist = []
                        p.check = False
                        p.checkfrom = []
                            
                        for bp in BlackPieces:
                            for a in ValidSquares(bp, bp.AvailableTiles()):
                                if p.tile == a:
                                    p.check = True
                            
                                    checklist.append(bp)
                                    p.checkfrom = checklist
                                    
                    for p in BlackPieces:
                        checklist = []
                        p.check = False
                        p.checkfrom = []

                        for bp in WhitePieces:
                            for a in ValidSquares(bp, bp.AvailableTiles()):
                                if p.tile == a:
                                    p.check = True
                
                                    checklist.append(bp)
                                    p.checkfrom = checklist

                   

                    for whitep in WhitePieces:
                        for a in whitep.checkfrom:
                            saveVP = whitep.tile.GetVispos()
                            whitep.tile.SetVispos(None)
                            for wp in WhitePieces:
                                if wp.tile in ValidSquares(a, a.AvailableTiles()):
                                    if wp != whitep:
                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        wp.SetPinnedPiece(whitep)
                                else:
                                    if type(wp) == King:
                                        print(f"CODE: X003 {type(a).__name__}")
                                    wp.RemovePinnedPiece(whitep)
                                    print("CODE: X002")                            

                            whitep.tile.SetVispos(saveVP)

                    for blackp in BlackPieces:
                        for a in blackp.checkfrom:
                            saveVP = blackp.tile.GetVispos()
                            blackp.tile.SetVispos(None)
                            for bp in BlackPieces:
                                if bp.tile in ValidSquares(a, a.AvailableTiles()):
                                    if bp != blackp:
                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        bp.SetPinnedPiece(blackp)
                                else:
                                    if type(bp) == King:
                                        print(f"CODE: X003: {type(a).__name__}")
                                    bp.RemovePinnedPiece(blackp)
                                    print("CODE: X002")
                                            


                            blackp.tile.SetVispos(saveVP)
                                    


                            




                                                
                    for w in WhitePieces:
                        print(f"White Peice: {type(w).__name__} (x: {w.tile.GetPosx()} y: {w.tile.GetPosy()}), check from: {w.checkfrom} pinning {w.pinnedpieces}")
                    for w in BlackPieces:
                        print(f"Black Peice: {type(w).__name__} (x: {w.tile.GetPosx()} y: {w.tile.GetPosy()}), check from: {w.checkfrom} pinning {w.pinnedpieces}")

                    print("-------------DONE-----------------")
                    


                    
                
        
                for tile in Tiles:
                    for wp in WhitePieces:
                        if tile.posxp == wp.tile.posxp and tile.posyp == wp.tile.posyp:
                            reprint(wp, tile)
                    for bp in BlackPieces:
                        if tile.posxp == wp.tile.posxp and tile.posyp == wp.tile.posyp:
                            reprint(wp, tile)

                
                    
                # for tile in Tiles:
                #     for st in ShownTiles:
                #         if st.center == (tile.posxp, tile.posyp):
                #             for wp in WhitePieces:
                #                 if wp.tile == tile:
                #                     reprint(wp, tile)
                #             for bp in BlackPieces:
                #                 if bp.tile == tile:
                #                     reprint(bp, tile)

                
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()