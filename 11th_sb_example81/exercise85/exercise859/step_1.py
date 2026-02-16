from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 12
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

DUSTYROSE = "#C0737A"
DUSTYTEAL = "#4C9085"

class Exercise859(Scene):
    def construct(self):
        A = np.array([-4, -2, 0])
        B = np.array([4, -2, 0])
        C = np.array([4, 2, 0])
        D = np.array([-4, 2, 0])

        AB = Line(A, B, color=DUSTYTEAL, stroke_width=4)
        BC = Line(B, C, color=DUSTYTEAL, stroke_width=4)
        CD = Line(C, D, color=DUSTYTEAL, stroke_width=4)
        DA = Line(D, A, color=DUSTYTEAL, stroke_width=4)

        BD = Line(B, D, color=DUSTYROSE, stroke_width=4)

        AC = DashedLine(A, C, dash_length=0.4, dashed_ratio=0.8, color=DUSTYROSE, stroke_width=4)

        def mid_tip(line):
            mid = line.get_center()
            angle = line.get_angle()
            tip = StealthTip(length=0.3, color=BLACK)
            tip.set_stroke(width=-9)
            tip.set_fill(BLACK, opacity=1.5)
            tip.rotate(angle)
            tip.move_to(mid)
            return tip

        tip_AB = mid_tip(AB)
        tip_BC = mid_tip(BC)
        tip_CD = mid_tip(CD)
        tip_DA = mid_tip(DA)

        label_A = MathTex("A", color=BLACK).next_to(A, DOWN+LEFT, buff=0.2)
        label_B = MathTex("B", color=BLACK).next_to(B, DOWN+RIGHT, buff=0.2)
        label_C = MathTex("C", color=BLACK).next_to(C, UP+RIGHT, buff=0.2)
        label_D = MathTex("D", color=BLACK).next_to(D, UP+LEFT, buff=0.2)

        label_a1 = MathTex(r"\vec{a}", color=BLACK).next_to(AB, DOWN, buff=0.3)
        label_a2 = MathTex(r"\vec{-a}", color=BLACK).next_to(CD, UP, buff=0.3)

        label_a_plus_b = MathTex(r"\vec{a}+\vec{b}", color=BLACK).move_to((A + C)/2 + np.array([-1.5, -0.15, 0]))

        angle_ac = AC.get_angle()

        if np.cos(angle_ac) < 0:
            label_a_plus_b.rotate(PI)

        label_a_plus_b.rotate(angle_ac)
        label_a_plus_b.next_to(AC).shift(LEFT*6.5+DOWN*0.2)

        label_b= MathTex(r"\vec{b}", color=BLACK).next_to(BC).shift(LEFT*0)

        minus_b = MathTex(r"-\vec{b}", color=BLACK).next_to(DA, LEFT)

        self.add(AB, BC, CD, DA, AC, BD,
                 tip_AB, tip_BC, tip_CD, tip_DA,
                 label_A, label_B, label_C, label_D,
                 label_a1, label_a2, minus_b,
                 label_a_plus_b,
                 label_b)