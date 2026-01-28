from manim import *

config.frame_height=8
config.frame_width=10
config.pixel_height=2800
config.pixel_width=2800

config.background_color=WHITE

class SixShapes(Scene):
    def construct(self):
        circle= Circle(radius=1, color=PINK, fill_color=LIGHT_PINK, fill_opacity=0.5)
        square= Square(side_length=2, color=BLUE_D, fill_color=BLUE, fill_opacity=0.5)
        ellipse= Ellipse(width=3, height=2, color=GREEN_D, fill_color=GREEN, fill_opacity=0.5)
        rectangle= Rectangle(height=2, width=3, color=RED_D, fill_color=RED, fill_opacity=0.5).next_to(circle, DOWN)
        triangle= Triangle(color=YELLOW_D,fill_color=YELLOW, fill_opacity=0.5).scale(1.4)
        polygon= Polygon([0, 0, 0],[1.2, 0.6, 0],[1.2, 2, 0],[0, 1.4, 0], color=ORANGE,fill_color=ORANGE, fill_opacity=0.5).scale(1.2)

        square.to_corner(UR)
        ellipse.to_corner(UL)
        circle.next_to(ellipse, buff=1)
        rectangle.to_corner(DL)
        triangle.next_to(rectangle, buff=0.9)
        polygon.next_to(triangle, buff=1)
        polygon.shift(UP*0.15)

        circle_label=Text("Circle", color=BLACK).next_to(circle, DOWN)
        ellipse_label=Text("Ellipse", color=BLACK).next_to(ellipse, DOWN)
        square_label=Text("Square", color=BLACK).next_to(square, DOWN)
        ellipse_label=Text("Ellipse", color=BLACK).next_to(ellipse, DOWN)
        rectangle_label=Text("Rectangle", color=BLACK).next_to(rectangle, DOWN)
        triangle_label=Text("Triangle", color=BLACK).next_to(triangle, DOWN)
        polygon_label=Text("Polygon", color=BLACK).next_to(polygon, DOWN)


        self.add(circle, square, ellipse, rectangle, triangle, polygon, circle_label, 
                 ellipse_label, square_label, rectangle_label, triangle_label, polygon_label)

