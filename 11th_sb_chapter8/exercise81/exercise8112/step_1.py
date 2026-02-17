from manim import *

config.frame_height = 8
config.frame_width = 10
config.pixel_width = 2500
config.pixel_height = 2500
config.background_color=WHITE

class Exercise8112(Scene):
    def construct(self):

        A = LEFT*3 + DOWN*2
        B = RIGHT*3 + DOWN*2.5
        C = RIGHT*3 + UP*1.5
        D = LEFT*3 + UP*2

        AC = Line(A, C, color=BLUE)
        DB = Line(D, B, color=BLUE)

        E = AC.point_from_proportion(0.4)
        F = DB.point_from_proportion(0.6)

        EF = Line(E, F, color=GREEN_C)

        quad = Polygon(A, B, C, D, color=BLUE_E)

        quad.set_z_index(10)
        EF.set_z_index(8)
        AC.set_z_index(9)
        DB.set_z_index(9)

        label_A = Text("A", font_size=28, color=BLACK).next_to(A, DOWN)
        label_B = Text("B", font_size=28, color=BLACK).next_to(B, DOWN)
        label_C = Text("C", font_size=28, color=BLACK).next_to(C, UP)
        label_D = Text("D", font_size=28, color=BLACK).next_to(D, UP)

        label_E = Text("E", font_size=28, color=BLACK).next_to(E, LEFT).shift(UP*0.06)
        label_F = Text("F", font_size=28, color=BLACK).next_to(F, RIGHT).shift(UP*0.04)

        self.add(quad, AC, DB, EF,
                 label_A, label_B, label_C, label_D,
                 label_E, label_F)