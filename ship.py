import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #加载飞船图像并获取外接矩形
        self.image=pygame.image.load('img/ship.bmp')
        self.rect=self.image.get_rect()

        #每艘新飞船都放在屏幕底部的中央
        self.rect.midbottom=self.screen_rect.midbottom
        #在飞船的属性X中存储一个浮点数
        self.x=float(self.rect.x)
        #移动标志（飞船一开始不移动）
        """玩家按下右键按键变为true并且玩家释放时将moving_right设置False"""
        self.moving_right=False
        self.moving_left=False
        
    def update(self):
        """根据移动标志调整飞船的位置"""
        #更新飞船的活动范围
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        #根据self.x更新rect对象
        self.rect.x=self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)