from manim import *
import numpy as np

config.frame_height = 17
config.frame_width = 19
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BLUE1 = "#015482"
BLUE2 = "#00555A"
BLUE3 = "#017374"

class Exercise8210(Scene):
    def construct(self):

        A = np.array([-4, 0, 0])

        AD = Line(A, [3, 3, 0], color=BLUE1)
        AC = Line(A, [3.5, 0, 0], color=BLUE2)
        AB = Line(A, [3, -3, 0], color=BLUE3)

        AD.add_tip(tip_shape=StealthTip)
        AC.add_tip(tip_shape=StealthTip)
        AB.add_tip(tip_shape=StealthTip)

        def middle_arrow(line, length=0.8):
            angle = line.get_angle()
            center = line.point_from_proportion(0.5)

            direction = np.array([np.cos(angle), np.sin(angle), 0])
            start = center - direction * length / 2
            end = center + direction * length / 2

            return Arrow(
                start=start,
                end=end,
                color=line.get_color(),
                buff=0,
                stroke_width=0,
                max_tip_length_to_length_ratio=0.38
            )

        AD_mid = middle_arrow(AD)
        AC_mid = middle_arrow(AC)
        AB_mid = middle_arrow(AB)

        A_label = MathTex("A", color=BLACK).next_to(A, LEFT)
        D_label = MathTex("D", color=BLACK).next_to(AD.get_end(), RIGHT * 0.5)
        C_label = MathTex("C", color=BLACK).next_to(AC.get_end(), RIGHT)
        B_label = MathTex("B", color=BLACK).next_to(AB.get_end(), RIGHT * 0.5)
        origin_label = Text("(origin)", color=BLACK, font_size=33)\
            .next_to(A, DOWN * 1.2).shift(LEFT * 0.4)

        # ---- VECTOR LABELS (ADDED) ----
        AD_label = MathTex(r"\vec{AD}", color=BLACK).next_to(AD).shift(LEFT*4.2+UP*0.6)
        AC_label = MathTex(r"\vec{AC}", color=BLACK).next_to(AC).shift(DOWN*0.46+LEFT*3.4)
        AB_label = MathTex(r"\vec{AB}", color=BLACK).next_to(AB).shift(LEFT*4.2+DOWN*0.6)

        grp = VGroup(
            AD, AC, AB,
            AD_mid, AC_mid, AB_mid,
            A_label, B_label, C_label, D_label,
            origin_label,
            AD_label, AC_label, AB_label
        ).shift(LEFT * 4)

        rect = Rectangle(
            height=1.2,
            width=6,
            color=BLACK,
            stroke_width=1.5
        ).next_to(grp, RIGHT * 6).shift(DOWN * 0.5)

        rect_text = MathTex(
            "A, B, C, D\\ \\text{Coplanar}",
            color=BLACK,
            font_size=60
        ).shift(RIGHT * 4.6 + DOWN * 0.6)

        self.add(
            AD, AC, AB,
            AD_mid, AC_mid, AB_mid,
            A_label, B_label, C_label, D_label,
            origin_label,
            AD_label, AC_label, AB_label,
            rect, rect_text
        )

