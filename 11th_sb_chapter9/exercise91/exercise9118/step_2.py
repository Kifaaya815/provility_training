from manim import *
import numpy as np

config.frame_height = 15
config.frame_width = 14
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BRIGHTPURPLE = "#BE03FD"

class Example9118b(Scene):
    def construct(self):

        axes = Axes(x_range=[-5, 5, 1],
                    y_range=[-1.5, 4, 1],
                    x_length=10,
                    y_length=10,
                    axis_config={"color": BLACK,
                                 "stroke_width": 3,
                                 "include_ticks": False,
                                 "include_numbers": False},
                    tips=True)
        axes.center()

        x_label = MathTex("x", font_size=45, color=BLACK).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y", font_size=45, color=BLACK).next_to(axes.y_axis.get_end(), UP)

        tick_len = 0.07

        x_ticks = VGroup(*[Line(axes.c2p(i, -tick_len), axes.c2p(i, tick_len), color=BLACK, stroke_width=3)
                  for i in [-4, -3, -2, -1, 1, 2, 3, 4]])

        y_ticks = VGroup(*[Line(axes.c2p(-tick_len, i), axes.c2p(tick_len, i), color=BLACK, stroke_width=3)
                  for i in [1, 2, 3]])

        x_numbers = VGroup(*[MathTex(str(i), font_size=28, color=BLACK).next_to(axes.c2p(i, 0), DOWN)
                    for i in [-4, -3, -2, -1, 1, 2, 3, 4]])

        y_numbers = VGroup(*[MathTex(str(i), font_size=28, color=BLACK).next_to(axes.c2p(0, i), LEFT)
                    for i in [1, 2, 3]])

        zero = MathTex("0", font_size=33, color=BLACK).next_to(axes.c2p(0, 0), DL*0.6).shift(DOWN*0.06)

        y0_line = Line(start=axes.c2p(-5, 0),
                       end=axes.c2p(2, 0),
                       color=BRIGHTPURPLE,
                       stroke_width=3)

        dot_neg2 = Dot(axes.c2p(-2, 0), color=BLACK, radius=0.13)
        dot_20 = Dot(axes.c2p(2, 0), color=BLACK, radius=0.13)

        label_neg2 = MathTex("(-2,0)", color=BLACK).next_to(dot_neg2, UP)
        label_20 = MathTex("(2,0)", color=BLACK).next_to(dot_20, DOWN*2.5)

        y0_text = MathTex("y=0", color=BLACK).next_to(y0_line, DOWN*3)

        y1_line = Line(start=axes.c2p(2, 1),
                       end=axes.c2p(5, 1),
                       color=BRIGHTPURPLE,
                       stroke_width=3)
        y1_line.add_tip(tip_length=0.3, tip_width=0.3)

        dot_21 = Dot(axes.c2p(2, 1), color=BLACK, radius=0.13)
        y1_text = MathTex("y=1", color=BLACK).next_to(y1_line, DOWN)

        self.add(axes,
                 x_label, y_label,
                 x_ticks, y_ticks,
                 x_numbers, y_numbers, zero,
                 y0_line, y1_line,
                 dot_neg2, dot_20, dot_21,
                 label_neg2, label_20,
                 y0_text, y1_text)
