import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_ground():
    # Draw the ground
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snowman(x, y):
    # Snow
    arcade.draw_circle_filled(x, y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y+80, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y+140, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x-15, y+150, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x+15, y+150, 5, arcade.color.BLACK)

def on_draw(delta_time):
    arcade.get_window().clear()  # Sets the background color
    draw_ground()
    draw_snowman(on_draw.snow_person1_x, 200)  # Animate this snowman
    draw_snowman(450, 180)

    on_draw.snow_person1_x += 1  # Move the snowman

on_draw.snow_person1_x = 150  # Snowman's starting position

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 1/60th of a second
    arcade.schedule(on_draw, 1/60)
    arcade.run()

if __name__ == "__main__":
    main()
