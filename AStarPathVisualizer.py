import pygame as pg
from tkinter import *
from settings import *
vec = pg.math.Vector2
 
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("A Star Pathfinding")
clock = pg.time.Clock()
 
class Astar():
    # create the node
    def __init__(self, parent=None, position=None):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.playing = True
        self.state = 'menu'  # menu asks user where to start and end, astar will show the visualization of it
        self.cell_width = MAZE_WIDTH // COLS
        self.cell_height = MAZE_HEIGHT // ROWS
 
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        self.walls = []
        self.walkable = []
        self.start = 0
        self.goal = 0
 
    def __eq__(self, other):
        return self.position == other.position
 
    def run(self):
        while self.playing:
            if self.state == 'menu':
                self.draw_gui()
                self.menu_events()
                self.menu_update()
                self.menu_draw()
            elif self.state == 'astar':
                self.astar_events()
                self.astar_update()
                self.astar_draw()
 
    def algorithm(self, maze, start, goal):
        pass
 
    def load(self):
        # appends maze wall and walkable locations to their lists
        with open('maze.txt', 'r') as file:
            for yindex, line in enumerate(file):
                for xindex, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xindex, yindex))
                    elif char == "0":
                        self.walkable.append(vec(xindex, yindex))
 
    def menu_events(self):
        # ask user for input on start and end location
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
 
    def menu_update(self):
        # check to see if user has made an input and if it was valid
        pass
 
    def menu_draw(self):
        # use tkinter to make a gui
        self.screen.fill(BLACK)
        pg.display.update()
 
    def draw_gui(self):
        # create window object
        window = Tk()
 
        # define our lables: start "(0, 0)" and end "(5, 8)"
        l1 = Label(window, text="Start x: ")
        l1.grid(row=0, column=0)
 
        l2 = Label(window, text="Start y: ")
        l2.grid(row=1, column=0)
 
        l3 = Label(window, text="Goal x: ")
        l3.grid(row=2, column=0)
 
        l4 = Label(window, text="Goal y: ")
        l4.grid(row=3, column=0)
 
        # create entries
        global var
        var = IntVar()
        e1 = Entry(window, textvariable=var) # start x text
        e1.grid(row=0, column=1)
 
        global var2
        var2 = IntVar()
        e2 = Entry(window, textvariable=var2) # start y text
        e2.grid(row=1, column=1)
 
        global var3
        var3 = IntVar()
        e3 = Entry(window, textvariable=var3) # goal x text
        e3.grid(row=2, column=1)
 
        global var4
        var4 = IntVar()
        e4 = Entry(window, textvariable=var4) # goal y text
        e4.grid(row=3, column=1)
 
        def onClick(args):
            if args == 1:
                self.state = 'astar'
                # close gui element
                print(var.get())
                print(var2.get())
                print(var3.get())
                print(var4.get())
 
        # define buttons
        b1 = Button(window, text="Run", width=12, command=lambda: onClick(1))
        b1.grid(row=2, column=3)
        b2 = Button(window, text="Quit", width=12, command=exit)
        b2.grid(row=3, column=3)
 
        window.mainloop()
 
    def astar_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                if event.key == pg.K_r:
                    self.reset()
 
    def astar_update(self):
        # when algothrim is done, display finished screen
        pass
 
    def astar_draw(self):
        # draw a grid, make bg white
        self.screen.fill(WHITE)
        self.load()
        self.draw_walls()
        self.draw_walkables()
        self.draw_start(var.get(), var2.get())
        self.draw_goal(var3.get(), var4.get())
        self.draw_grid()
        pg.display.update()
 
    def draw_start(self, x, y):
        self.rect = pg.Rect(x, y, 32, 32)
        self.startRect = pg.draw.rect(self.screen, GREEN, self.rect)
 
    def draw_goal(self, x, y):
        self.rect2 = pg.Rect(x, y, 32, 32)
        pg.draw.rect(self.screen, BLUE, self.rect2)
 
    def draw_walls(self):
        for wall in self.walls:
            pg.draw.rect(self.screen, RED, (wall.x*self.cell_width, wall.y*self.cell_height, W, H))
 
    def draw_walkables(self):
        for walkable in self.walkable:
            pg.draw.rect(self.screen, WHITE, (walkable.x*self.cell_width, walkable.y*self.cell_height, W, H))
 
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
 
    def reset(self):
        self.state = 'menu'
 
 
a = Astar()
a.run()