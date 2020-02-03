import pygame
import os
# import ctypes

pygame.init()
# user32 = ctypes.windll.user32
# user32.SetProcessDPIAware()
width = 1550  # user32.GetSystemMetrics(0)
height = 800  # user32.GetSystemMetrics(1)
size = width, height  # (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(size)  # , pygame.FULLSCREEN)


def load_image(name, colorkey=None):
    fullname = os.path.join('data/', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_start(self, name):
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image(name)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = self.width / 16 * 5
        sprite.rect.y = self.height / 8 * 2
        sprite.image = pygame.transform.scale(sprite.image, (int(self.width / 16 * 6), int(self.height / 8)))
        all_sprites.add(sprite)

    def draw_info(self, name):
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image(name)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = self.width / 16 * 5
        sprite.rect.y = self.height / 8 * 3
        sprite.image = pygame.transform.scale(sprite.image, (int(self.width / 16 * 6), int(self.height / 8)))
        all_sprites.add(sprite)

    def draw_rules(self, name):
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image(name)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = self.width / 16 * 5
        sprite.rect.y = self.height / 8 * 4
        sprite.image = pygame.transform.scale(sprite.image, (int(self.width / 16 * 6), int(self.height / 8)))
        all_sprites.add(sprite)

    def draw_settings(self, name):
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image(name)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = self.width / 16 * 5
        sprite.rect.y = self.height / 8 * 5
        sprite.image = pygame.transform.scale(sprite.image, (int(self.width / 16 * 6), int(self.height / 8)))
        all_sprites.add(sprite)

    def draw_exit(self, name):
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image(name)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = self.width / 16 * 5
        sprite.rect.y = self.height / 8 * 6
        sprite.image = pygame.transform.scale(sprite.image, (int(self.width / 16 * 6), int(self.height / 8)))
        all_sprites.add(sprite)


def proverka():
    if width / 16 * 5 <= cor[0] <= width / 16 * 11 and height / 8 * 2 <= cor[1] <= height / 8 * 3:
        pygame.draw.rect(screen, color,
                         (width / 16 * 5, height / 8 * 2, width / 16 * 6, height / 8), 1)
    if width / 16 * 5 <= cor[0] <= width / 16 * 11 and height / 8 * 3 <= cor[1] <= height / 8 * 4:
        pygame.draw.rect(screen, color,
                         (width / 16 * 5, height / 8 * 3, width / 16 * 6, height / 8), 1)
    if width / 16 * 5 <= cor[0] <= width / 16 * 11 and height / 8 * 4 <= cor[1] <= height / 8 * 5:
        pygame.draw.rect(screen, color,
                         (width / 16 * 5, height / 8 * 4, width / 16 * 6, height / 8), 1)
    if width / 16 * 5 <= cor[0] <= width / 16 * 11 and height / 8 * 5 <= cor[1] <= height / 8 * 6:
        pygame.draw.rect(screen, color,
                         (width / 16 * 5, height / 8 * 5, width / 16 * 6, height / 8), 1)
    if width / 16 * 5 <= cor[0] <= width / 16 * 11 and height / 8 * 6 <= cor[1] <= height / 8 * 7:
        pygame.draw.rect(screen, color,
                         (width / 16 * 5, height / 8 * 6, width / 16 * 6, height / 8), 1)

menu = Menu(width, height)
all_sprites = pygame.sprite.Group()
menu.draw_start("buttons/play.png")
menu.draw_settings("buttons/help.png")
menu.draw_rules("buttons/rules.png")
menu.draw_info("buttons/singin.png")
menu.draw_exit("buttons/exit.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        if event.type == pygame.MOUSEMOTION:
            cor = event.pos
            color = pygame.Color(0, 0, 255)
            proverka()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cor = event.pos
            color = pygame.Color(255, 0, 0)
            proverka()
        pygame.display.flip()
pygame.quit()