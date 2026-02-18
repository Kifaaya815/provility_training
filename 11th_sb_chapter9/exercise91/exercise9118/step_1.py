from manim import *
import numpy as np

config.frame_height = 15
config.frame_width = 14
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BRIGHTPURPLE = "#BE03FD"

class Example9118a(Scene):
    def construct(self):

        axes = Axes(x_range=[-2, 11, 1],
                    y_range=[-2, 8, 1],
                    x_length=10,
                    y_length=10,
                    axis_config={
                        "color": BLACK,
                        "stroke_width": 3,
                        "include_ticks": False,
                        "include_numbers": False},
                    tips=True)
        axes.center()

        x_label = MathTex("x", font_size=45, color=BLACK).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y", font_size=45, color=BLACK).next_to(axes.y_axis.get_end(), UP)

        tick_len = 0.14

        x_ticks = VGroup(*[Line(axes.c2p(i, -tick_len),
                                axes.c2p(i, tick_len),
                                color=BLACK,
                                stroke_width=3)
                  for i in range(1, 5)])

        y_ticks = VGroup(*[Line(axes.c2p(-tick_len, i),
                                axes.c2p(tick_len, i),
                                color=BLACK,
                                stroke_width=3)
                for i in range(1, 7)])

        x_numbers = VGroup(*[MathTex(str(i), font_size=33, color=BLACK).next_to(axes.c2p(i, 0), DOWN)
                    for i in range(1, 5)])

        y_numbers = VGroup(*[MathTex(str(i), font_size=33, color=BLACK).next_to(axes.c2p(0, i), LEFT)
                    for i in range(1, 7)])

        zero = MathTex("0", font_size=33, color=BLACK).next_to(axes.c2p(0, 0), DL)

        line = Line(start=axes.c2p(-3, 5.5),
                    end=axes.c2p(11, -1.5),
                    color=BRIGHTPURPLE,
                    stroke_width=3)
        line.add_tip(tip_length=0.3, tip_width=0.3)
        line.add_tip(at_start=True, tip_length=0.3, tip_width=0.3)

        dot_04 = Dot(axes.c2p(0, 4), color=BLACK, radius=0.13)
        dot_23 = Dot(axes.c2p(2, 3), color=BLACK, radius=0.13)
        dot_26 = Dot(axes.c2p(2, 6), color=BLACK, radius=0.13)

        label_04 = MathTex("(0,4)", color=BLACK).next_to(dot_04, RIGHT).shift(UP*0.2)
        label_23 = MathTex("(2,3)", color=BLACK).next_to(dot_23, RIGHT).shift(UP*0.2)
        label_26 = MathTex("(2,6)", color=BLACK).next_to(dot_26, RIGHT)

        self.add(axes,
                 x_label, y_label,
                 x_ticks, y_ticks,
                 x_numbers, y_numbers, zero,
                 line,
                 dot_04, dot_23, dot_26,
                 label_04, label_23, label_26)
