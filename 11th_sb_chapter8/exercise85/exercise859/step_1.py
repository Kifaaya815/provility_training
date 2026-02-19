from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 12
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

DUSTYROSE = "#C0737A"
DUSTYBLUE = "#5A86AD"
FADEDORANGE = "#F0944D"

class Exercise859(Scene):
    def construct(self):
        A = np.array([-4, -2, 0])
        B = np.array([4, -2, 0])
        C = np.array([4, 2, 0])
        D = np.array([-4, 2, 0])

        AB = Line(A, B, color=FADEDORANGE, stroke_width=4)
        BC = Line(B, C, color=FADEDORANGE, stroke_width=4)
        CD = Line(C, D, color=FADEDORANGE, stroke_width=4)
        DA = Line(D, A, color=FADEDORANGE, stroke_width=4)

        AB.set_length(AB.get_length() + 0.03)
        BC.set_length(BC.get_length() + 0.03)
        CD.set_length(CD.get_length() + 0.03)
        DA.set_length(DA.get_length() + 0.03)

        AC = Line(A, C, color=DUSTYROSE, stroke_width=4)

        BD = Line(B, D,  color=DUSTYBLUE, stroke_width=4)

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
        tip_BC = mid_tip(BC)
        tip_CD = mid_tip(CD)
        tip_DA = mid_tip(DA).rotate(angle=179.1)
        tip_AC = mid_tip(AC).shift(DOWN*0.55+LEFT*1)

        tick_AB = tick_on_line(AB, length=0.3, offset=0.15)
        tick_CD = tick_on_line(CD, length=0.3, offset=-0.15)

        tick_DA_1 = tick_on_line(DA, length=0.3, offset=-0.15)
        tick_DA_2 = tick_on_line(DA, length=0.3, offset=-0.19)

        tick_BC_1 = tick_on_line(BC, length=0.3, offset=0.15)
        tick_BC_2 = tick_on_line(BC, length=0.3, offset=0.19)

        tip_BD = StealthTip(length=0.3, color=BLACK)
        tip_BD.set_stroke(width=-9)
        tip_BD.set_fill(BLACK, opacity=1.5)
        tip_BD.rotate(BD_helper.get_angle())
        tip_BD.move_to(BD_helper.point_from_proportion(0.3)).shift(DOWN*0.04)

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
        label_a_plus_b.next_to(AC).shift(LEFT*6.9+DOWN*0.5)

        label_b= MathTex(r"\vec{b}", color=BLACK).next_to(BC).shift(LEFT*0)
        
        angle_bd = BD.get_angle()
        
        label_b_minus_a = MathTex(r"\vec{b}-\vec{a}", color=BLACK)

        if np.cos(angle_bd) < 0:
            label_b_minus_a.rotate(PI)

        label_b_minus_a.rotate(angle_bd)
        label_b_minus_a.next_to(BD).shift(LEFT*2.3+DOWN*0.7)

        minus_b = MathTex(r"\vec{b}", color=BLACK).next_to(DA, LEFT)

        self.add(AC, BD, AB, BC, CD, DA, 
                 tip_AB, tip_BC, tip_CD, tip_DA, tip_AC, tip_BD,
                 tick_AB, tick_CD,
                 tick_DA_1, tick_DA_2,
                 tick_BC_1, tick_BC_2,
                 label_A, label_B, label_C, label_D,
                 label_a1, label_a2, minus_b,
                 label_a_plus_b,label_b_minus_a,
                 label_b)