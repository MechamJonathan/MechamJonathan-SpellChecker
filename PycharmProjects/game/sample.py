import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        MyGame.draw_background(self)

    def draw_background(self):
        """
        This function draws the background. Specifically, the sky and ground.
        """
        # Draw the sky in the top two-thirds
        arcade.draw_lrtb_rectangle_filled(0,
                                          SCREEN_WIDTH,
                                          SCREEN_HEIGHT,
                                          SCREEN_HEIGHT * (1 / 3),
                                          arcade.color.SKY_BLUE)

        # Draw the ground in the bottom third
        arcade.draw_lrtb_rectangle_filled(0,
                                          SCREEN_WIDTH,
                                          SCREEN_HEIGHT / 3,
                                          0,
                                          arcade.color.FOREST_GREEN)
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()