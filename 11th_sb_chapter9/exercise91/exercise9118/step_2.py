from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 15
config.pixel_height = 2500
config.pixel_width = 2500
config.background_color = WHITE

BRIGHTPURPLE = "#BE03FD"

class Example9118b(Scene):
    def construct(self):

        axes = Axes(x_range=[-7, 5, 1],
                    y_range=[-4, 4, 1],
                    x_length=10,
                    y_length=10,
                    axis_config={"color": BLACK,
                                 "stroke_width": 5,
                                 "include_ticks": False,
                                 "include_numbers": False,
                                 "tip_length": 0.35,
                                 "tip_width": 0.25},
                    tips=True)
        axes.center()

        axes.y_axis.add_tip(at_start=True, tip_length=0.44, tip_width=0.29)
        axes.x_axis.add_tip(at_start=True, tip_length=0.44, tip_width=0.29)

        x_label = MathTex("x", font_size=45, color=BLACK).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y", font_size=45, color=BLACK).next_to(axes.y_axis.get_end(), UP)

        tick_len = 0.07

        x_ticks = VGroup(*[Line(axes.c2p(i, -tick_len), axes.c2p(i, tick_len), color=BLACK, stroke_width=5)
                  for i in [-4, -3, -2, -1, 1, 2, 3, 4]])

        y_ticks = VGroup(*[Line(axes.c2p(-tick_len, i), axes.c2p(tick_len, i), color=BLACK, stroke_width=5)
                  for i in [1, 2, 3, -1, -2, -3]])

        x_numbers = VGroup(*[MathTex(str(i), font_size=28, color=BLACK).next_to(axes.c2p(i, 0), DOWN)
                    for i in [-4, -3, -2, -1, 1, 2, 3, 4]])

        y_numbers = VGroup(*[MathTex(str(i), font_size=28, color=BLACK).next_to(axes.c2p(0, i), LEFT)
                    for i in [1, 2, 3, -1, -2, -3]])

        zero = MathTex("0", font_size=33, color=BLACK).next_to(axes.c2p(0, 0), DL*0.6).shift(DOWN*0.06)

        y0_line = Line(start=axes.c2p(-5, 0),
                       end=axes.c2p(2, 0),
                       color=BRIGHTPURPLE,
                       stroke_width=7)

        dot_neg2 = Dot(axes.c2p(-2, 0), color=PURE_RED, radius=0.1)
        dot_20 = Dot(axes.c2p(2, 0), color=PURE_RED, radius=0.1)

        label_neg2 = MathTex("(-2,0)", color=BLACK).next_to(dot_neg2, UP)
        label_20 = MathTex("(2,0)", color=BLACK).next_to(dot_20, UP*1)

        triangle = Polygon([-1.5, 0.42, 0], 
                           [-1.5, -0.42, 0], 
                           [0, 0, 0],
                           color=BRIGHTPURPLE, 
                           fill_color=BRIGHTPURPLE, 
                           fill_opacity=1,
                           stroke_width=0).scale(0.36).rotate(PI)
        
        triangle.next_to(axes, LEFT).shift(RIGHT*2)

        arrow1 = Arrow(start=axes.coords_to_point(-4, -0.6),
                      end=axes.coords_to_point(-2.1, -0.6),
                      buff=0,
                      stroke_width=6,
                      color="#FE46A5",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25)
        
        arrow2 = Arrow(start=axes.coords_to_point(-0.2, -0.6),
                      end=axes.coords_to_point(-1.9, -0.6),
                      buff=0,
                      stroke_width=6,
                      color="#FE46A5",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25)
        
        arrow3 = Arrow(start=axes.coords_to_point(0.2, -0.6),
                      end=axes.coords_to_point(1.9, -0.6),
                      buff=0,
                      stroke_width=6,
                      color="#FE46A5",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25)
        
        arrow4 = Arrow(start=axes.coords_to_point(4, -0.6),
                      end=axes.coords_to_point(2.1, -0.6),
                      buff=0,
                      stroke_width=6,
                      color="#FE46A5",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25)
        
        circle = Circle(radius=0.19, color=BLACK, stroke_width=3).move_to([-0.83,0,0])

        minus_plus2_label=MathTex(r"-2^{+}", color=BLACK, font_size=37).next_to(arrow2, DOWN*0.2).shift(LEFT*0.3)
        minus_minus2_label=MathTex(r"-2^{-}", color=BLACK, font_size=37).next_to(arrow1, DOWN*0.35).shift(RIGHT*0.3)
        plus2_label=MathTex(r"2^{+}", color=BLACK, font_size=37).next_to(arrow3, DOWN*0.2).shift(RIGHT*0.3)
        minus2_label=MathTex(r"2^{-}", color=BLACK, font_size=37).next_to(arrow4, DOWN*0.35).shift(LEFT*0.3)

        x1_label=MathTex("x'", color=BLACK).next_to(axes.x_axis, LEFT)
        x2_label=MathTex("y'", color=BLACK).next_to(axes.y_axis, DOWN)

        self.add(axes,
                 x_label, y_label,
                 x_ticks, y_ticks,
                 x_numbers, y_numbers, zero,
                 y0_line,
                 dot_neg2, dot_20,
                 label_neg2, label_20,
                 triangle,
                 circle, arrow1, arrow2, arrow3, arrow4,
                 minus_plus2_label, minus_minus2_label,
                 plus2_label, minus2_label,
                 x1_label, x2_label)
