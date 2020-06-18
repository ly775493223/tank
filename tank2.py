import pygame
COLOR = pygame.Color(0,0,0)

class MainGame():
    #游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    def __init__(self):
        pass
    #游戏开始方法
    def startGame(self):
        pygame.display.init()
        #创建窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #设置游戏标题
        pygame.display.set_caption("坦克大战v1.02")
        #让窗口持续刷新
        while True:
            #给窗口填充颜色
            MainGame.window.fill(COLOR)
            #窗口刷新
            pygame.display.update()
            
    #游戏结束方法
    def endGame(self):
        pass

class Tank():
    def __init__(self):
        pass
    #坦克移动方法
    def move(self):
        pass
    #坦克射击方法
    def shot(self):
        pass
    #坦克展示方法
    def displayTank(self):
        pass

class MyTank(Tank):
    def __init__(self):
        pass

class EnemyTank(Tank):
    def __init__(self):
        pass

class Bullet():
    def __init__(self):
        pass
    #子弹移动方法
    def move(self):
        pass
    #子弹展示方法
    def displayBullet(self):
        pass

class Explode():
    def __init__(self):
        pass
    #展示爆炸效果方法
    def displayExplode(self):
        pass

class Wall():
    def __init__(self):
        pass
    #展示墙壁方法
    def displayWall(self):
        pass

class music():
    def __init__(self):
        pass
    #播放音乐方法
    def play(self):
        pass

MainGame().startGame()
