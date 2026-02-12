from manim import *
import numpy as np

config.frame_height = 8
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BRIGHTPINK = "#FE01B1"
BRIGHTRED = "#FF000D"

class Exerc(Scene):
    def construct(self):

        # Parallelogram points
        A = np.array([-4, -2, 0])
        B = np.array([3, -2, 0])
        C = np.array([4, 2, 0])
        D = np.array([-3, 2, 0])

        # Thin outer sides
        AB = Line(A, B, color=BRIGHTPINK, stroke_width=4)
        BC = Line(B, C, color=BRIGHTPINK, stroke_width=4)
        CD = Line(C, D, color=BRIGHTPINK, stroke_width=4)
        DA = Line(D, A, color=BRIGHTPINK, stroke_width=4)

        # Diagonal
        AC = Line(A, C, color=BRIGHTRED, stroke_width=4)

        # Dashed diagonal
        BD = DashedLine(
            B, D,
            dash_length=0.8,
            dashed_ratio=0.6,
            color=BRIGHTRED,
            stroke_width=4
        )

        # -------- MID STEALTH TIP FUNCTION --------
        def mid_tip(line):
            mid = line.get_center()
            angle = line.get_angle()

            tip = StealthTip(
                length=0.3,
                color=BLACK
            )

            tip.set_stroke(width=-9)   
            tip.set_fill(BLACK, opacity=1.5)  

            tip.rotate(angle)
            tip.move_to(mid)

            return tip

        # Create tips
        tip_AB = mid_tip(AB)
        tip_BC = mid_tip(BC).shift(LEFT*0.03)
        tip_CD = mid_tip(CD)
        tip_DA = mid_tip(DA).shift(RIGHT*0.03)
        tip_AC = mid_tip(AC).shift(DOWN*0.04)

        # ---- Labels ----
        label_A = MathTex("A", color=BLACK).next_to(A, DOWN+LEFT, buff=0.2)
        label_B = MathTex("B", color=BLACK).next_to(B, DOWN+RIGHT, buff=0.2)
        label_C = MathTex("C", color=BLACK).next_to(C, UP+RIGHT, buff=0.2)
        label_D = MathTex("D", color=BLACK).next_to(D, UP+LEFT, buff=0.2)

        label_a1 = MathTex(r"\vec{a}", color=BLACK).next_to(AB, DOWN, buff=0.3)
        label_a2 = MathTex(r"\vec{-a}", color=BLACK).next_to(CD, UP, buff=0.3)

        label_b = MathTex(r"\vec{b}", color=BLACK)\
            .move_to((A + C)/2 + np.array([0.2, 0.5, 0]))

        label_b_minus_a = MathTex(r"\vec{b}-\vec{a}", color=BLACK)\
            .next_to(BC).shift(LEFT*0.4)

        # Add everything
        self.add(
            AB, BC, CD, DA,
            AC, BD,
            tip_AB, tip_BC, tip_CD, tip_DA, tip_AC,
            label_A, label_B, label_C, label_D,
            label_a1, label_a2,
            label_b,
            label_b_minus_a
        )