from manim import *
import numpy as np

config.frame_height = 15
config.frame_width = 14
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BURGUNDY = "#610023"
BURNTORANGE = "#C04E01"

class Example91(Scene):
    def construct(self):

        axes = Axes(x_range=[-0.5, 6, 1],
                    y_range=[-0.5, 4, 1],
                    x_length=8,
                    y_length=6,
                    axis_config={"color": BURGUNDY,
                                 "stroke_width": 6,
                                 "include_ticks": False,
                                 "include_numbers": False})

        axes.shift(LEFT*0.5 + DOWN*0.5).set_z_index(10)

        origin_label = MathTex("0", font_size=40, color=BLACK)
        origin_label.next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.15)

        x_label = MathTex("x", font_size=45, color=BLACK)
        y_label = MathTex("y", font_size=45, color=BLACK)

        x_label.next_to(axes.x_axis.get_end())
        y_label.next_to(axes.y_axis.get_end(), UP)

        sqrt_curve = ParametricFunction(lambda t: axes.c2p(t, np.sqrt(t)),
                                        t_range=[0, 5.6],
                                        color=BURNTORANGE,
                                        stroke_width=6)


        func_label = MathTex("f(x)=\\sqrt{x}", color=BLACK)
        func_label.scale(0.9)
        func_label.next_to(sqrt_curve, UP, buff=0.3).shift(RIGHT*2.5)

        self.add(axes)
        self.add(sqrt_curve)
        self.add(origin_label)
        self.add(x_label, y_label)
        self.add(func_label)
