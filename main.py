import pygame
pygame.init()

# creer une seconde class qui va reprensenter notre jeu
class Game:

    def __init__(self):

        self.player = Player()




# creer une classe qui va representer notre joueur
# modifier la classe comme etatnt un sprite dans notre jeu/element graphique qui peut se déplacer
class Player(pygame.sprite.Sprite):  # creer un objet qui va representer le player
    def __init__(self):
        # récuperer la super classe et faire apelle a son constructure
        super().__init__()  # et desormais notre player est un sprite sur le jeu
        # charger les aracteristiue par defaut de notre joueur
        self.health = 100  # vie du joeur/variable
        self.max_health = 100  # le nombre maximum
        self.attack = 10
        self.velocity = 5  # la vitesse de deplacemment par pixels
        self.image = pygame.image.load('assets/player.png')  # afficher l'image du joueur
        # pour faire deplacer l'image on devra recuperer ces cordonnées
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500


# Generer la fenetre de notre jeu
pygame.display.set_caption("savage")  # titre de la fentre et l'icone
screen = pygame.display.set_mode((1080, 720))  # la taille de la fenetre
background = pygame.image.load('assets/bg.jpg')

# charger notre jeu
game = Game()





running = True
# faire la boucle du jeu/tans que cette condition est vrai
while running:


    # applliquer larriére plan de notre jeu

    screen.blit(background, (0, -200))

    # appliquer l'image du joueur

    screen.blit(game.player.image, game.player.rect)

    # mettre ajour notre ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # que levenement de fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu ")
            print("")
