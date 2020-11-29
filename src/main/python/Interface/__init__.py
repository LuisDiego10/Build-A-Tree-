import pygame
import Factory
import Socket

background = pygame.image.load("backgound.jpg")
pygame.init()
win = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Build-A-Tree")
font = pygame.font.SysFont(None, 80)

# //////Sockets/////// #
#   global Variables  #
socket = Socket.ClientSocket()
socket.start()
challenge = None
tokens = []


# Functions for socket#
def check_msg(msg):
    global socket, challenge, tokens
    if msg.__class__ == Factory.Challenge.__class__ and challenge != msg:
        challenge = msg
    if msg.__class__ == Factory.Token.__class__ and not (msg in tokens):
        tokens.append(msg)
    if msg.__class__ == "".__class__:
        pass
    print(challenge, tokens)


# ////////////////////#
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    while True:
        win.fill((0, 0, 0))
        draw_text("Build-A-Tree's Main Menu", font, (255, 255, 255), win, 250, 20)
        draw_text("START", font, (255, 255, 255), win, 500, 200)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        button_start = pygame.Rect(550, 270, 75, 75)
        if button_start.collidepoint((mx, my)):
            if click:
                game()
        pygame.draw.rect(win, (255, 0, 0), button_start)

        pygame.display.update()


def game():
    player1 = Players()
    player2 = Players()

    plataform1 = Plataform()
    plataform2 = Plataform()
    plataform3 = Plataform()
    plataform_princ = Plataform()

    running = True
    while running:
        pygame.time.delay(100)
        win.fill((0, 0, 0))
        win.blit(background, [-1000, 0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()

        # Player 1 Keys
        if keys[pygame.K_LEFT] and player1.x > 10:
            player1.x -= 15

        if keys[pygame.K_RIGHT] and player1.x < 850:
            player1.x += 15

        if not player1.Jump:
            if keys[pygame.K_UP] and player1.y > 100:
                player1.Jump = True

            if keys[pygame.K_DOWN] and player1.y < 500:
                player1.y += 5
        else:
            if player1.jumpCount >= -30:
                neg = 1
                if player1.jumpCount < 0:
                    neg = -1
                player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
                player1.jumpCount -= 1

            else:
                player1.Jump = False
                player1.jumpCount = 10

        # Player 2 Keys
        if keys[pygame.K_a] and player2.x > 10:
            player2.x -= 15

        if keys[pygame.K_d] and player2.x < 850:
            player2.x += 15

        if not player2.Jump:
            if keys[pygame.K_w] and player2.y > 100:
                player2.Jump = True

            if keys[pygame.K_s] and player2.y < 500:
                player2.y += 5
        else:
            if player2.jumpCount >= -30:
                neg = 1
                if player2.jumpCount < 0:
                    neg = -1
                player2.y -= (player2.jumpCount ** 2) * 0.5 * neg
                player2.jumpCount -= 1

            else:
                player2.Jump = False
                player2.jumpCount = 10

        player1.color = 255, 0, 0
        player2.color = 0, 0, 255

        player1.draw_player()
        player2.draw_player()

        plataform1.xp = 75
        plataform1.yp = 300
        plataform1.draw_plataform()

        plataform2.xp = 700
        plataform2.yp = 300
        plataform2.draw_plataform()

        plataform3.xp = 375
        plataform3.yp = 200
        plataform3.width = 200
        plataform3.draw_plataform()

        plataform_princ.xp = 210
        plataform_princ.yp = 450
        plataform_princ.width = 500
        plataform_princ.draw_plataform()

        pygame.display.update()


class Players(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 220
        self.y = 390
        self.Jump = False
        self.jumpCount = 10
        self.color = (0, 0, 0)
        self.width = 40
        self.height = 60

    def draw_player(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

class Plataform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.xp = 0
        self.yp = 0
        self.color = (255, 0, 0)
        self.width = 150
        self.height = 20

    def draw_plataform(self):
        pygame.draw.rect(win, self.color, (self.xp, self.yp, self.width, self.height))



main_menu()
