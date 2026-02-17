from manim import *
import numpy as np

config.frame_height = 8
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

LIGHTMAGENTA = "#FA5FF7"
LIGHTMAROON = "#A24857"

class Exercise8512(Scene):
    def construct(self):
        line = Line(start=LEFT*4,
                    end=RIGHT*4,
                    color=LIGHTMAROON,
                    stroke_width=5)

        tick_p = Line(UP*0.2, DOWN*0.2, color=LIGHTMAGENTA, stroke_width=4)
        tick_p1 = Line(UP*0.2, DOWN*0.2, color=BLACK, stroke_width=7)

        center_AB = line.get_center()

        tick_p.move_to(center_AB)
        tick_p1.move_to(center_AB)

        label_A = MathTex(r"\vec{b}", font_size=36, color=BLACK).next_to(line.get_start(), DOWN*1)
        label_B = MathTex(r"\vec{a}", font_size=36, color=BLACK).next_to(line.get_end(), DOWN*1)

        label_P = MathTex("7:9", font_size=36, color=BLACK).next_to(tick_p, UP)

        self.add(line, tick_p1,
                 tick_p,
                 label_A, label_P, label_B)