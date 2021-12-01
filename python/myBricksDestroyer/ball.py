import random, board

class Ball:
    def __init__(self, board, width, height, color, x_posn, y_posn, x=10, y=5):
        self.board = board
        self.width = width
        self.height = height
        self.color = color
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.x_start = x_posn
        self.y_start = y_posn
        self.x = x
        self.y = y

        self.circle = self.board.draw_oval(self)

    def move_ball(self):
        self.x_posn = self.x_posn + self.x
        self.y_posn = self.y_posn + self.y
        if self.x_posn <= 0 or self.x_posn+self.width >= 500:
            self.x = -self.x
        if self.y_posn <= 0 or self.y_posn+self.height >= 500:
            self.y = -self.y

        self.board.move_item(self.circle, self.x_posn, self.y_posn, self.x_posn+self.width, self.y_posn+self.height)

    def default_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    def start_ball(self, x, y):
        self.x = -x if random.randint(0, 1) else x
        self.y = -y
        self.default_position()

    def stop_ball(self):
        self.x = 0
        self.y = 0
