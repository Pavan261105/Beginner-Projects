import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Art Generator")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

def get_colors(num_colors):
    return [colorsys.hsv_to_rgb(i / num_colors, 1, 1) for i in range(num_colors)]

def draw_spiral(colors):
    num_colors = len(colors)
    for i in range(360):
        pen.color(colors[i % num_colors])
        pen.forward(i * 2)
        pen.right(59)
        pen.forward(i // 3)

def rgb_to_hex(color):
    return f"#{int(color[0] * 255):02x}{int(color[1] * 255):02x}{int(color[2] * 255):02x}"

def main():
    colors = get_colors(360)
    colors = [rgb_to_hex(color) for color in colors]
    draw_spiral(colors)
    screen.mainloop()

main()