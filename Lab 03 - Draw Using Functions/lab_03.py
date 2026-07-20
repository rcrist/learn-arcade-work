"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_circular_tree(x, y):
    # Draw tree #1
    arcade.draw_lrbt_rectangle_filled(x, 599, y, 300, arcade.csscolor.GREEN)
    arcade.draw_rect_filled(arcade.XYWH(x+100, y+320, 20, 60), arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(x+100, y+350, 30, arcade.csscolor.DARK_GREEN)

def draw_elliptical_tree():
    # Draw elliptical tree
    arcade.draw_rect_filled(arcade.XYWH(200, 320, 20, 60), arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

def draw_arc_tree():
    # Draw arc tree
    arcade.draw_rect_filled(arcade.XYWH(300, 320, 20, 60), arcade.csscolor.SIENNA)
    arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

def draw_triangle_tree():
    # Another triangle tree
    arcade.draw_rect_filled(arcade.XYWH(400, 320, 20, 60), arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

def draw_polygon_tree():
    # Draw a tree using a polygon with a list of points
    arcade.draw_rect_filled(arcade.XYWH(500, 320, 20, 60), arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(((500, 400),
                                (480, 360),
                                (470, 320),
                                (530, 320),
                                (520, 360)
                                ),
                            arcade.csscolor.DARK_GREEN)
    
def draw_sun():
    # Draw a sun
    arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

    # Rays to the left, right, up, and down
    arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

    # Diagonal rays
    arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

def draw_message_text():
    # Draw text at (150, 230) with a font size of 24 pts.
    arcade.draw_text("Arbor Day - Plant a Tree!",
                    150, 230,
                    arcade.color.BLACK, 24)
    
def on_draw(delta_time):
    arcade.get_window().clear()  # Sets the background color

    draw_circular_tree(0, 0)
    draw_circular_tree(50, 0)
    draw_elliptical_tree()
    draw_arc_tree()
    draw_triangle_tree()
    draw_polygon_tree()
    draw_sun()
    draw_message_text()

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    # Call on_draw every 1/60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()

# Call the main function to get the program started.
main()