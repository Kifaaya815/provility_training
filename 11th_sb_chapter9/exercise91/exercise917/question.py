from manim import *

config.frame_height = 10
config.frame_width = 14
config.pixel_height = 3200
config.pixel_width = 3200
config.background_color = WHITE

AXISGREEN= "#1B7F3F"
LINEBLUE= "#2E2F75"

class Exercise917(Scene):
    def construct(self):

        axes = Axes(x_range=[-2.5, 5.5, 1],
                    y_range=[-1.5, 6, 1],
                    x_length=11.5,
                    y_length=8.5,
                    axis_config={"color": AXISGREEN,
                                 "stroke_width": 8},
                    tips=True)

        axes.x_axis.ticks.set_stroke(width=4)
        axes.y_axis.ticks.set_stroke(width=4)

        axes.shift(DOWN*0.2)

        axes.add_coordinates(font_size=28, color=BLACK)

        origin_label = MathTex("0", font_size=30, color=BLACK)
        origin_label.next_to(axes.coords_to_point(0, 0),
                             DOWN + LEFT,
                             buff=0.25)

        graph = axes.plot(lambda x: -x + 4,
                          x_range=[-2.2, 5.2],
                          color= LINEBLUE,
                          stroke_width=7)

        point = Dot(axes.coords_to_point(3, 1),
                    radius=0.1,
                    color="#111827")

        x_label = MathTex("x", font_size=50, color=BLACK)
        x_label.next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)

        y_label = MathTex("y", font_size=50, color=BLACK)
        y_label.next_to(axes.y_axis.get_end(), UP, buff=0.15)

        self.add(axes, graph, point, x_label, y_label, origin_label)
