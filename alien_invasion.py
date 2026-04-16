import sys
from time import sleep

import pygame

from game_stats import GameStats
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        # 编组外星人
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        """外星人撞到飞船时，将余下的飞船数量减1"""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        self.ship = Ship(self)
        # 游戏启动后处于活动状态
        self.game_active = True

    def _ship_hit(self):
        """响应飞船和外星人的碰撞"""
        if self.stats.ships_left > 0:
            # 将ships_left减一，默认gamestat.ships_left=3
            self.stats.ships_left -= 1
            # 清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()
            # 创建一个新的外星舰队，并将飞船放在屏幕底部的中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(0.5)
        else:
            self.game_active = False

    def _create_fleet(self):
        """创建一个外星舰队"""
        # 创建一个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 3 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # 添加一行外星人后，重置x值并递增y值
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """创建一个外星人并将其放在当前行中"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()  # 检查按键鼠标窗口
            if self.game_active:  # 游戏处于活跃状态执行
                self.ship.update()  # 更新飞船位置（左右）
                self._update_bullets()  # 更新游戏子弹位置
                self._update_aliens()  # 删除已经消失的子弹
            self._update_screen()  # 不管游戏是否暂停都要刷新画面
            self.clock.tick(60)  # 游戏固定60fps

    def _update_aliens(self):
        """更新外星舰队中所有外星人的位置"""
        """检查外星人位于屏幕边缘，并更新整个外星舰队的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查是否有外星人到到达了屏幕的下边缘
        self._check_aliens_bottom()

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
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        # 删除已消失子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # 检查是否有子弹击中了外星人
        # 如果是，就删除相应的子弹和外星人
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """响应子弹和外星人的碰撞"""
        # 删除发生碰撞的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # 外星人舰队击落后在显示另一个外星舰队
        # 检查aliens是否为空
        if not self.aliens:
            # 删除现有的子弹并创建一个新的外星舰队
            self.bullets.empty()
            self._create_fleet()

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets"""
        # 玩家按下空格检查bullets的长度，如果小于len(self.bullets)小于3
        # 就创建新子弹，则什么不做
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_fleet_edges(self):
        """在外星人到达边缘时采取相应的措施"""
        # 外星人到达边缘时，暂停
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个外星人舰队向下移动，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕的下边缘"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # 像飞船被撞到一样进行处理
                self._ship_hit()
                break


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
