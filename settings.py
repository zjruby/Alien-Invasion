class Settings:
    """存储游戏《外星人入侵》中所有设置类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        #飞船速度设置
        self.ship_speed=20
        #子弹设置
        self.bullet_speed=2.0#设置发射速度
        self.bullet_width=3#宽度为3
        self.bullet_height=15#高度为15
        self.bullet_color=(60,60,60)#颜色为灰色