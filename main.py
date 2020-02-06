from gamelevel import *


def level1():  # если уровень 1, то открываем его
    gl = GameLevel('data/levels/map.txt')
    gl.play()


def level2():
    gl = GameLevel('data/levels/map2.txt')
    gl.play()


def level3():
    gl = GameLevel('data/levels/map3.txt')
    gl.play()


def level4():
    gl = GameLevel('data/levels/map4.txt')
    gl.play()


def level5():
    gl = GameLevel('data/levels/map5.txt')
    gl.play()