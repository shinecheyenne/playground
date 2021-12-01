class Plate:
    def __init__(self, board, width, height, x_posn, y_posn, color, x=40, y=40):
        self.board = board
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color
        self.x_start = x_posn
        self.y_start = y_posn
        self.x = x
        self.y = y

        self.plate = self.board.draw_plate(self)

    def move_plate(self, event):
        if(self.x_posn <=0):
            self.x_posn = 40
        if(self.x_posn >=400):
            self.x_posn = 360

        if event.keysym == "Left":
            self.x_posn = self.x_posn - self.x
        if event.keysym == "Right":
            self.x_posn = self.x_posn + self.x

        self.board.move_item(self.plate, self.x_posn, self.y_posn, self.x_posn+self.width, self.y_posn+self.height)

    def detect_collision(self, ball):

        collision = False
        feel = 5

        self.coords = self.board.get_coords(self.plate)
        ball.coords = self.board.get_coords(ball.circle)

        r= (ball.coords[2]-ball.coords[0])/2

        if (ball.coords[3] > self.coords[1]) and (ball.coords[1] < self.coords[3]) and (
                ball.coords[2] > self.coords[0]) and (ball.coords[0] < self.coords[2]):
            collision = True
            print("collided")

        if (collision):
            if (ball.coords[1]<=self.coords[3]) and (ball.coords[3]>self.coords[3]) and (ball.coords[0]>self.coords[0]-r) and (ball.coords[2]<self.coords[2]+r):
                ball.y = abs(ball.y)#S
            elif (ball.coords[3]>=self.coords[1]) and (ball.coords[1]<self.coords[1]) and (ball.coords[0]>self.coords[0]-r) and (ball.coords[2]<self.coords[2]+r):
                ball.y = -abs(ball.y)#N

            adjustment = (-((self.coords[0] + self.coords[2])/2 - (ball.coords[0] + ball.coords[2])/2))/(self.width/2)
            ball.x = feel * adjustment
            return (collision)

    def to_default_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
        self.board.move_item(self.plate, self.x_posn, self.y_posn, self.x_posn+self.width, self.y_posn+self.height)
