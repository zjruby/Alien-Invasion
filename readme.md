## python练手项目游戏《外星人入侵》
 ## 项目开始
 ```
windows安装pygame
前往以下地址，下载与你python版本匹配的安装包
》官方：https://bitbucket.org/pygame/pygame/downloads/
>备选：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
若为 .exe 文件：直接运行安装。
若为 .whl 文件：复制到项目目录，用 pip 安装：
>python -m pip install --user pygame-1.9.2a0-cp35-none-win32.wh1
 ```

验证：
```
>python
>>>import pygame
```
 **使用技术栈:**
 + python3
 + pygame

# 功能介绍
 ## alien_invansion
 主文件alien_invasion包含Alienlnvasion类，这个类创建在游戏的很多地方会用到的一系列属性：赋给这个settings的设置，赋给self.screen的主显示surface，以及一个飞船实例。这个模块还包含游戏的主循环，即一个调用_check_events()、ship.update()和_update_screen()的while循环，它还在每次通过循环后让时钟按键计时。
 \
 _check_events()方法检测相关的时间（如按下和释放），并通过调用_check_keydown_events()方法和_check_keyup_events()方法处理这些事件。当前，这些方法负责管理飞船的移动。
 \
 Alienlnvasion类还包含_update_screen()方法，这个方法在主循环中重绘屏幕。
 \
 要开始《外星人入侵》,只需运行文件alien_invasion.py，其它文件（setting.py和ship.py）包含的代码会被导入这个文件  
 
 ## settings
 文件setting包含Settings类，这个类只包含__init__()方法，用于初始化控制游戏外观和飞行速度的属性
 
 ## ship
 文件ship包含Ship类，这个类包含__init__()方法、管理飞船位置的update()方法和在屏幕上绘制飞船的blitme()方法。表示飞船的图像ship.bmp存储在文件夹images中

 ## Bullet
 1.创建子弹的属性rect。子弹并非基于图像文件的，因此必须使用pygame.Rect()类从头开始创建一个矩形。在创建这个类的实例时，必须提供矩形左上角x坐标和y坐标，还有矩形的宽度和高度。我们在（0,0）处创建这个矩形，而下一行代码将其移到了正确的位置，因为子弹的初始位置取决于飞船当前的位置。子弹的宽度和高度是重self.settings中获取的
 \
 2.将子弹的rect.midtop设置为飞船的rect.midto，这样子将出现在飞船顶部，看起来像是飞船发射出来的。我们将子弹的y坐标存储为浮点数，以便能够调子弹的速度
\
3.update()方法管理子弹的位置。发射之后，子弹向上移动，这意味着y坐标将不断减小。为了更新子弹的位置，从self.y中减去settings.bullet_speed的值。接下来，将self.rect.y设置为self.y的值
\
属性bullet_speed让我们能够随着游戏的进行或根据需要加快子弹的速度，以调整游戏的行为。子弹发射后，其x坐标始终不变，因此子弹将沿直线垂直上升
\
在需要绘制子弹时，我们调用draw_bullet()。draw.rect()使用存储在self.color中的颜色值,填充表示子弹的rect占据的那部分屏幕

 # 日志
 ## 2026-3-20
 添加游戏射击功能