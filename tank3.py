'''
v1.03
    新增功能
    事件处理：
        点击关闭按钮，退出程序事件
        方向控制，子弹发射
'''


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
        pygame.display.set_caption("坦克大战v1.03")
        #让窗口持续刷新
        while True:
            #给窗口填充颜色
            MainGame.window.fill(COLOR)
            #在事件中持续完成事件的获取
            self.getEvent()
            #窗口刷新
            pygame.display.update()
            
    #游戏结束方法
    def endGame(self):
        print('谢谢使用')
    #获取程序期间所有事件（鼠标事件，键盘事件）
    def getEvent(self):
        #获取所有事件
        eventList = pygame.event.get()
        #对事件进行判断处理（1、点击关闭按钮  2、按下键盘上的某个按钮）
        for event in eventList:
            #判断event.type是否QUIT，如果是退出的话，直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endGame()
            #判断事件类型是否为按键按下，如果是，继续判断是哪一个按键，来进行对应处理
            if event.type == pygame.KEYDOWN:
                #具体是哪一个按键的处理
                if event.key == pygame.K_LEFT:
                    print('坦克左调头，移动')
                elif event.key == pygame.K_RIGHT:
                    print('坦克右调头，移动')
                elif event.key == pygame.K_UP:
                    print('坦克上调头，移动')
                elif event.key == pygame.K_DOWN:
                    print('坦克下调头，移动')
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')       

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
