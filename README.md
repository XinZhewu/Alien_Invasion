# Alien_Invasion
**From Python Crash Course.**  
**一个致敬Space Invaders的迷你游戏。**  

## 修改日志
>#### 2018年3月13日20点37分，对`game_functions.py`进行重构。
>1. 提取`check_play_button()`，新建为`start_game()`。
>2. 在`check_play_button()`和`check_keydown_events()`中调用`start_game()`。
>3. 新增：点击P键，即可开始游戏。（以往只能通过鼠标点击按钮以开始游戏。）

>#### 2018年3月14日23点41分，新增把历史最高分保存到本地的功能。
>1. 添加`highest.txt`以保存历史最高分。
>2. 修改`game_stats.py`和`scoreboard.py`的代码以进行适配。
>3. 在`game_functions.py`添加一系列函数进行适配：`contrast_high_score()`/`save_high_score(stats)`。