import pygame
import os
import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
screen_size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
# screen_size = (1280, 720)
pygame.init()
size = WIDTH, HEIGHT = screen_size
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)


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


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_start(self, name):
        sprite = AnimatedSprite(load_image(name), 1, 3, self.width / 2, self.height / 10 * 3)
        all_sprites.add(sprite)

    def draw_info(self, name):
        sprite = AnimatedSprite(load_image(name), 1, 3, self.width / 2, self.height / 10 * 4)
        all_sprites.add(sprite)

    def draw_rules(self, name):
        sprite = AnimatedSprite(load_image(name), 1, 3, self.width / 2, self.height / 10 * 5)
        all_sprites.add(sprite)

    def draw_settings(self, name):
        sprite = AnimatedSprite(load_image(name), 1, 3, self.width / 2, self.height / 10 * 6)
        all_sprites.add(sprite)

    def draw_exit(self, name):
        sprite = AnimatedSprite(load_image(name), 1, 3, self.width / 2, self.height / 10 * 7)
        all_sprites.add(sprite)


def proverka():
    if size[0] / 2 - 100 <= cor[0] <= size[0] / 2 + 100 and size[1] / 10 * 3 - 25 <= cor[1] <= size[1] / 10 * 3 + 25:
        # sprite = AnimatedSprite(load_image("buttons/play_btn.png"), 1, 3, size[0] / 2, size[1] / 10 * 3)
        for i in all_sprites:
            if i == AnimatedSprite(load_image("buttons/play_btn.png"), 1, 3, size[0] / 2, size[1] / 10 * 3):
                i.update()
        # all_sprites.add(sprite)
    if size[0] / 2 - 100 <= cor[0] <= size[0] / 2 + 100 and size[1] / 10 * 4 - 25 <= cor[1] <= size[1] / 10 * 4 + 25:
        AnimatedSprite(load_image("buttons/about_developers_btn.png"), 1, 3, size[0] / 2, size[1] / 10 * 4).update()
    if size[0] / 2 - 100 <= cor[0] <= size[0] / 2 + 100 and size[1] / 10 * 5 - 25 <= cor[1] <= size[1] / 10 * 5 + 25:
        AnimatedSprite(load_image("buttons/rules.png"), 1, 3, size[0] / 2, size[1] / 10 * 5).update()
    if size[0] / 2 - 100 <= cor[0] <= size[0] / 2 + 100 and size[1] / 10 * 6 - 25 <= cor[1] <= size[1] / 10 * 6 + 25:
        AnimatedSprite(load_image("buttons/singin.png"), 1, 3, size[0] / 2, size[1] / 10 * 6).update()
    if size[0] / 2 - 100 <= cor[0] <= size[0] / 2 + 100 and size[1] / 10 * 7 - 25 <= cor[1] <= size[1] / 10 * 7 + 25:
        AnimatedSprite(load_image("buttons/exit_btn.png"), 1, 3, size[0] / 2, size[1] / 10 * 7).update()


menu = Menu(size[0], size[1])
all_sprites = pygame.sprite.Group()
menu.draw_start("buttons/play_btn.png")
menu.draw_info("buttons/about_developers_btn.png")
menu.draw_rules("buttons/rules.png")
menu.draw_settings("buttons/singin.png")
menu.draw_exit("buttons/exit_btn.png")
fon = pygame.transform.scale(load_image('buttons/background.png'), (size[0], size[1]))
screen.blit(fon, (0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.draw(screen)
        if event.type == pygame.MOUSEMOTION:
            cor = event.pos
            proverka()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cor = event.pos
            proverka()
        pygame.display.flip()
pygame.quit()