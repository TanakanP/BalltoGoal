import arcade

from models import World, Ball, Map, Slider, Map_mini, Ball_mini, End

 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 750

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class BallGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)

        self.map_sprite = ModelSprite('images/map.jpg', model=self.world.map)
        self.slider_texture = arcade.load_texture('images/slider.png')
        self.ball_sprite = ModelSprite('images/ball.png',model=self.world.ball)
        self.map_mini_sprite = ModelSprite('images/map_mini.jpg',model=self.world.map_mini)
        self.ball_mini_sprite = ModelSprite('images/ball_mini.png',model=self.world.ball_mini)
        self.end_sprite = ModelSprite('images/end.jpg',model=self.world.end)

    def draw_slider(self, slider):
        for m in slider:
            arcade.draw_texture_rectangle(m.x,m.y,75,93,self.slider_texture)
            
 
    def on_draw(self):
        arcade.start_render()
        if self.world.health > 0:
            self.map_sprite.draw()
            self.ball_sprite.draw()
            self.draw_slider(self.world.slider)
            self.map_mini_sprite.draw()
            self.ball_mini_sprite.draw()

            arcade.draw_text(str("Health: " + str(self.world.health)),self.width-115,self.height-30,
                             arcade.color.RED,20)
        else:
            self.end_sprite.draw()

    def animate(self, delta): 
        self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)
 
 
if __name__ == '__main__':
    window = BallGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

