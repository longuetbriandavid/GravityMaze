import pygame
import sys
from pygame.locals import *
from game import*

class Menu():
    def __init__(self):
        #Constantes
        self.width = 800
        self.height = 512
        self.screen = ""
        self.icons_01 = ""
        self.fps = 30
        self.color = (255,255,255)
        self.police01 = ""
        self.police02 = ""
        self.texte01 = ""
        self.texte02 = ""
        self.texte03 = ""
        self.texte_rect01 = ""
        self.texte_rect02 = ""
        self.texte_rect03 = ""
        self.clock = ""

    def pygame_init(self):
        # Initialisation des modules + le temps
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()

    def caption(self):
        # Création du titre de la fenètre
        pygame.display.set_caption("The Labyrinth")

    def icons(self):
        self.icons_01 = pygame.image.load("images/icon_01.png")
        pygame.display.set_icon(self.icons_01)

    def display(self):
        # Création de la fenètre
        self.screen = pygame.display.set_mode((self.width, self.height),HWSURFACE | DOUBLEBUF)
    
    def music(self):
        # Chargement de la musique + lecture en boucle
        pygame.mixer.music.load("music/sound_01.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0)
        

    def police(self):
        # Chargement des polices
        self.police01 = pygame.font.Font("polices/Humblle Rought Caps.otf", 80)
        self.police02 = pygame.font.Font("polices/Margarita.otf", 50)

    def texte(self):
        # Définition des textes
        self.texte01 = self.police01.render("The Labyrinth",True, self.color)
        self.texte02 = self.police02.render("Appuyez sur ESPACE pour", True, self.color)
        self.texte03 = self.police02.render("commencer la partie", True, self.color)

    def texte_rect(self):
        # Création du rectangle des textes
        self.texte_rect01 = self.texte01.get_rect()
        self.texte_rect02 = self.texte02.get_rect()
        self.texte_rect03 = self.texte03.get_rect()

    def texte_position(self):
        # Définition de leurs positions sur l'écran
        self.texte_rect01.centerx = self.width/2
        self.texte_rect01.centery = 100
        self.texte_rect02.centerx = self.width/2
        self.texte_rect02.centery = 300
        self.texte_rect03.centerx = self.width/2
        self.texte_rect03.centery = 350

    def texte_blit(self):
        # Collage des textes sur l'écran
        self.screen.blit(self.texte01, self.texte_rect01)
        self.screen.blit(self.texte02, self.texte_rect02)
        self.screen.blit(self.texte03, self.texte_rect03)
        
def start():
    # Initialisation des fonctions des différentes class
    menu = Menu()
    menu.pygame_init()
    menu.caption()
    menu.icons()
    menu.display()
    menu.music()
    menu.police()
    menu.texte()
    menu.texte_rect()
    menu.texte_position()

    #Draw / render + delay

    background01 = pygame.image.load("images/fond_01.png")
    menu.screen.blit(pygame.transform.scale(background01, (menu.width, menu.height)), (0, 0))
    pygame.display.flip()
    pygame.time.delay(3000)

    # Chargement du fond + collage + utilsation de la class Menu
    background02 = pygame.image.load("images/fond_02.jpg")
    menu.screen.blit(pygame.transform.scale(background02, (menu.width, menu.height)), (0, 0))
   
    

    #Variable pour le scrolling du background
    x=0
    test = True
    while test:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif pygame.key.get_pressed()[K_ESCAPE]:
                sys.exit()
            elif pygame.key.get_pressed()[K_SPACE]:
                play()

            #Adapter le 1er fond à la taille de l'écran
            elif event.type == VIDEORESIZE:
                menu.screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF)
                menu.screen.blit(pygame.transform.scale(background01, event.dict['size']), (0, 0))
            #Le 2eme fond
            elif event.type == VIDEORESIZE:
                menu.screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF)
                menu.screen.blit(pygame.transform.scale(background02, event.dict['size']), (0, 0))
            #Puis le 3ème
            elif event.type == VIDEORESIZE:
                menu.screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF)
                menu.screen.blit(pygame.transform.scale(background03, event.dict['size']), (0, 0))
                
        #Scrolling Background
        rel_x = x % background02.get_rect().width
        menu.screen.blit(background02,(rel_x - background02.get_rect().width,0))
        if rel_x < menu.width:
            menu.screen.blit(background02,(rel_x,0))
        x -=1
        
        # Chargement du fond + collage + utilsation de la class Menu + affichage du texte
        background03 = pygame.image.load("images/fond_03.png")
        menu.screen.blit(pygame.transform.scale(background03, (490, 100)), (160, 65))
        menu.texte_blit()

        menu.clock.tick(menu.fps)
        pygame.display.flip()