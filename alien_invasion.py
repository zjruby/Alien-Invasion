import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """管理游资源和行为类"""

    def __init__(self):
        pygame.display.set_caption("Alien Invasion")
        # 设置背景颜色
        self.bg_color = (230, 230, 230)
        """初始化游戏并创建资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # 设置全屏
        self.screen = pygame.display.set_mode(
            (1200, 800),
        )  # pygame.FULLSCREEN
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # 编组
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()  # 更新游戏子弹位置
            self._update_bullets() # 删除已经消失的子弹
            self._update_screen()
            self.clock.tick(60)

    # 检查玩家是否单击了关闭窗口按钮的代码移到这个方法中
    def _check_events(self):
        """响应按键和鼠标"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # 响应按下
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 按q结束，全屏状态下不能按q结束
        elif event.key == pygame.K_q:
            sys.exit()
            # esc切换窗口飞机无法重新绘制在屏幕上
        elif event.key == pygame.K_ESCAPE:
            self.screen = pygame.display.set_mode((1200, 800))
            self.settings.screen_width = 1200
            self.settings.screen_height = 800
            self.ship.screen_rect = self.screen.get_rect()
            self.ship.rect.midbottom = self.ship.screen_rect.midbottom
            self.ship.x = float(self.ship.rect.x)
            # 按空格开火
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # 响应释放
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()

    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        # 删除已消失子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets"""
        # 玩家按下空格检查bullets的长度，如果小于len(self.bullets)小于3
        # 就创建新子弹，则什么不做
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
