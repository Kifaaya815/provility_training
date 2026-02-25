from manim import *
import numpy as np

config.frame_height = 8
config.frame_width = 10
config.pixel_width = 2500
config.pixel_height = 2500


class Exercise8112d(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        A = np.array([-4, 2, 0])
        C = np.array([3, -3, 0])
        E = np.array([0.2, -1, 0])
        F = E + np.array([0, 2.2, 0])

        AC = Line(A, C, color="#FF63E9", stroke_width=4)

        AF = Line(A, F, color="#FF63E9", stroke_width=4)
        EF = Line(E, F, color=RED, stroke_width=4)
        CF = Line(C, F, color="#FF63E9", stroke_width=4)

        def manual_tip(
            line,
            color=BLACK,
            proportion=0.5,
            angle_offset=0,
            shift_amount=0):

            tip = ArrowTriangleFilledTip(length=0.27,
                                         width=0.25,
                                         color=color)

            base_angle = line.get_angle() - PI / 2
            tip.rotate(base_angle + angle_offset)
            tip.move_to(line.point_from_proportion(proportion))

            direction = line.get_unit_vector()
            tip.shift(direction * shift_amount)

            return tip

        tip_AF = manual_tip(AF,
                            proportion=0.45,
                            angle_offset=4.8,
                            shift_amount=0.1)

        tip_EF = manual_tip(EF,
                            color=BLACK,
                            proportion=0.5,
                            angle_offset=4.7,
                            shift_amount=0.0)

        tip_CF = manual_tip(CF,
                            proportion=0.55,
                            angle_offset=4.7,
                            shift_amount=0.0).shift(RIGHT * 0.03)

        def add_ticks(line, n=2, size=0.3, color=BLACK, center=0.5, spacing=0.03):
            ticks = VGroup()
            direction = line.get_unit_vector()
            normal = rotate_vector(direction, PI / 2)

            start = center - spacing / 2

            for i in range(n):
                alpha = start + i * spacing
                point = line.point_from_proportion(alpha)

                tick = Line(point - normal * size / 2,
                            point + normal * size / 2,
                            color=color,
                            stroke_width=3)
                ticks.add(tick)

            return ticks

        AE = Line(A, E)
        EC = Line(E, C)

        ticks_AE = add_ticks(AE, center=0.5, spacing=0.025)
        ticks_EC = add_ticks(EC, center=0.5, spacing=0.035)

        label_A = Text("A", color=BLACK, font_size=28).next_to(A, UP + LEFT)
        label_C = Text("C", color=BLACK, font_size=28).next_to(C, DOWN + RIGHT)
        label_E = Text("E", color=BLACK, font_size=28).next_to(E, DOWN)
        label_F = Text("F", color=BLACK, font_size=28).next_to(F, UP)

        label_11=MathTex("1", color=BLACK).next_to(ticks_AE, DOWN*0.3+LEFT*0.1)
        label_12=MathTex("1", color=BLACK).next_to(ticks_EC, DOWN*0.3+LEFT*0.1)

        self.add(AC, label_11, label_12,
                 AF, EF, CF,
                 tip_AF, tip_EF, tip_CF,
                 ticks_AE, ticks_EC,
                 label_A, label_C, label_E, label_F)