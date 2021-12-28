import pygame as pg
import setings as st


class Snake():

    body = []
    start_len = None

    def __init__(self, x, y, len):
        self.body.append(pg.Rect(x, y, st.SNAKE_SIZE, st.SNAKE_SIZE))
        self.start_len = len
        for i in range(len):
            self.eat()


    def eat(self):
        r = self.body[len(self.body)-1]
        self.body.append(pg.Rect(r.x + st.SNAKE_SIZE, r.y, st.SNAKE_SIZE, st.SNAKE_SIZE))


    def step(self, dir):
        head_x = self.body[0].x
        head_y = self.body[0].y
        if dir.lower() == "left":
            self.body[0].x -= st.SNAKE_SIZE
        elif dir.lower() == "right":
            self.body[0].x += st.SNAKE_SIZE
        elif dir.lower() == "down":
            self.body[0].y += st.SNAKE_SIZE
        elif dir.lower() == "up":
            self.body[0].y -= st.SNAKE_SIZE
        for i in range(len(self.body)):
            j = len(self.body) - i - 1
            if j == 1:
                self.body[1].x = head_x
                self.body[1].y = head_y
                break
            self.body[j].x = self.body[j-1].x
            self.body[j].y = self.body[j-1].y