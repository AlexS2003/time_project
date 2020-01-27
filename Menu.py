import pygame
# import ctypes

pygame.init()
# user32 = ctypes.windll.user32
# user32.SetProcessDPIAware()
width = 1550  # user32.GetSystemMetrics(0)
height = 800  # user32.GetSystemMetrics(1)
size = width, height  # (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(size)  # , pygame.FULLSCREEN)


class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_start(self):
        font = pygame.font.Font(None, 50)
        screen.blit(font.render("Играть", 1, (100, 255, 100)), (self.width / 16 * 5, self.height / 8 * 2))
        color = pygame.Color(255, 255, 255)
        pygame.draw.rect(screen, color, (self.width / 16 * 5, self.height / 8 * 2, self.width / 16 * 6, self.height / 8), 1)

    def draw_info(self):
        font = pygame.font.Font(None, 50)
        screen.blit(font.render("О разраб", 1, (100, 255, 100)), (self.width / 16 * 5, self.height / 8 * 3))
        color = pygame.Color(255, 255, 255)
        pygame.draw.rect(screen, color, (self.width / 16 * 5, self.height / 8 * 3, self.width / 16 * 6, self.height / 8), 1)

    def draw_rules(self):
        font = pygame.font.Font(None, 50)
        screen.blit(font.render("Правила", 1, (100, 255, 100)), (self.width / 16 * 5, self.height / 8 * 4))
        color = pygame.Color(255, 255, 255)
        pygame.draw.rect(screen, color, (self.width / 16 * 5, self.height / 8 * 4, self.width / 16 * 6, self.height / 8), 1)

    def draw_settings(self):
        font = pygame.font.Font(None, 50)
        screen.blit(font.render("*", 1, (100, 255, 100)), (self.width / 16 * 5, self.height / 8 * 5))
        color = pygame.Color(255, 255, 255)
        pygame.draw.rect(screen, color, (self.width / 16 * 5, self.height / 8 * 5, self.width / 16 * 6, self.height / 8), 1)

    def draw_exit(self):
        font = pygame.font.Font(None, 50)
        screen.blit(font.render('Выход', 1, (100, 255, 100)), (self.width / 16 * 5, self.height / 8 * 6))
        color = pygame.Color(255, 255, 255)
        pygame.draw.rect(screen, color, (self.width / 16 * 5, self.height / 8 * 6, self.width / 16 * 6, self.height / 8), 1)


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
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0, 0, 0))
        menu.draw_start()
        menu.draw_settings()
        menu.draw_rules()
        menu.draw_info()
        menu.draw_exit()
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