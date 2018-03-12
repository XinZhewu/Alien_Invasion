# coding=utf-8
# @Time   : 2018/2/6 14:46
# @Author : XinZhewu_568580410@qq.com

"""此文件跟踪游戏的统计信息
"""


class GameStats:

    def __init__(self, ai_settings):
        """初始化统计信息.
        只创建GameStats实例,当玩家开始新游戏,重置一些统计,
        在方法reset_stats中初始化大部分统计;
        如此创建实例时可妥善设置统计,同时玩家开始新游戏亦可调用reset_stats().
        """

        self.ai_settings = ai_settings

        self.reset_stats()

        # 游戏刚启动时处于非活跃状态
        self.game_active = False

        # 任何情况下都不重置的游戏历史最高分
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
