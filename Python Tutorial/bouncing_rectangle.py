import arcade

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Size of the rectangle
RECT_WIDTH = 50
RECT_HEIGHT = 50

def on_draw(delta_time):
    """
    Use this function to draw everything to the screen.
    """

    arcade.get_window().clear()

    arcade.draw_lbwh_rectangle_filled(on_draw.center_x, on_draw.center_y,
                                 RECT_WIDTH, RECT_HEIGHT,
                                 arcade.color.ALIZARIN_CRIMSON)

    # Modify rectangle's position
    on_draw.center_x += on_draw.delta_x * delta_time
    on_draw.center_y += on_draw.delta_y * delta_time

    # Figure out if we hit the edge and need to reverse.
    if on_draw.center_x < RECT_WIDTH // 2 \
            or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:
        on_draw.delta_x *= -1
    if on_draw.center_y < RECT_HEIGHT // 2 \
            or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:
        on_draw.delta_y *= -1

on_draw.center_x = 100      # Initial x position
on_draw.center_y = 50       # Initial y position
on_draw.delta_x = 115  # Initial change in x
on_draw.delta_y = 130  # Initial change in y

def main():
    # Open up our window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Bouncing Rectangle Example")
    arcade.set_background_color(arcade.color.WHITE)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1 / 80)

    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()