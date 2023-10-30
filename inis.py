    
import pygame
from ChessBoard import Tiles
from Visuals import AllPeices
from Visuals import screen
from inis import HorsebImage, RookbImage, BishopbImage, QueenbImage, KingbImage, PawnbImage, PawnwImage, HorsewImage, RookwImage, BishopwImage, QueenwImage, KingwImage


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
            StretchQueenb = pygame.transform.scale(QueenbImage,(45,45))
            screen.blit(StretchQueenb, Queenb1)
            AllPeices.append(Queenb1)
            Tiles[55+i].SetVispos(Queenb1)
        if i == 5:
            Kingb1 = pygame.Rect(300, 100, 50, 50)
            StretchKingb = pygame.transform.scale(KingbImage,(45,45))
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
            Rookb2 =  pygame.Rect(100 + 7*50, 100, 50, 50)
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
