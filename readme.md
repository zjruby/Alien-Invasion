## python练手项目游戏《外星人入侵》
 ## 项目开始
 ```
windows安装pygame
前往以下地址，下载与你python版本匹配的安装包
官方：https://bitbucket.org/pygame/pygame/downloads/
备选：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
若为 .exe 文件：直接运行安装。
若为 .whl 文件：复制到项目目录，用 pip 安装：
python -m pip install --user pygame-1.9.2a0-cp35-none-win32.wh1
 ```

验证：
```
>python
>>>import pygame
```
 -- alien_invansion
 主文件alien_invasion包含Alienlnvasion类，这个类创建在游戏的很多地方会用到的一系列属性：赋给这个settings的设置，赋给self.screen的主显示surface，以及一个飞船实例。这个模块还包含游戏的主循环，即一个调用_check_events()、ship.update()和_update_screen()的while循环，它还在每次通过循环后让时钟按键计时。
 _check_events()方法检测相关的时间（如按下和释放），并通过调用_check_keydown_events()方法和_check_keyup_events()方法处理这些事件。当前，这些方法负责管理飞船的移动。Alienlnvasion类还包含_update_screen()方法，这个方法在主循环中重绘屏幕。
 要开始《外星人入侵》,只需运行文件alien_invasion.py，其它文件（setting.py和ship.py）包含的代码会被导入这个文件  