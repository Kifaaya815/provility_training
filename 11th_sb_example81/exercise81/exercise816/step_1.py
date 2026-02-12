from manim import *
import numpy as np

config.frame_height = 8
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BRIGHTPURPLE = "#BE03FD"
BRIGHTPINK = "#FE01B1"

class Exercise816(Scene):
    def construct(self):

        # ---------------- OUTER SQUARE ----------------
        A = np.array([-2, -2, 0])
        B = np.array([ 2, -2, 0])
        C = np.array([ 2,  2, 0])
        D = np.array([-2,  2, 0])

        AB = Line(A, B, color=BRIGHTPURPLE, stroke_width=4)
        BC = Line(B, C, color=BRIGHTPURPLE, stroke_width=4)
        CD = Line(C, D, color=BRIGHTPURPLE, stroke_width=4)
        DA = Line(D, A, color=BRIGHTPURPLE, stroke_width=4)

        for l in (AB, BC, CD, DA):
            l.set_z_index(3)

        # ---------------- MIDPOINTS ----------------
        P = A + 0.5 * (B - A)
        Q = B + 0.5 * (C - B)
        R = C + 0.5 * (D - C)
        S = D + 0.5 * (A - D)

        # ---------------- INNER QUADRILATERAL ----------------
        PQ = Line(P, Q, color=BRIGHTPINK, stroke_width=3)
        QR = Line(Q, R, color=BRIGHTPINK, stroke_width=3)
        RS = Line(R, S, color=BRIGHTPINK, stroke_width=3)
        SP = Line(S, P, color=BRIGHTPINK, stroke_width=3)

        # ---------------- DIAGONALS ----------------
        AP = Line(A, P, color=BLACK, stroke_width=3)
        BP = Line(B, P, color=BLACK, stroke_width=3)
        CR = Line(C, R, color=BLACK, stroke_width=3)
        DR = Line(D, R, color=BLACK, stroke_width=3)

        # ---------------- ANGLE SECTORS ----------------
        arc_radius = 0.5

        angle_A = Sector(radius=arc_radius, start_angle=0, angle=PI/2,
                          arc_center=A, color=RED_D,
                          fill_color=RED_D, fill_opacity=0.25, stroke_width=3)

        angle_B = Sector(radius=arc_radius, start_angle=PI/2, angle=PI/2,
                          arc_center=B, color=YELLOW_E,
                          fill_color=YELLOW_E, fill_opacity=0.25, stroke_width=3)

        angle_C = Sector(radius=arc_radius, start_angle=PI, angle=PI/2,
                          arc_center=C, color=RED_D,
                          fill_color=RED_D, fill_opacity=0.25, stroke_width=3)

        angle_D = Sector(radius=arc_radius, start_angle=3*PI/2, angle=PI/2,
                          arc_center=D, color=YELLOW_E,
                          fill_color=YELLOW_E, fill_opacity=0.25, stroke_width=3)

        # ---------------- TICK MARKS ----------------
        tick_length = 0.25

        def midpoint_tick(line):
            mid = line.get_midpoint()
            d = line.get_unit_vector()
            n = np.array([-d[1], d[0], 0])
            return Line(
                mid - 0.5 * tick_length * n,
                mid + 0.5 * tick_length * n,
                color=BLACK,
                stroke_width=3
            )

        # Existing ticks
        tick_BP = midpoint_tick(BP).shift(LEFT * 0.1)
        tick_CR = midpoint_tick(CR).shift(RIGHT * 0.01)

        # ✅ NEW ticks (missing ones)
        tick_AP = midpoint_tick(AP)
        tick_DR = midpoint_tick(DR)

        # ---------------- STEALTH TIPS ----------------
        tip_scale = 1.3

        def stealth_tip_only(start, end, along=0.3, normal=0.1):
            direction = end - start
            unit = direction / np.linalg.norm(direction)
            n = np.array([-unit[1], unit[0], 0])

            tip = StealthTip(
                fill_color=BLACK,
                fill_opacity=1,
                stroke_width=0
            ).scale(tip_scale)

            tip.rotate(angle_of_vector(unit))
            tip.move_to(start + along * unit + normal * n)
            tip.set_z_index(10)
            return tip

        tip_BP = stealth_tip_only(P, B, along=1.2, normal=0.10).shift(DOWN * 0.1)
        tip_CR = stealth_tip_only(R, C, along=0.7, normal=-0.12).shift(UP * 0.11)

        # ---------------- LABELS ----------------
        label_A = Tex(r"A\ ($\vec{a}$)", font_size=42, color=BLACK).next_to(A, LEFT*0.4)
        label_B = Tex(r"B\ ($\vec{b}$)", font_size=42, color=BLACK).next_to(B, DOWN*1.8).shift(LEFT*0.2)
        label_C = Tex(r"C\ ($\vec{c}$)", font_size=42, color=BLACK).next_to(C).shift(LEFT*0.1 + DOWN*0.16)
        label_D = Tex(r"D\ ($\vec{d}$)", font_size=42, color=BLACK).next_to(D, UP*1.8).shift(RIGHT*0.2)

        label_P = Tex("P", font_size=36, color=BLACK).next_to(P, DOWN*0.6 + LEFT*1)
        label_Q = Tex("Q", font_size=36, color=BLACK).next_to(Q, DOWN*1.2 + RIGHT*0.4)
        label_R = Tex("R", font_size=36, color=BLACK).next_to(R, UP*0.4 + RIGHT*1)
        label_S = Tex("S", font_size=36, color=BLACK).next_to(S, LEFT*0.4 + UP*1)

        # ---------------- GROUPS ----------------
        shape_objects = VGroup(
            AB, BC, CD, DA,
            PQ, QR, RS, SP,
            AP, BP, CR, DR,
            angle_A, angle_B, angle_C, angle_D,
            tick_AP, tick_BP, tick_CR, tick_DR,
            tip_BP, tip_CR
        )

        label_objects = VGroup(
            label_A, label_B, label_C, label_D,
            label_P, label_Q, label_R, label_S
        )

        # ---------------- ROTATE SHAPE ONLY ----------------
        shape_objects.rotate(-12 * DEGREES, about_point=ORIGIN)

        # ---------------- ADD TO SCENE ----------------
        self.add(shape_objects, label_objects)
