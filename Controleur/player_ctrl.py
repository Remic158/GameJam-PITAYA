import sys
sys.path.append('../GameJam-PITAYA/View')
sys.path.append('../GameJam-PITAYA/Model')

from Model.player import Player
import pygame
from Model.game import Game
from pygame.locals import *
# A faire : fuel qui diminue score, altitude qui augmente temps qui augmente obstacles qui bloque ou tue le joueur
# Objet supplementaire : haricot magique , aile , pitaya ...

# Creation d'un joueur au centre de la map
player1 = Player(1, int(1024/2)-40, int(768/2)-40, 100)
player_position = (player1.get_x(), player1.get_y())
player_position2 = (player1.get_x()-50, player1.get_y()-50)
quantitefuel = player1.get_fuel()
game1 = Game(0, 0) #score et time


# Test des evenements
pygame.init()
screen = pygame.display.set_mode((1024, 768), RESIZABLE)
# fond et collage du fond à la fenetre
fond = pygame.Surface(screen.get_size())
fond.fill((100,100,200))
# fond = pygame.image.load("../model/data/background.jpg").convert()
screen.blit(fond, (0, 0))
# Chargement et collage du personnage
# convert alpha pour la transparance du png
perso = pygame.image.load("../Model/data/perso.png").convert_alpha()
screen.blit(perso, player_position)
perso2 = pygame.image.load("../Model/data/perso.png").convert_alpha()
screen.blit(perso2, player_position2)


# Boucle affichage de la fenetre
## ici variables pour retenir en mémoire l’état des touches
droite = False
gauche = False
haut = False
bas = False
fall = True
timefuel = 0
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            ## on met a True l’état quand on appuye sur la touche
            if event.key == pygame.K_RIGHT:
                if player1.get_x() <= 1024:
                    droite = True
            elif event.key == pygame.K_LEFT:
                gauche = True
            elif event.key == pygame.K_UP:
                haut = True
            elif event.key == pygame.K_DOWN:
                bas = True
            elif event.key != pygame.K_DOWN:
                fall = True
        elif event.type == pygame.KEYUP:
            ## on met a False l’état quand la touche est relâchée
            if event.key == pygame.K_RIGHT:
                droite = False
            elif event.key == pygame.K_LEFT:
                gauche = False
            elif event.key == pygame.K_UP:
                haut = False
            elif event.key == pygame.K_DOWN:
                bas = False
    if player1.get_x() >= 940:
        droite=False
    elif player1.get_x()  <=10:
        gauche=False
    elif player1.get_y() >= 700:
        launched=False
    elif player1.get_y() <= 7:
        haut=False
    ## et on traite les évènements ici
    if droite:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(1, 0)
            player_position = player1.movePositCourante(0, 0.1)
    elif gauche:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(-1, 0)
            player_position = player1.movePositCourante(0, 0.1)
    elif haut:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(0, -1)
    elif bas:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(0, 1)
    elif fall:
        if player1.get_x() >= 0 or player1.get_x() <= 1024:
            player_position = player1.movePositCourante(0, 0.10)





    # Re-collage
    screen.blit(fond, (0, 0))
    screen.blit(perso, player_position)
    screen.blit(perso2, player_position2)
    # Fuel
    timefuel += 1
    if (timefuel % 150) == 0: #Retourne la duree depuis que pygame.init a été appeler en ms
        quantitefuel -= 1 #diminue de 1 le fuel à chaque boucle modulo 10 du timefuel
        player1.set_fuel(quantitefuel)
    if quantitefuel <= 0:
        launched = False
    rect = pygame.Rect(740, 690, quantitefuel*2, 25)
    pygame.draw.rect(screen, (255, 0, 0), rect)
    #Score
    game1.set_time(timefuel)
    if (game1.get_time() % 50) == 0:
        game1.add_score(1)
    text = pygame.font.Font('freesansbold.ttf', 25)
    score = text.render('Score : {}'.format(game1.get_score()), True, (0, 0, 255))
    screen.blit(score, (20, 20))
    # Rafraichissement
    pygame.display.flip()

    # à supprimer juste pour get la position du pointeur
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
        print(pygame.mouse.get_pos())  # getposition


