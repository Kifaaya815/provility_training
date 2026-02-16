from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 12
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BLUE1="#015482"
BLUE2="#00555A"
BLUE3="#017374"

class Exercise8210(Scene):
    def construct(self):

        # -------- POINT A --------
        A = np.array([-4, 0, 0])

        # -------- RAYS --------
        AD = Line(A, [3, 3, 0], color=BLUE1)
        AC = Line(A, [3.5, 0, 0], color=BLUE2)
        AB = Line(A, [3, -3, 0], color=BLUE3)

        # -------- END TIPS (STEALTH) --------
        AD.add_tip(tip_shape=StealthTip)
        AC.add_tip(tip_shape=StealthTip)
        AB.add_tip(tip_shape=StealthTip)

        # -------- MIDDLE ARROWS (NORMAL) --------
        def middle_arrow(line, length=0.8):
            angle = line.get_angle()
            center = line.point_from_proportion(0.5)

            direction = np.array([np.cos(angle), np.sin(angle), 0])
            start = center - direction * length / 2
            end = center + direction * length / 2

            return Arrow(start=start,
                             end=end,
                             color=line.get_color(),
                             buff=0,
                             stroke_width=0,                  # ← hides the line
                             max_tip_length_to_length_ratio=0.38)

        AD_mid = middle_arrow(AD)
        AC_mid = middle_arrow(AC)
        AB_mid = middle_arrow(AB)

        # -------- LABELS --------
        A_label = MathTex("A", color=BLACK).next_to(A, LEFT)
        D_label = MathTex("D", color=BLACK).next_to(AD.get_end(), UP*0+RIGHT*0.5)
        C_label = MathTex("C", color=BLACK).next_to(AC.get_end(), RIGHT)
        B_label = MathTex("B", color=BLACK).next_to(AB.get_end(), DOWN*0+RIGHT*0.5)

        # -------- ADD --------
        self.add(
            AD, AC, AB,
            AD_mid, AC_mid, AB_mid,
            A_label, B_label, C_label, D_label
        )
