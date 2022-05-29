import tkinter as tk
import random

#==========================================
# Purpose: Main Game/Loop
# Instance variables:
    #self.win=tkinter object
    #self.canvas= tkinter canvas object
    #self.board= the borderlines of the game
    #self.food= self-explanatory
    #self.snake= Human player snake
    #self.enemy_snake= Computer player snake
# Methods:
    #constructor(): create required attributes to instantiate a frame and the appropriate canvas and set up the loop for the first time
    #restartMethod(): required in order to recall it in case of gameover. Creates the player snake, the enemy snake and binds keys
    #printKeyInfo(): binds the wasd,up-down-left-right keys to direct the correspondent movement and the r key to restart the game
    #targetAuto(): defines the AI movement
    #gameLoop(): the main gameloop which is responsible for the updates. It, also, checks whether the game must stop (if the flag is true)
    #RestartGame(): It restarts the game, if it over
#==========================================

class SnakeGUI(tk.Tk):

    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Snake Game")
        self.canvas = tk.Canvas(self.win, width=660, height=660)
        self.canvas.pack()
        self.restartMethod()
        self.gameloop()

    def restartMethod(self):
        self.board = self.canvas.create_rectangle(30, 30, 630, 630)
        self.food=Food("red",self.canvas)
        self.snake=Snake(330,300,"green",self.canvas)
        self.enemy_snake=Snake(150,150,"purple",self.canvas)
        self.win.bind("<KeyPress>", self.printKeyInfo)

    def printKeyInfo(self, event):
        if event.keysym == "Up" or event.keysym == "w":
            self.snake.vx=0
            self.snake.vy=-30
        elif event.keysym == "Down" or event.keysym == "s":
            self.snake.vx=0
            self.snake.vy=+30
        elif event.keysym == "Left" or event.keysym == "a":
            self.snake.vx=-30
            self.snake.vy=0
        elif event.keysym == "Right" or event.keysym == "d":
            self.snake.vx=+30
            self.snake.vy=0
        elif event.keysym == "r":
            self.restartGame()

    def targetAuto(self, targetx, targety):
        if self.enemy_snake.x > targetx:
            self.enemy_snake.vx=-30
            self.enemy_snake.vy=0

        if self.enemy_snake.x < targetx:
            self.enemy_snake.vx=+30
            self.enemy_snake.vy=0

        if self.enemy_snake.x == targetx:
            if self.enemy_snake.y < targety:
                self.enemy_snake.vx = 0
                self.enemy_snake.vy = +30

            if self.enemy_snake.y > targety:
                self.enemy_snake.vx = 0
                self.enemy_snake.vy = -30

    def gameloop(self):
        if (self.snake.game_over_flag):
            self.canvas.create_text(350, 300, fill="blue", font="Times 25 italic bold", text="GameOver!")
            self.canvas.create_text(350, 350, fill="blue", font="Times 25 italic bold", text="Points:" + str(len(self.snake.segments)))
            self.canvas.create_text(350, 400, fill="blue", font="Times 25 italic bold", text="Press R to restart")
        else:
            self.targetAuto(self.food.x,self.food.y)
            self.food.checkFood(self.snake.move(self.food.x,self.food.y) or self.enemy_snake.move(self.food.x,self.food.y))
            self.snake.gameOver(self.enemy_snake.segments)

        self.canvas.after(100, self.gameloop)

    def restartGame(self):
        if (self.snake.game_over_flag):
            self.canvas.delete(tk.ALL)
            self.restartMethod()


#==========================================
# Purpose: The snake entity
# Instance variables:
    #self.x=x coordinate
    #self.y= y coordinate
    #self.color= the color of the snake
    #self.canvas= required canvas attribute in order to create rectangles to our canvas
    #self.segments= snake parts
    #self.vx=direction (pixel based) regarding the x axis
    #self.vy=direction (pixel based) regarding the y axis
    #self.game_over_flag= whether we should end the game or not according to the player snake status
# Methods:
    #constructor(): create required the aforementioned attributes and initialize the snake by creating the first rectangle and sets the default direction
    #move(): moving the snake, if the head is at the same position with the food, dont delete the last segment, otherise please do. Return the appropriate boolean
    #gameOver(): check if I exceed the borders, if I hitted my own body or the AI's
#==========================================
class Snake:

    def __init__(self,initX,initY,color,canvas):
        self.x=initX
        self.y=initY
        self.color=color
        self.canvas=canvas
        self.segments=[]
        initialRect=self.canvas.create_rectangle(self.x,self.y,self.x+30,self.y+30,fill=self.color)
        self.segments.append(initialRect)
        self.vx=30
        self.vy=0
        self.game_over_flag=False

    def move(self,foodx,foody):
        self.x+=self.vx
        self.y+=self.vy
        self.segments.insert(0,self.canvas.create_rectangle(self.x,self.y,self.x+30,self.y+30,fill=self.color))
        if (self.x==foodx and self.y==foody):
            return True
        else:
            last=self.segments.pop(-1)
            self.canvas.delete(last)
            return False

    def gameOver(self,enemy_segment):
        if (self.x>20*30 or self.x<1*30 or self.y>20*30 or self.y<1*30): self.game_over_flag=True
        for val in self.segments[1:]:
            if(self.canvas.coords(val)[0]==self.x and self.canvas.coords(val)[1]==self.y): self.game_over_flag=True
        for val in enemy_segment:
            if(self.canvas.coords(val)[0]==self.x and self.canvas.coords(val)[1]==self.y): self.game_over_flag=True


#==========================================
# Purpose: The food entity
# Instance variables:
    #self.x=x coordinate (random number following the appropriate positions)
    #self.y= y coordinate (random number following the appropriate positions)
    #self.color= the color of the food
    #self.canvas= required canvas attribute in order to create ovals to our canvas
    #self.segments= food parts (not necessary)
# Methods:
    #constructor(): create required the aforementioned attributes and initialize the food by creating the first oval
    #checkFood(): check whether a snake (enemy or player) ate the food so create another oval somewhere else while deleting the previous one
#==========================================
class Food:

    def __init__(self,color,canvas):
        self.x = random.randint(3, 18)*30
        self.y = random.randint(3, 18)*30
        self.color=color
        self.canvas=canvas
        self.segments = []
        initialRect = self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30,fill=self.color)
        self.segments.append(initialRect)

    def checkFood(self,wasEaten):
        if (wasEaten):
            self.x = random.randint(3, 18)*30
            self.y = random.randint(3, 18)*30
            self.segments.insert(0, self.canvas.create_oval(self.x, self.y , self.x + 30, self.y + 30,fill=self.color))
            last = self.segments.pop(-1)
            self.canvas.delete(last)


SnakeGUI()
tk.mainloop()