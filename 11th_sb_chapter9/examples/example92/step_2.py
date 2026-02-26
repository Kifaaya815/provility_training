from manim import *
import numpy as np

config.frame_height = 9
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BURNTORANGE = "#C04E01"

class Example92b(Scene):
    def construct(self):

        axes = Axes(x_range=[-1.2, 6, 1],
                    y_range=[-1.2, 6, 1],
                    x_length=8,
                    y_length=8,
                    tips=False,
                    axis_config={"color": BLACK,
                                 "stroke_width": 3,
                                 "include_ticks": False,
                                 "include_numbers": False})

        axes.shift(LEFT * 0.5 + DOWN * 0.5).set_z_index(10)

        for axis in [axes.x_axis, axes.y_axis]:
            axis.add_tip(tip_length=0.35, tip_width=0.25,
                         at_start=True)
            axis.add_tip(tip_length=0.35, tip_width=0.25,
                         at_start=False)

        origin_label = MathTex("0", font_size=40, color=BLACK)
        origin_label.next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.15)

        x_label = MathTex("x", font_size=45, color=BLACK)
        y_label = MathTex("y", font_size=45, color=BLACK)

        x_label.next_to(axes.x_axis.get_end())
        y_label.next_to(axes.y_axis.get_end(), UP)

        sqrt_curve = ParametricFunction(lambda t: axes.c2p(t, np.sqrt(t)),
                                        t_range=[0, 5.6],
                                        color=BURNTORANGE,
                                        stroke_width=5)

        end_point = sqrt_curve.get_end()
        prev_point = sqrt_curve.point_from_proportion(0.6)

        curve_arrow = Arrow(prev_point,
                            end_point,
                            buff=0,
                            max_tip_length_to_length_ratio=0.6,
                            stroke_width=0,
                            tip_length=0.25,
                            color=BURNTORANGE).shift(RIGHT*0.1+UP*0.03)

        func_label = MathTex("f(x)=\\sqrt{x},\\ x>0", color=BLACK)
        func_label.scale(0.9)
        func_label.next_to(sqrt_curve, UP, buff=0).shift(RIGHT * 1.3)
        func_label.rotate(PI/14)

        tick_positions = [1, 2, 3, 4, 5]
        tick_labels = ["1", "2", "3", "4", "9"]

        y_ticks = VGroup()
        y_tick_labels = VGroup()

        for pos, lab in zip(tick_positions, tick_labels):
            y_pos = axes.c2p(0, pos)

            tick = Line(y_pos + LEFT * 0.12,
                        y_pos + RIGHT * 0.12,
                        color=BLACK,
                        stroke_width=3)

            label = MathTex(lab, color=BLACK, font_size=36)
            label.next_to(tick, LEFT, buff=0.25)

            y_ticks.add(tick)
            y_tick_labels.add(label)

        x_positions = [1, 2, 3, 4]

        x_ticks = VGroup()
        x_tick_labels = VGroup()

        for val in x_positions:
            x_pos = axes.c2p(val, 0)

            tick = Line(x_pos + UP * 0.12,
                        x_pos + DOWN * 0.12,
                        color=BLACK,
                        stroke_width=3)   

            label = MathTex(str(val), color=BLACK, font_size=36)
            label.next_to(tick, DOWN, buff=0.25)

            x_ticks.add(tick)
            x_tick_labels.add(label)

        origin_point = axes.c2p(0, 0)

        origin_dot = Dot(origin_point, radius=0.06, color=PURE_BLUE, z_index=10)
        origin_circle = Circle(radius=0.15, color=BLACK, stroke_width=3).move_to(origin_point)

        point_11 = axes.c2p(1, 1)
        dot_11 = Dot(point_11, radius=0.06, color=PURE_BLUE)
        circle_11 = Circle(radius=0.15, color=BLACK, stroke_width=3).move_to(point_11)

        point_12 = axes.c2p(2.8, 1.66)
        dot_12 = Dot(point_12, radius=0.06, color=PURE_BLUE)
        circle_12 = Circle(radius=0.15, color=BLACK, stroke_width=3).move_to(point_12)

        point_13 = axes.c2p(3.6, 1.89)
        dot_13 = Dot(point_13, radius=0.06, color=PURE_BLUE)
        circle_13 = Circle(radius=0.15, color=BLACK, stroke_width=3).move_to(point_13)

        origin_coord = MathTex("(0,0)", color=BLACK, font_size=35)\
            .next_to(origin_label, DOWN * 0.5).shift(LEFT * 0.3)

        self.add(axes, origin_coord,
                 sqrt_curve,
                 origin_label,
                 x_label, y_label,
                 func_label,
                 y_ticks, y_tick_labels,
                 x_ticks, x_tick_labels,
                 origin_dot, origin_circle,
                 dot_11, circle_11,
                 dot_12, circle_12,
                 dot_13, circle_13, curve_arrow)