from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 12
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BRIGHTPINK = "#FE01B1"
BRIGHTRED = "#FF000D"

class Exercise817(Scene):
    def construct(self):
        A = np.array([-4, -2, 0])
        B = np.array([3, -2, 0])
        C = np.array([4, 2, 0])
        D = np.array([-3, 2, 0])

        AB = Line(A, B, color=BRIGHTPINK, stroke_width=4)
        BC = Line(B, C, color=BRIGHTPINK, stroke_width=4)
        CD = Line(C, D, color=BRIGHTPINK, stroke_width=4)
        DA = Line(D, A, color=BRIGHTPINK, stroke_width=4)

        AC = Line(A, C, color=BRIGHTRED, stroke_width=4)

        BD = DashedLine(B, D, dash_length=0.4, dashed_ratio=0.8, color=BRIGHTRED, stroke_width=4)

        BD_helper = Line(B, D)

        def mid_tip(line):
            mid = line.get_center()
            angle = line.get_angle()
            tip = StealthTip(length=0.3, color=BLACK)
            tip.set_stroke(width=-9)
            tip.set_fill(BLACK, opacity=1.5)
            tip.rotate(angle)
            tip.move_to(mid)
            return tip

        def tick_on_line(line, length=0.25, offset=0.0):
            mid = line.point_from_proportion(0.5 + offset)
            angle = line.get_angle() + PI/2
            return Line(
                mid + length/2 * np.array([np.cos(angle), np.sin(angle), 0]),
                mid - length/2 * np.array([np.cos(angle), np.sin(angle), 0]),
                color=BLACK,
                stroke_width=4)

        tip_AB = mid_tip(AB)
        tip_BC = mid_tip(BC).shift(LEFT*0.03)
        tip_CD = mid_tip(CD)
        tip_DA = mid_tip(DA).shift(RIGHT*0.03)
        tip_AC = mid_tip(AC).shift(DOWN*0.55+LEFT*1)

        tick_AB = tick_on_line(AB, length=0.3, offset=0.15)
        tick_CD = tick_on_line(CD, length=0.3, offset=-0.15)

        tick_DA_1 = tick_on_line(DA, length=0.3, offset=-0.15)
        tick_DA_2 = tick_on_line(DA, length=0.3, offset=-0.19)

        tick_BC_1 = tick_on_line(BC, length=0.3, offset=0.15)
        tick_BC_2 = tick_on_line(BC, length=0.3, offset=0.19)

        tick_AC_start_1 = tick_on_line(AC, length=0.3, offset=-0.21)
        tick_AC_start_2 = tick_on_line(AC, length=0.3, offset=-0.23)
        tick_AC_start_3 = tick_on_line(AC, length=0.3, offset=-0.25)

        tick_AC_end_1 = tick_on_line(AC, length=0.3, offset=0.21)
        tick_AC_end_2 = tick_on_line(AC, length=0.3, offset=0.23)
        tick_AC_end_3 = tick_on_line(AC, length=0.3, offset=0.25)

        tick_BD_start_1 = tick_on_line(BD_helper, length=0.3, offset=-0.31)
        tick_BD_start_2 = tick_on_line(BD_helper, length=0.3, offset=-0.33)
        tick_BD_start_3 = tick_on_line(BD_helper, length=0.3, offset=-0.35)
        tick_BD_start_4 = tick_on_line(BD_helper, length=0.3, offset=-0.37)

        tick_BD_end_1 = tick_on_line(BD_helper, length=0.3, offset=0.31)
        tick_BD_end_2 = tick_on_line(BD_helper, length=0.3, offset=0.33)
        tick_BD_end_3 = tick_on_line(BD_helper, length=0.3, offset=0.35)
        tick_BD_end_4 = tick_on_line(BD_helper, length=0.3, offset=0.37)

        tip_BD = StealthTip(length=0.3, color=BLACK)
        tip_BD.set_stroke(width=-9)
        tip_BD.set_fill(BLACK, opacity=1.5)
        tip_BD.rotate(BD_helper.get_angle())
        tip_BD.move_to(BD_helper.point_from_proportion(0.3)).shift(DOWN*0.019)

        label_A = MathTex("A", color=BLACK).next_to(A, DOWN+LEFT, buff=0.2)
        label_B = MathTex("B", color=BLACK).next_to(B, DOWN+RIGHT, buff=0.2)
        label_C = MathTex("C", color=BLACK).next_to(C, UP+RIGHT, buff=0.2)
        label_D = MathTex("D", color=BLACK).next_to(D, UP+LEFT, buff=0.2)

        label_a1 = MathTex(r"\vec{a}", color=BLACK).next_to(AB, DOWN, buff=0.3)
        label_a2 = MathTex(r"\vec{-a}", color=BLACK).next_to(CD, UP, buff=0.3)

        label_b = MathTex(r"\vec{b}", color=BLACK).move_to((A + C)/2 + np.array([-1.5, -0.15, 0]))

        label_b_minus_a = MathTex(r"\vec{b}-\vec{a}", color=BLACK).next_to(BC).shift(LEFT*0.4)
        
        angle_bd = BD.get_angle()
        
        label_b_minus_2a = MathTex(r"\vec{b}-{2}\vec{a}", color=BLACK)

        if np.cos(angle_bd) < 0:
            label_b_minus_2a.rotate(PI)

        label_b_minus_2a.rotate(angle_bd)
        label_b_minus_2a.next_to(BD).shift(LEFT*1.8+DOWN*0.7)

        minus_b_minus_a = MathTex(r"-(\vec{b}-\vec{a})", color=BLACK).next_to(DA, LEFT, buff=-0.2).shift(UP*0.2)

        self.add(AB, BC, CD, DA, AC, BD,
                 tip_AB, tip_BC, tip_CD, tip_DA, tip_AC, tip_BD,
                 tick_AB, tick_CD,
                 tick_DA_1, tick_DA_2,
                 tick_BC_1, tick_BC_2,
                 tick_AC_start_1, tick_AC_start_2, tick_AC_start_3,
                 tick_AC_end_1, tick_AC_end_2, tick_AC_end_3,
                 tick_BD_start_1, tick_BD_start_2, tick_BD_start_3, tick_BD_start_4,
                 tick_BD_end_1, tick_BD_end_2, tick_BD_end_3, tick_BD_end_4,
                 label_A, label_B, label_C, label_D,
                 label_a1, label_a2, minus_b_minus_a,
                 label_b,label_b_minus_2a,
                 label_b_minus_a)

