import arcade
from datetime import datetime, timedelta

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_background():
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




def draw_pine_tree(x, y):
    """
    This function draws a pine tree at the specified location.
    """
    # Draw the triangle on top of the trunk
    arcade.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100,
                                arcade.color.DARK_GREEN)

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)


def draw_bird(x= 150, y= 400):
    """
    Draw a bird using a couple arcs.
    """
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 20, 20, arcade.color.BLACK, 90, 180)



def draw_Character(x, y , scale):
    arcade.draw_text("draw_bitmap", 483, -20, arcade.color.BLACK, 12)
    texture = arcade.load_texture("/Users/jonathanmecham/Desktop/fiddlesworth.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)

def draw_Title():
    arcade.draw_text("draw_bitmap", 483, -20, arcade.color.BLACK, 12)
    texture = arcade.load_texture("/Users/jonathanmecham/Desktop/New Piskel.png")
    scale = 8.0
    arcade.draw_texture_rectangle(300, 400, scale * texture.width,
                                  scale * texture.height, texture, 0)








# Text---------------------------------------------------
def text1():
    start_x = 50
    start_y = 450
    arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
    arcade.draw_text("Simple line of text in 12 point", start_x, start_y, arcade.color.BLACK, 12)





def intro():

    draw_background()
    draw_pine_tree(112, 312)
    draw_pine_tree(300, 205)
    draw_pine_tree(400, 325)
    draw_bird()
    draw_Character(100, 150, 5.0)
    draw_Title()
    arcade.finish_render()
    arcade.run()




def actOne():
    draw_background()
    draw_pine_tree(112, 312)
    draw_pine_tree(300, 205)
    draw_pine_tree(400, 325)
    draw_bird()
    draw_Character(100, 100, 9.0)


def main():
    """
    This is the main program.
    """

    # Open the window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Fiddler's Quest")

    # Start the render process. This must be done before any drawing commands.
    arcade.start_render()


#draw intro background

    intro()
    arcade.finish_render()
    arcade.run()







    print("welcome to Fiddler's Quest!")






    arcade.finish_render()
    arcade.run()





if __name__ == "__main__":
    main()
