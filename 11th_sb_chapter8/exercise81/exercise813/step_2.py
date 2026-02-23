from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 12
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

AMETHYST = "#9B5FC0"

class Exercise813b(Scene):
    def construct(self):

        A = np.array([-3, 2, 0])
        B = np.array([ 3, 2, 0])
        O = np.array([ 0,-2.5, 0])
        P = np.array([ 0, 2, 0])

        triangle = Polygon(A, B, O, color=AMETHYST, stroke_width=3, fill_opacity=0)

        AB = Line(A, B)
        OA = Line(O, A)
        OB = Line(O, B)

        def double_tick(line, proportion, size=0.12, gap=0.12):
            point = line.point_from_proportion(proportion)
            direction = line.get_unit_vector()
            normal = rotate_vector(direction, PI/2)

            tick1 = Line(point + normal * size,
                         point - normal * size,
                         color=BLACK,
                         stroke_width=3)
            tick2 = tick1.copy().shift(direction * gap)
            return VGroup(tick1, tick2)

        dt1 = double_tick(AB, 0.84)
        dt2 = double_tick(AB, 0.53)
        dt3 = double_tick(AB, 0.15)

        def mid_tip_on_line(line):
            point = line.point_from_proportion(0.5)
            direction = line.get_unit_vector()
            tip = StealthTip(length=0.28, color=BLACK)
            tip.rotate(line.get_angle())
            tip.move_to(point + direction * (-0.15))
            return tip

        mid_AB_tip = mid_tip_on_line(AB)

        def mid_tip(line):
            mid = line.point_from_proportion(0.5)
            tip = StealthTip(length=0.25, color=BLACK)
            tip.rotate(line.get_angle())
            tip.move_to(mid)
            return tip

        tip_a = mid_tip(OA).shift(RIGHT*0.03)
        tip_b = mid_tip(OB).shift(LEFT*0.03)

        label_A = MathTex("A", color=BLACK).next_to(A, LEFT)
        label_B = MathTex("B", color=BLACK).next_to(B, RIGHT)
        label_O = MathTex("O", color=BLACK).next_to(O, DOWN)
        label_P = MathTex("P", color=BLACK).next_to(P, UP*1.2 + LEFT*3.5)
        label_Q = MathTex("Q", color=BLACK).next_to(P, UP*1 + RIGHT*3.6)

        label_a = MathTex(r"\vec a", color=BLACK).next_to(OA, LEFT).shift(RIGHT*1.2)
        label_b = MathTex(r"\vec b", color=BLACK).next_to(OB, RIGHT).shift(LEFT*1.2)

        dot_P = Dot(P, color=PURE_BLUE).next_to(P, LEFT*4)
        dot_Q = Dot(P, color=PURE_BLUE).next_to(P, RIGHT*4)

        label_1 = MathTex("1", color=PURE_RED).next_to(dot_P, DOWN*1.5+LEFT*1.7)
        label_2 = MathTex("2", color=PURE_RED).next_to(dot_Q, DOWN*1.6+LEFT*0.8)

        right_triangle = VGroup(triangle, dot_P, dot_Q,
                                dt1, dt2, dt3,
                                mid_AB_tip, tip_a, tip_b,
                                label_A, label_B, label_O, label_P, label_Q,
                                label_a, label_b,
                                label_1, label_2).shift(RIGHT * 4.2)

        O_shifted = right_triangle[0].get_vertices()[2]  
        OP_line = Line(O_shifted, dot_P.get_center(), color=PURE_RED, stroke_width=3)

        OP_mid = OP_line.point_from_proportion(0.5)
        OP_tip = StealthTip(length=0.28, color=BLACK)
        OP_tip.rotate(OP_line.get_angle())
        OP_tip.move_to(OP_mid).shift(LEFT*0.09+UP*0.5)

        OP_group = VGroup(OP_line, OP_tip)
        new_group = VGroup(OP_group, right_triangle).shift(LEFT * 4)

        self.add(new_group)