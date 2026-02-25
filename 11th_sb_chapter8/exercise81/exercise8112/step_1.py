from manim import *

config.frame_height = 8
config.frame_width = 10
config.pixel_width = 2500
config.pixel_height = 2500

class Exercise8112a(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        A = LEFT * 1.5 + DOWN * 2
        B = RIGHT * 3 + DOWN * 3
        C = RIGHT * 3 + UP * 3
        D = LEFT * 1.5 + UP * 2

        AC = Line(D, B, color=BLACK)
        DB = Line(A,C ,color=BLACK)

        E = AC.point_from_proportion(0.6)
        F = DB.point_from_proportion(0.6)
        EF = Line(E, F, color="#FF000D").set_z_index(-1)
        AF = Line(D,F,color="#0165FC").set_z_index(-1)
        CF = Line(B,F,color="#0165FC").set_z_index(-1)

        quad = Polygon(A, B, C, D, color=BLACK)

        label_A = Text("D", font_size=28, color=BLACK).next_to(A, DOWN)
        label_B = Text("C", font_size=28, color=BLACK).next_to(B, DOWN)
        label_C = Text("B", font_size=28, color=BLACK).next_to(C, UP)
        label_D = Text("A", font_size=28, color=BLACK).next_to(D, UP)
        label_F = Text("F", font_size=28, color=BLACK).next_to(F, UP)
        label_E = Text("E", font_size=28, color=BLACK).next_to(E, DOWN)

        self.add(AC,DB,EF,AF,CF,quad,label_A, label_B, label_C, label_D,label_F,label_E)