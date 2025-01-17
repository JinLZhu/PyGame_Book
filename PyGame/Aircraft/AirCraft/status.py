# 定义Status类，记录游戏状态


class Status:
    # Game status
    WELCOME, RUN, GAMEOVER, PAUSE = range(4)

    def __init__(self):
        # self.status = Status.RUN
        self.status = Status.WELCOME
        self.score = 0

    def reset(self):
        self.score = 0