import pygame
import os
# import ctypes

#user32 = ctypes.windll.user32
#user32.SetProcessDPIAware()
#screen_size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
screen_size = (1280, 720)
pygame.init()
# ty
size = WIDTH, HEIGHT = screen_size
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


all_sprites = pygame.sprite.Group()
sprite_1 = AnimatedSprite(load_image("level1_btn.png"), 1, 3, size[0] // 2 - 100, size[1] / 10 * 3)
all_sprites.add(sprite_1)
sprite_2 = AnimatedSprite(load_image("level2_btn.png"), 1, 3, size[0] // 2 - 100, size[1] / 10 * 4)
all_sprites.add(sprite_2)
sprite_3 = AnimatedSprite(load_image("level3_btn.png"), 1, 3, size[0] // 2 - 100, size[1] / 10 * 5)
all_sprites.add(sprite_3)
sprite_4 = AnimatedSprite(load_image("level4_btn.png"), 1, 3, size[0] // 2 - 100, size[1] / 10 * 6)
all_sprites.add(sprite_4)
sprite_5 = AnimatedSprite(load_image("level5_btn.png"), 1, 3, size[0] // 2 - 100, size[1] / 10 * 7)
all_sprites.add(sprite_5)
f1, f2, f3 = 0, 0, 0
fon = pygame.transform.scale(load_image('buttons/background.png'), (size[0], size[1]))
screen.blit(fon, (0, 0))