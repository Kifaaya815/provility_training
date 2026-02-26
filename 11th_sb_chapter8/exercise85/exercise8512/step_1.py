from manim import *
import numpy as np

config.frame_height = 8
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BLUE = "#1E88E5"
RED = "#E53935"

class Exercise8512(Scene):
    def construct(self):

        A = np.array([-3, 2, 0])
        B = np.array([ 3, 2, 0])
        O = np.array([ 0,-2.5, 0])
        P = np.array([ 0, 2, 0])

        AB = Line(A, B, color=BLUE, stroke_width=3)
        OA = Line(O, A, color=BLUE, stroke_width=3)
        OB = Line(O, B, color=BLUE, stroke_width=3)
        OP = Line(O, P, color=RED, stroke_width=3)

        def mid_tip(line, color=BLACK):
            mid = line.point_from_proportion(0.5)
            angle = line.get_angle()
            tip = StealthTip(length=0.25, color=color)
            tip.rotate(angle)
            tip.move_to(mid)
            return tip

        tip_a = mid_tip(OA).shift(RIGHT*0.03)
        tip_b = mid_tip(OB).shift(LEFT*0.03)
        tip_r = mid_tip(OP)

        label_A = MathTex("A",color=BLACK).next_to(A, LEFT)
        label_B = MathTex("B",color=BLACK).next_to(B, RIGHT)
        label_P = MathTex("P",color=BLACK).next_to(P, UP*0.7)
        label_O = MathTex("O",color=BLACK).next_to(O, DOWN)

        label_a = MathTex(r"\vec a",color=BLACK).next_to(OA, LEFT).shift(RIGHT*1.2)
        label_b = MathTex(r"\vec b",color=BLACK).next_to(OB, RIGHT).shift(LEFT*1.2)
        label_r = MathTex(r"\vec r", color=BLACK).next_to(OP, RIGHT)

        label_mn = MathTex("m : n", color=PURE_RED).next_to(P, UP*5.6)
        label_79 = MathTex("7 : 9", color=BLACK).next_to(P, UP*3.1).shift(RIGHT*0.06)

        curve_start = P + UP*1.9+RIGHT*0.4            
        curve_control1 = curve_start + UP*1.8 
        curve_control2 = np.array([-7, 3, 0])  
        curve_end = np.array([-2.7, -0.2, 0])      

        red_curve = CubicBezier(curve_start,
                                curve_control1,
                                curve_control2,
                                curve_end,
                                color=RED,
                                stroke_width=3)

        p1 = red_curve.point_from_proportion(0.98)
        p2 = red_curve.point_from_proportion(1.0)
        angle = np.arctan2(p2[1] - p1[1], p2[0] - p1[0])

        curve_tip = StealthTip(color=RED, length=0.25)
        curve_tip.rotate(angle)
        curve_tip.move_to(curve_end).shift(UP*0.019)

        curve2_start = P + UP*1.9 + LEFT*0.4
        curve2_control1 = curve2_start + UP*1.8
        curve2_control2 = np.array([7, 3, 0])
        curve2_end = np.array([2.7, -0.2, 0])

        red_curve_2 = CubicBezier(curve2_start,
                                  curve2_control1,
                                  curve2_control2,
                                  curve2_end,
                                  color=RED,
                                  stroke_width=3)

        q1 = red_curve_2.point_from_proportion(0.98)
        q2 = red_curve_2.point_from_proportion(1.0)
        angle2 = np.arctan2(q2[1] - q1[1], q2[0] - q1[0])

        curve2_tip = StealthTip(color=RED, length=0.25)
        curve2_tip.rotate(angle2)
        curve2_tip.move_to(curve2_end).shift(UP*0.019)

        self.add(OP, AB, OA, OB,
                 tip_a, tip_b, tip_r,
                 label_A, label_B, label_P, label_O,
                 label_a, label_b, label_r,
                 label_mn, red_curve, curve_tip,
                 red_curve_2, curve2_tip, label_79)
