# PySnake
Snake Game with Tkinter

#==========================================
# Purpose: Main Game/Loop
## Instance variables:
    #self.win=tkinter object
    #self.canvas= tkinter canvas object
    #self.board= the borderlines of the game
    #self.food= self-explanatory
    #self.snake= Human player snake
    #self.enemy_snake= Computer player snake
## Methods:
    #constructor(): create required attributes to instantiate a frame and the appropriate canvas and set up the loop for the first time
    #restartMethod(): required in order to recall it in case of gameover. Creates the player snake, the enemy snake and binds keys
    #printKeyInfo(): binds the wasd,up-down-left-right keys to direct the correspondent movement and the r key to restart the game
    #targetAuto(): defines the AI movement
    #gameLoop(): the main gameloop which is responsible for the updates. It, also, checks whether the game must stop (if the flag is true)
    #RestartGame(): It restarts the game, if it over
#==========================================

#==========================================
# Purpose: The snake entity
## Instance variables:
    #self.x=x coordinate
    #self.y= y coordinate
    #self.color= the color of the snake
    #self.canvas= required canvas attribute in order to create rectangles to our canvas
    #self.segments= snake parts
    #self.vx=direction (pixel based) regarding the x axis
    #self.vy=direction (pixel based) regarding the y axis
    #self.game_over_flag= whether we should end the game or not according to the player snake status
## Methods:
    #constructor(): create required the aforementioned attributes and initialize the snake by creating the first rectangle and sets the default direction
    #move(): moving the snake, if the head is at the same position with the food, dont delete the last segment, otherise please do. Return the appropriate boolean
    #gameOver(): check if I exceed the borders, if I hitted my own body or the AI's
#==========================================
