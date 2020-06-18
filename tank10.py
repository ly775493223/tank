'''
v1.10
    新增功能：
        1、完善子弹类的封装
'''


import pygame
import time
import random
COLOR = pygame.Color(0,0,0)
RED = pygame.Color(255,0,0)
class MainGame():
    #游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    #创建我方坦克
    TANK_P1 = None
    #敌方坦克存储列表
    EnemyTank_list = []
    #敌方坦克数量
    EnemyTank_count = 5
    def __init__(self):
        pass
    #游戏开始方法
    def startGame(self):
        pygame.display.init()
        #创建窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #设置游戏标题
        pygame.display.set_caption("坦克大战v1.10")
        #创建我方坦克
        MainGame.TANK_P1 = Tank(400,300)
        #创建敌方坦克
        self.creatEnemyTank()
        
##        self.getTextSurface('aaa')
        
        #让窗口持续刷新
        while True:
            #给窗口填充颜色
            MainGame.window.fill(COLOR)
            #在事件中持续完成事件的获取
            self.getEvent()
            #将绘制得到的文字画布粘贴到窗口中
            MainGame.window.blit(self.getTextSurface('剩余敌方坦克%d辆'%len(MainGame.EnemyTank_list)),(5,5))
            #将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
            #循环展示敌方坦克
            self.biltEnemyTank()
            time.sleep(0.02)
            #根据坦克开关调用移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
            #窗口刷新
            pygame.display.update()
    #创建敌方坦克
    def creatEnemyTank(self):
        top = 100
        speed = random.randint(3,6)
        for i in range(MainGame.EnemyTank_count):
            left = random.randint(1,7)
            eTank = EnemyTank(left*100,top,speed)
            MainGame.EnemyTank_list.append(eTank)
    def biltEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            eTank.displayTank()
            eTank.randMove()
            
    #游戏结束方法
    def endGame(self):
        print('谢谢使用')
        exit()
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
                    #修改坦克方向
                    MainGame.TANK_P1.direction = 'L'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    #修改坦克方向
                    MainGame.TANK_P1.direction = 'R'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_UP:
                    #修改坦克方向
                    MainGame.TANK_P1.direction = 'U'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_DOWN:
                    #修改坦克方向
                    MainGame.TANK_P1.direction = 'D'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    MainGame.TANK_P1.stop = True

    def getTextSurface(self,text):
        #初始化字体模块
        pygame.font.init()
        
##        #列出所有字体
##        fontList = pygame.font.get_fonts()
##        print(fontList)
        
         
        #选中一个合适的字体
        font = pygame.font.SysFont("kaiti",18)
        #使用对应的字符完成相关内容的绘制
        textSurface = font.render(text,True,RED)
        return textSurface
class Tank():
    def __init__(self,left,top):
        self.images = {
            'U':pygame.image.load('img/p1tankU.gif'),
            'D':pygame.image.load('img/p1tankD.gif'),
            'L':pygame.image.load('img/p1tankL.gif'),
            'R':pygame.image.load('img/p1tankR.gif')
            }
        self.direction= 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        #指定坦克位置
        self.rect.left = left
        self.rect.top = top
        #新增速度属性
        self.speed = 5
        #坦克的移动开关
        self.stop = True
    #坦克移动方法
    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed
    #坦克射击方法
    def shot(self):
        pass
    #坦克展示方法
    def displayTank(self):
        #重新设置坦克图片
        self.image = self.images[self.direction]
        #将坦克添加到窗口中
        MainGame.window.blit(self.image,self.rect)

class MyTank(Tank):
    def __init__(self):
        pass

class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        self.images = {
            'U':pygame.image.load('img/enemy1U.gif'),
            'D':pygame.image.load('img/enemy1D.gif'),
            'L':pygame.image.load('img/enemy1L.gif'),
            'R':pygame.image.load('img/enemy1R.gif')
            }
        self.direction= self.randDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        #指定坦克位置
        self.rect.left = left
        self.rect.top = top
        #新增速度属性
        self.speed = 5
        #坦克的移动开关
        self.stop = True
        #新增步数属性，用来控制敌方坦克的随即移动
        self.step = 50
    def randDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'
    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 20
        else:
            self.move()
            self.step -= 1
        
class Bullet():
    def __init__(self,tank):
        #图片
        self.image = pygame.image.load('img/enemymissile.gif')
        #方向
        self.direction = tank.direction
        #位置
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank .rect.top - self.rect.top
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.weight
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.top/2
        elif self.direcion == 'R':
            self.rect.left = tank.rect.left + tank.rect.weight
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.top/2
        #速度
        self.speed = 7
    #子弹移动方法
    def move(self):
        pass
    #子弹展示方法
    def displayBullet(self):
        MainGame.window.bilt(self.image,self.rect)

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
