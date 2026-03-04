from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 15
config.pixel_height = 2500
config.pixel_width = 2500
config.background_color = WHITE

BRIGHTPURPLE = "#BE03FD"

class Example9118a(Scene):
    def construct(self):

        axes = Axes(x_range=[-6, 6, 1],
                    y_range=[-4, 7, 1],
                    x_length=10,
                    y_length=10,
                    axis_config={
                        "color": BLACK,
                        "stroke_width": 4,
                        "include_ticks": False,
                        "include_numbers": False,
                        "tip_length": 0.35,
                        "tip_width": 0.25},
                    tips=True).center()

        axes.y_axis.add_tip(at_start=True, tip_length=0.44, tip_width=0.29)
        axes.x_axis.add_tip(at_start=True, tip_length=0.44, tip_width=0.29)

        x_label = MathTex("x", font_size=45, color=BLACK).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y", font_size=45, color=BLACK).next_to(axes.y_axis.get_end(), UP)
        x1_label = MathTex("x'", font_size=45, color=BLACK).next_to(axes.x_axis, LEFT)
        y1_label = MathTex("y'", font_size=45, color=BLACK).next_to(axes.y_axis, DOWN)

        tick_len = 0.07

        x_ticks = VGroup(*[ Line(axes.c2p(i, -tick_len), axes.c2p(i, tick_len),
                            color=BLACK, stroke_width=4)
                            for i in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]])

        y_ticks = VGroup(*[ Line(axes.c2p(-tick_len, i), axes.c2p(tick_len, i),
                            color=BLACK, stroke_width=4)
                            for i in [1, 2, 3, 4, 5, 6, -1, -2, -3]])

        x_numbers = VGroup(*[ MathTex(str(i), font_size=28, color=BLACK).next_to(axes.c2p(i, 0), DOWN)
                              for i in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]])

        y_numbers = VGroup(*[ MathTex(str(i), font_size=28, color=BLACK).next_to(axes.c2p(0, i), LEFT)
                              for i in [1, 2, 3, 4, 5, 6, -1, -2, -3]])

        zero = MathTex("0", font_size=33, color=BLACK).next_to(axes.c2p(0, 0), DL*0.6).shift(DOWN*0.06)

        curve_left = axes.plot( lambda x: 4 - 0.25*(x**2),
                                x_range=[-3.5, -0.23],
                                color=BRIGHTPURPLE,
                                stroke_width=7)

        curve_middle = axes.plot(lambda x: 4 - 0.25*(x**2),
                                 x_range=[0.23, 3.5],
                                 color=BRIGHTPURPLE,
                                 stroke_width=7)

        hole_0 = Dot(axes.c2p(0, 4),
                     radius=0.19,
                     color=BLACK,
                     fill_opacity=0,
                     stroke_width=3)

        hole_2 = Dot(axes.c2p(2, 6),
                     radius=0.19,
                     color=BLACK,
                     fill_opacity=0,
                     stroke_width=3)

        solid_point = Dot(axes.c2p(2, 6),
                          radius=0.1,
                          color=PURE_RED)

        arrow1 = Arrow(axes.c2p(-3, 0.4), axes.c2p(-0.4, 0.4),
                       buff=0, stroke_width=6, color="#FE46A5",
                       tip_length=0.3)

        arrow2 = Arrow(axes.c2p(3, 0.4), axes.c2p(0.4, 0.4),
                       buff=0, stroke_width=6, color="#FE46A5",
                       tip_length=0.3)
        
        arrow3 = Arrow(axes.c2p(3.8, -0.8), axes.c2p(2.1, -0.8),
                       buff=0, stroke_width=6, color="#FE46A5",
                       tip_length=0.3)

        arrow4 = Arrow(axes.c2p(0.5, -0.8), axes.c2p(1.9, -0.8),
                       buff=0, stroke_width=6, color="#FE46A5",
                       tip_length=0.3)

        minus_label = MathTex(r"0^{-}",color=BLACK, font_size=37).next_to(arrow1, UP*0.3).shift(RIGHT*0.2)
        plus_label = MathTex(r"0^{+}",color=BLACK, font_size=37).next_to(arrow2, UP*0.3).shift(LEFT*0.17)
        plus2_label=MathTex(r"2^{+}", color=BLACK, font_size=37).next_to(arrow3, DOWN*0.2)
        minus2_label=MathTex(r"2^{-}", color=BLACK, font_size=37).next_to(arrow4, DOWN*0.35)
        coord_label=MathTex("(2,6)", color=BLACK).next_to(hole_2)
        
        dash_horizontal = DashedLine(axes.coords_to_point(0, 3),
                                     axes.coords_to_point(2, 3),
                                     dash_length=0.1,
                                     color=BLUE_D)

        dash_vertical = DashedLine(axes.coords_to_point(2, 0),
                                   axes.coords_to_point(2, 3),
                                   dash_length=0.1,
                                   color=BLUE_D)


        self.add(dash_horizontal, dash_vertical,
            axes, x_label, y_label, x1_label, y1_label,
            x_ticks, y_ticks,
            x_numbers, y_numbers, zero,
            curve_left, curve_middle, coord_label,
            hole_0, hole_2, solid_point,
            arrow1, arrow2, minus_label, plus_label,
            arrow4, arrow3, plus2_label, minus2_label)