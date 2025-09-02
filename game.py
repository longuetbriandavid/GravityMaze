import pygame, random, sys
from pygame.locals import *
from functions import *

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		self.game = Game()
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/ball.png')
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(5, 5)
		self.x = 0
		self.y = 1
		self.v = 1

	def update(self):
		dx = self.rect.centerx + self.x * self.v
		dy = self.rect.centery + self.y * self.v
		self.rect.center = (dx, dy)
		
		if not (self.rect.centery < self.game.width and self.game.height - self.image.get_height() ):
			self.v = 0
			
		elif (self.rect.centery < self.game.width and self.game.height -  self.image.get_height() ):
			self.v = 1
		
	def rotationg(self):
		self.rect.center=(self.rect.center[1],self.game.width and self.game.height - self.rect.center[0])
		
	def rotationd(self):
		self.rect.center=(self.game.width and self.game.height - self.rect.center[1],self.rect.center[0])

class Game():
	def __init__(self):
		#constantes
		self.width = 302
		self.height = 302
		self.screen = ""
		self.icons_01 = ""
		self.delay = 15

	def pygame_init(self):
		pygame.init()
		pygame.display.init()
		pygame.mixer.init()

	def display(self):
		self.screen = pygame.display.set_mode((self.width,self.height))

	def caption(self):
		pygame.display.set_caption("Maze")

	def icons(self):
		self.icons_01 = pygame.image.load("images/icon_01.png")
		pygame.display.set_icon(self.icons_01)

	def musicMenu(self):
		# Arreter la musique du menu
		pygame.mixer.music.stop()

	def drawMaze(self):
		mazeGen()
		
	def musicDrawMaze(self):
		#musique pendant la génération du terrain
		pygame.mixer.music.load("music/sound_02.mp3")
		pygame.mixer.music.play(loops=-1, start=0.0)

	def musicBackground(self):
		#Musique du terrain
		pygame.mixer.music.load("music/sound_03.mp3")
		pygame.mixer.music.play(loops=-1, start=0.0)

	def delaY(self):
		pygame.time.delay(self.delay)

