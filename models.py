import arcade.key

from random import randint

class Ball:
    DIR_RIGHT = 1
    DIR_LEFT = 2
    SPEED = 0
    SPEED_ANGLE = 0
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
        self.direction = Ball.DIR_RIGHT

    def hit(self, slider):
        return ((abs(self.x - slider.x) < 20) and (abs(self.y - ((slider.y)-30)) <20))

    def switch_direction(self, direction):
        self.direction == direction
 
    def animate(self, delta):
        if self.direction == self.DIR_RIGHT:
            if self.x >= self.world.width-15:
                self.x = self.world.width-15
            self.x += self.SPEED
            self.angle += self.SPEED_ANGLE
        elif self.direction == self.DIR_LEFT:
            if self.x < 0:
                self.x = 0
            self.x += self.SPEED
            self.angle += self.SPEED_ANGLE
        

class Slider:
    SPEED = 7
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = 0

 
    def animate(self, delta):
        if(self.y >0):
            self.y -=self.SPEED
        else:
            self.y =-200

class Map:
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

 
    def animate(self, delta):
        if(self.y >-7060):
            self.y -=3
        else:
            self.y =-7060
            
class Map_mini:
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

 
    def animate(self, delta):
        self.x = self.x
        self.y = self.y

class Ball_mini:
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.count = 0
        self.angle = 0

 
    def animate(self, delta):
        self.count +=1
        if(self.count < 14500 and self.count % 13 == 0):
            self.y += 1
            
class End:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

 
    def animate(self, delta):
        self.x = self.x
        self.y = self.y
    
        

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.health = 5
        self.count = 0
        self.count2 = 0
        self.count_change = 0
        self.countR = 0
        self.amount = 42
        self.slider = []
        for i in range(1):
            self.slider.append(Slider(randint(20,380), 730, 75, 93))
        self.number = 1
        self.map = Map(self, 200 , 7814)
        self.end = End(self, 200 , 375)
        self.ball = Ball(self, 100, 15)
        self.map_mini = Map_mini(self,20,550)
        self.ball_mini = Ball_mini(self,20,361)
        self.bgm = arcade.sound.load_sound("sounds/bgm.mp3")
        self.bang = arcade.sound.load_sound("sounds/bang.mp3")
        arcade.sound.play_sound(self.bgm)
 
 
    def animate(self, delta):
        self.count +=1
        self.map.animate(delta)
        for m in self.slider:
            m.animate(delta)
        if self.map.y!=-7060 and self.health > 0:
            self.spawn()
        self.hit_ball()
        self.delete()        
        self.ball.animate(delta)
        self.ball_mini.animate(delta)

    def spawn(self):
        if self.count > self.amount:
            for i in range(self.number):
                self.slider.append(Slider(randint(0,400), 730, 75, 93))
                self.countR += 1
            self.count = 0
            self.count2 += 1
            self.count_change +=1
        if self.count2 > 4:
            for m in self.slider:
                m.SPEED += 3
            self.count2 = 0
        if self.count_change > 5:
            self.count_change = 0
            if self.amount > 7:
                self.amount -= 7

    def delete(self):
        for i in range(self.countR):
            if self.slider[i].y < 0:
                self.slider.pop(i)
                self.countR -= 1

    def hit_ball(self):
        for i in range(self.countR):
            if self.ball.hit(self.slider[i])== True:
                arcade.sound.play_sound(self.bang)
                self.slider.pop(i)
                self.countR -= 1
                self.health -=1                

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.ball.switch_direction(self.ball.DIR_LEFT)
            self.ball.SPEED = -8
            self.ball.SPEED_ANGLE = 5
        elif key == arcade.key.RIGHT:
            self.ball.switch_direction(self.ball.DIR_RIGHT)
            self.ball.SPEED = 8
            self.ball.SPEED_ANGLE = -5


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.SPEED = 0
            self.ball.SPEED_ANGLE = 0
