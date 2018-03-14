# Alien_Invasion
**From Python Crash Course.**  
**一个致敬Space Invaders的迷你游戏。**  

## 修改日志
>#### 2018年3月13日20点37分，对`game_functions.py`进行重构。
>1. 提取`check_play_button()`，新建为`start_game()`。
>2. 在`check_play_button()`和`check_keydown_events()`中调用`start_game()`。
>3. 新增：点击P键，即可开始游戏。（以往只能通过鼠标点击按钮以开始游戏。）