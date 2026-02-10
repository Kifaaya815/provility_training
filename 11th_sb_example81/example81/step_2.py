from manim import *
import numpy as np

config.frame_height= 8
config.frame_width= 10
config.pixel_height= 2800
config.pixel_width= 2800
config.background_color= WHITE

P_PURP = "#6D597A"  

class Example81_1(Scene):
    def construct(self):

        axes= Axes(x_range=[-3, 3],
                   y_range=[-3, 3],
                   x_length=7,
                   y_length=6,
                   axis_config={"color": P_PURP,
                                "include_tip": True,
                                "include_ticks": False,
                                "stroke_width": 9,
                                "tip_shape": StealthTip})

        axes.x_axis.tip.scale(1.5)
        axes.y_axis.tip.scale(1.5)
        axes.x_axis.add_tip(at_start=True, tip_shape=StealthTip, tip_length=0.62, tip_width=0.62)
        axes.y_axis.add_tip(at_start=True, tip_shape=StealthTip, tip_length=0.62, tip_width=0.62)

        axes.move_to(ORIGIN)

        angle= -50*DEGREES
        length= 3

        Q= Line(start=axes.c2p(0, 0),
                end=axes.c2p(
                length*np.cos(angle),
                length*np.sin(angle)), color=BLUE_D, stroke_width=8)

        Q.add_tip(tip_shape=StealthTip, tip_length=0.62, tip_width=0.62)

        Q_label= Text("Q", font_size=36, color=BLACK)
        Q_label.next_to(Q.get_end(), DR, buff=0.15)

        distance_label= Text("60 km", font_size=30, color=BLACK)
        distance_label.next_to(Q.get_center(), UP, buff=-0.2).shift(RIGHT*0.9)

        angle_arc = CurvedArrow(start_point=axes.c2p(0, 0) + RIGHT * 0.95,
                                end_point=axes.c2p(0, 0) + RIGHT * 0.6 + DOWN * 0.7,
                                radius=-1,
                                color=BLACK,
                                stroke_width=4,
                                tip_length=0.2)

        angle_label= MathTex("50^{\\circ}", font_size=40, color=BLACK)
        angle_label.next_to(angle_arc, RIGHT, buff=0.15)

        N = Text("N", font_size=36, color=BLACK).next_to(axes.y_axis.get_end(), UP, buff=0.2)
        S = Text("S", font_size=36, color=BLACK).next_to(axes.y_axis.get_start(), DOWN, buff=0.2)
        E = Text("E", font_size=36, color=BLACK).next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        W = Text("W", font_size=36, color=BLACK).next_to(axes.x_axis.get_start(), LEFT, buff=0.2)

        self.add(axes,
                 Q, Q_label, distance_label,
                 angle_arc, angle_label,
                 N, E, W, S)