class Menu_fin():
    def __init__(self):
        #Constantes
        self.width = 800
        self.height = 512
        self.screen = ""
        self.icons_01 = ""
        self.fps = 30
        self.color = (255,255,255)
        self.color_orange = (255,165,0)
        self.color_red = (255,0,0)
        self.police01 = ""
        self.police02 = ""
        self.police03 = ""
        self.police04 = ""
        self.texte01 = ""
        self.texte02 = ""
        self.texte03 = ""
        self.texte04 = ""
        self.texte05 = ""
        self.texte_rect01 = ""
        self.texte_rect02 = ""
        self.texte_rect03 = ""
        self.texte_rect04 = ""
        self.texte_rect05 = ""
        self.clock = ""

    def pygame_init(self):
        # Initialisation des modules + le temps
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()

    def caption(self):
        # Création du titre de la fenètre
        pygame.display.set_caption("Menu Fin")

    def icons(self):
        self.icons_01 = pygame.image.load("images/icon_01.png")
        pygame.display.set_icon(self.icons_01)

    def display(self):
        # Création de la fenètre
        self.screen = pygame.display.set_mode((self.width, self.height),HWSURFACE | DOUBLEBUF)

    def music(self):
        # Chargement de la musique + lecture en boucle
        pygame.mixer.music.load("music/sound_04.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0)
        

    def police(self):
        # Chargement des polices
        self.police01 = pygame.font.Font('polices/Humblle Rought Caps.otf', 80)
        self.police02 = pygame.font.Font('polices/Margarita.otf', 30)
        self.police03 = pygame.font.SysFont('Arial', 50)
        self.police04 = pygame.font.SysFont('Arial', 12)

    def texte(self):
        # Définition des textes
        self.texte01 = self.police01.render("The Labyrinth",True, self.color_orange)
        self.texte02 = self.police02.render("Appuyez sur ESPACE pour relancer une partie", True, self.color_red)
        self.texte03 = self.police02.render("Appuyez sur ECHAP pour quitter le jeu", True, self.color_red)
        self.texte04 = self.police03.render("Merci d'avoir joué à notre jeu",  True, self.color)
        self.texte05 = self.police04.render("Copyright © 2019-XXXX. Tous droits réservés.",  True, self.color)

    def texte_rect(self):
        # Création du rectangle des textes
        self.texte_rect01 = self.texte01.get_rect()
        self.texte_rect02 = self.texte02.get_rect()
        self.texte_rect03 = self.texte03.get_rect()
        self.texte_rect04 = self.texte04.get_rect()
        self.texte_rect05 = self.texte05.get_rect()

    def texte_position(self):
        # Définition de leurs positions sur l'écran
        self.texte_rect01.centerx = self.width/2
        self.texte_rect01.centery = 70
        self.texte_rect02.centerx = self.width/2
        self.texte_rect02.centery = 220
        self.texte_rect03.centerx = self.width/2
        self.texte_rect03.centery = 320
        self.texte_rect04.centerx = self.width/2
        self.texte_rect04.centery = 420
        self.texte_rect05.centerx = self.width/2
        self.texte_rect05.centery = 505

    def texte_blit(self):
        # Collage des textes sur l'écran
        self.screen.blit(self.texte01, self.texte_rect01)
        self.screen.blit(self.texte02, self.texte_rect02)
        self.screen.blit(self.texte03, self.texte_rect03)
        self.screen.blit(self.texte04, self.texte_rect04)
        self.screen.blit(self.texte05, self.texte_rect05)

def play():
	#Constantes
	game = Game()
	game.pygame_init()
	game.musicMenu()
	game.musicDrawMaze()
	game.drawMaze()
	game.pygame_init()
	game.display()
	game.caption()
	game.icons()
	
	background = pygame.image.load('MAZE.png')
    
	game.musicBackground()
	
	ball = Ball()
	
	all_sprites = pygame.sprite.Group()
	all_sprites.add(ball)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if pygame.key.get_pressed()[K_LEFT]:
				background=pygame.transform.rotate(background, 90)
				Ball.rotationg(ball)

			if pygame.key.get_pressed()[K_RIGHT]:
				background=pygame.transform.rotate(background, -90)
				Ball.rotationd(ball)
				
		if background.get_at((ball.rect.centerx,ball.rect.centery + 6)) == (0,0,0,255):
			ball.v = 0
		
		elif background.get_at((ball.rect.centerx,ball.rect.centery)) == (0, 255, 0):
			start_menu_fin()

		all_sprites.update()
		
		game.screen.blit(background, [0, 0])
		all_sprites.draw(game.screen)
		pygame.display.flip()
		
		game.delaY()

def start_menu_fin():
    # Initialisation des fonctions des différentes class
    menu_fin = Menu_fin()
    menu_fin.pygame_init()
    menu_fin.caption()
    menu_fin.icons()
    menu_fin.display()
    menu_fin.music()
    menu_fin.police()
    menu_fin.texte()
    menu_fin.texte_rect()
    menu_fin.texte_position()

    # Chargement du fond + collage + utilsation de la class Menu
    background02 = pygame.image.load("images/fond_04.png")
    menu_fin.screen.blit(pygame.transform.scale(background02, (menu_fin.width, menu_fin.height)), (0, 0))
   
    #Variable pour le scrolling du background
    x=0
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif pygame.key.get_pressed()[K_ESCAPE]:
                sys.exit()
            elif pygame.key.get_pressed()[K_SPACE]:
                play()

            #Adapter le fond à la taille de l'écran
            elif event.type == VIDEORESIZE:
                menu_fin.screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF)
                menu_fin.screen.blit(pygame.transform.scale(background02, event.dict['size']), (0, 0))

        #Scrolling Background
        rel_x = x % background02.get_rect().width
        menu_fin.screen.blit(background02,(rel_x - background02.get_rect().width,0))
        if rel_x < menu_fin.width:
            menu_fin.screen.blit(background02,(rel_x,0))
        x -=1     
            
        menu_fin.texte_blit()

        menu_fin.clock.tick(menu_fin.fps)
        pygame.display.flip()
