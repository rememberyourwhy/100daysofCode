from turtle import Turtle


STARTING_POSITIONS = [(-430, 30), (-430, 10), (-430, -10), (-430, -30)]
UP = 90
DOWN = 270

STARTING_POSITIONS_COMPUTER = [
    (430, 150), (430, 130), (430, 110), (430, 90),
    (430, 70), (430, 50), (430, 30), (430, 10),
    (430, -10), (430, -30), (430, -50), (430, -70),
    (430, -90), (430, -110), (430, -130), (430, -150)
]

class Paddle:
    def __init__(self):
        self.segments = []
        self.speed = "fastest"
        self.create_paddle()
        self.head = self.segments[0]

    def create_paddle(self):
        for turtle_index in range(5):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.pu()
            new_segment.setpos(STARTING_POSITIONS[turtle_index])
            self.segments.append(new_segment)

    def moveup(self, move_distance=0):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        if self.head:
            self.head.forward(move_distance)

    def movedown(self, move_distance=0):
        for seg_num in range(0, len(self.segments) - 1, 1):
            new_x = self.segments[seg_num + 1].xcor()
            new_y = self.segments[seg_num + 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        if self.head:
            self.head.forward(move_distance)

    def up(self):
        self.head = self.segments[0]
        self.head.setheading(UP)
        self.moveup(move_distance=20)
        self.head = None

    def down(self):
        self.head = self.segments[len(self.segments) - 1]
        self.head.setheading(DOWN)
        self.movedown(move_distance=20)
        self.head = None


class PaddleComputer(Paddle):
    def __init__(self):
        super().__init__()

    def create_paddle(self):
        for turtle_index in range(len(STARTING_POSITIONS_COMPUTER)):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.pu()
            new_segment.setpos(STARTING_POSITIONS_COMPUTER[turtle_index])
            self.segments.append(new_segment)

