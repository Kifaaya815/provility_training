from manim import *
import numpy as np

config.frame_height = 8
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BROWNGREEN = "#706C11"
DARKPINK = "#E18683"
RED_1 = "#FF000D"

class Example811a(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3],
                    y_range=[-3, 3],
                    x_length=7,
                    y_length=6,
                    axis_config={"color": BROWNGREEN,
                                 "include_tip": True,
                                 "include_ticks": False,
                                 "stroke_width": 9,
                                 "tip_shape": StealthTip})

        axes.x_axis.tip.scale(1.5)
        axes.y_axis.tip.scale(1.5)

        axes.x_axis.add_tip(at_start=True, tip_shape=StealthTip, tip_length=0.62, tip_width=0.62)
        axes.y_axis.add_tip(at_start=True, tip_shape=StealthTip, tip_length=0.62, tip_width=0.62)

        axes.move_to(ORIGIN)

        length = 3.19
        angle = 30*DEGREES

        P = Line(start=axes.c2p(0, 0),
                 end=axes.c2p(length * np.cos(angle), length * np.sin(angle)),
                 color=DARKPINK,
                 stroke_width=8).set_z_index(-1)

        P.add_tip(tip_shape=StealthTip, tip_length=0.62, tip_width=0.62)

        P_label = Tex("P", color=BLACK, font_size=36)
        P_label.next_to(P.get_end(), UR, buff=0.15)

        tip_offset = 5.5 * DEGREES

        angle_arc = Arc(
        radius=1.1,
        start_angle=0,
        angle=angle - tip_offset,
        color=BLACK,
        stroke_width=4).move_arc_center_to(axes.c2p(0, 0))

        angle_arc.add_tip(
        tip_length=0.2,
        tip_width=0.2)

        angle_label = MathTex("30^{\\circ}", font_size=38, color=BLACK)
        angle_label.next_to(angle_arc, buff=0.15)

        distance_label = MathTex(r"45\,\text{cm}", color=BLACK, font_size=40)
        distance_label.rotate(angle)
        distance_label.next_to(P,UP, buff=-0.7).shift(RIGHT*0.3)

        O_label = Tex("O", color=BLACK, font_size=36).move_to(axes.c2p(-0.25, -0.35))
        O_dot = Dot(axes.c2p(0, -0.04), color=RED_1, radius=0.1).set_z_index(10)

        N = Tex("N", color=BLACK, font_size=36).next_to(axes.y_axis.get_end(), UP, buff=0.2)
        S = Tex("S", color=BLACK, font_size=36).next_to(axes.y_axis.get_start(), DOWN, buff=0.2)
        E = Tex("E", color=BLACK, font_size=36).next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        W = Tex("W", color=BLACK, font_size=36).next_to(axes.x_axis.get_start(), LEFT, buff=0.2)

        self.add(axes, P,
                 N, E, W, S,
                 P_label,
                 angle_arc, angle_label,
                 distance_label,
                 O_dot, O_label)