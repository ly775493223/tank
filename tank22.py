'''
v1.20
    新增功能：
        1、实现坦克之间的碰撞检测

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
    #存储我方子弹的列表
    Bullet_list = []
    #存储敌方子弹的列表
    Enemy_Bullet_list = []
    #爆炸效果列表
    Explode_list = []
    #墙壁列表
    Wall_list = []
    def __init__(self):
        pass
    #游戏开始方法
    def startGame(self):
        pygame.display.init()
        #创建窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #设置游戏标题
        pygame.display.set_caption("坦克大战v1.20")
        #创建我方坦克
        self.creatMyTank()
        #创建敌方坦克
        self.creatEnemyTank()
        #创建墙壁
        self.creatWalls()

##        self.getTextSurface('aaa')

        #让窗口持续刷新
        while True:
            #给窗口填充颜色
            MainGame.window.fill(COLOR)
            #在事件中持续完成事件的获取
            self.getEvent()
            #将绘制得到的文字画布粘贴到窗口中
            MainGame.window.blit(self.getTextSurface('剩余敌方坦克%d辆'%len(MainGame.EnemyTank_list)),(5,5))
            #展示墙壁
            self.biltWalls()
            #将我方坦克加入到窗口中
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                MainGame.TANK_P1.displayTank()
            else:
                del MainGame.TANK_P1
                MainGame.TANK_P1 = None
            #循环展示敌方坦克
            self.blitEnemyTank()
            #调用渲染子弹列表的方法
            self.blitBullet()
            #调用渲染敌方子弹列表的方法
            self.blitEnemyBullet()
            #根据坦克开关调用移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
                #调用坦克碰撞墙壁方法
                MainGame.TANK_P1.hitwalls()
                #调用我方坦克碰撞敌方坦克的方法
                MainGame.TANK_P1.hitEnemyTank()
            #调用展示爆炸效果的方法
            self.displayExplodes()
            time.sleep(0.02)
            #窗口刷新
            pygame.display.update()
    #创建我方坦克
    def creatMyTank(self):
        MainGame.TANK_P1 = MyTank(400,300)
    #创建敌方坦克
    def creatEnemyTank(self):
        top = 100
        for i in range(MainGame.EnemyTank_count):
            #随机生成一个左值
            speed = random.randint(3,6)
            left = random.randint(1,7)
            eTank = EnemyTank(left*100,top,speed)
            MainGame.EnemyTank_list.append(eTank)
    #创建墙壁
    def creatWalls(self):
        for i in range(1,7):
            wall = Wall(135*i,200)
            MainGame.Wall_list.append(wall)
    #将墙壁加入窗口
    def biltWalls(self):
        for wall in MainGame.Wall_list:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.Wall_list.remove(wall)
    #将敌方坦克加入到窗口中
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if eTank.live:
                eTank.displayTank()
                eTank.randMove()
                #调用敌方坦克与墙壁的碰撞方法
                eTank.hitwalls()
                #调用敌方坦克和我方坦克碰撞方法
                eTank.hitMyTank()
                #调用敌方坦克射击方法
                ebullet = eTank.shot()
                if ebullet:
                    MainGame.Enemy_Bullet_list.append(ebullet)
            else:
                MainGame.EnemyTank_list.remove(eTank)
    #将我方子弹加入到窗口中
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            if bullet.live:
                bullet.displayBullet()
                bullet.bulletMove()
                #调用子弹与坦克碰撞方法
                bullet.hitEnemyTank()
                #调用我方子弹是否碰撞墙壁方法
                bullet.hitWall()
            else:
                MainGame.Bullet_list.remove(bullet)
    #将敌方子弹加入到窗口中
    def blitEnemyBullet(self):
        for eBullet in MainGame.Enemy_Bullet_list:
            #如果子弹还活着，绘制出来，否则，移除列表中该子弹
            if eBullet.live:
                eBullet.displayBullet()
                eBullet.bulletMove()
                eBullet.hitWall()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    eBullet.hitMyTank()
            else:
                MainGame.Enemy_Bullet_list.remove(eBullet)
    #展示爆炸效果
    def displayExplodes(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.Explode_list.remove(explode)
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
                if event.key == pygame.K_ESCAPE and not MainGame.TANK_P1:
                    self.creatMyTank()
                #具体是哪一个按键的处理
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
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
                        if len(MainGame.Bullet_list) < 3:
                            #产生一颗子弹
                            m = Bullet(MainGame.TANK_P1)
                            #将子弹加入到子弹列表
                            MainGame.Bullet_list.append(m)
            #结束游戏方法
            if event.type == pygame.KEYUP:
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
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

class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Tank(BaseItem):
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
        #新增属性 live  记录坦克是否活着
        self.live = True
        #新增属性，用来记录坦克移动之前的坐标（用于坐标还原）
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
    #坦克移动方法
    def move(self):
        #先记录移动之前的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
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
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop
    def hitwalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                self.stay()
    def shot(self):
        return Bullet(self)
    #坦克展示方法
    def displayTank(self):
        #重新设置坦克图片
        self.image = self.images[self.direction]
        #将坦克添加到窗口中
        MainGame.window.blit(self.image,self.rect)

class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)
    #新增主动碰撞敌方坦克方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank,self):
                self.stay()
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        super(EnemyTank,self).__init__(left,top)
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
    def shot(self):
        num = random.randint(1,100)
        if num <= 3:
            return Bullet(self)
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self,MainGame.TANK_P1):
            self.stay()

class Bullet(BaseItem):
    def __init__(self,tank):
        #图片
        self.image = pygame.image.load('img/enemymissile.gif')
        #方向
        self.direction = tank.direction
        #位置
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank .rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.height/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.height/2
        #速度
        self.speed = 10
        #记录子弹是否存在
        self.live = True
    #子弹移动方法
    def bulletMove(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
                self.rect.left += self.speed
            else:
                self.live = False
    #子弹展示方法
    def displayBullet(self):
        MainGame.window.blit(self.image,self.rect)
    #新增我方子弹与敌方坦克碰撞方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank,self):
                #产生一个爆炸效果
                explode = Explode(eTank)
                #将爆炸效果加入到爆炸效果列表
                MainGame.Explode_list.append(explode)
                self.live = False
                eTank.live = False
    #新增敌方子弹与我方坦克的碰撞方法
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self,MainGame.TANK_P1):
            #产生爆炸效果，并加入爆炸效果列表中
            explode = Explode(MainGame.TANK_P1)
            MainGame.Explode_list.append(explode)
            # #修改子弹状态
            self.live = False
            #修改我方坦克状态
            MainGame.TANK_P1.live = False
    #新增子弹与墙壁碰撞的方法
    def hitWall(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                #修改子弹状态
                self.live = False
                wall.hp -= 1
                if wall.hp == 0:
                    wall.live = False
class Explode():
    def __init__(self,tank):
        self.rect = tank.rect
        self.step = 0
        self.live = True
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif')
        ]
        self.image = self.images[self.step]
    #展示爆炸效果方法
    def displayExplode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0
class Wall():
    def __init__(self,left,top):
        self.image = pygame.image.load('img/steels.gif')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        #用来判断墙壁是否应该在窗口中展示
        self.live = True
        self.hp = 3
    #展示墙壁方法
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)

class music():
    def __init__(self):
        pass
    #播放音乐方法
    def play(self):
        pass

MainGame().startGame()
