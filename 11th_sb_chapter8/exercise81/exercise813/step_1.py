from manim import *
import numpy as np

config.frame_height = 8
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

AMETHYST ="#9B5FC0"
BRIGHTSKYBLUE = "#02CCFE"

class Exercise813(Scene):
    def construct(self):

        line = Line(start=LEFT*4,
                    end=RIGHT*4,
                    color=AMETHYST,
                    stroke_width=5)

        tick_p = Line(UP*0.2, DOWN*0.2, color=BRIGHTSKYBLUE, stroke_width=4)
        tick_p1 = Line(UP*0.2, DOWN*0.2, color=BLACK, stroke_width=7)

        tick_q = Line(UP*0.2, DOWN*0.2, color=BRIGHTSKYBLUE, stroke_width=4)
        tick_q1 = Line(UP*0.2, DOWN*0.2, color=BLACK, stroke_width=7)

        tick_p.move_to(LEFT*1.2)
        tick_p1.move_to(LEFT*1.2)

        tick_q.move_to(RIGHT*1.2)
        tick_q1.move_to(RIGHT*1.2)

        label_A = Text("A", font_size=36, color=BLACK).next_to(line.get_start(), DOWN*1.5)
        label_B = Text("B", font_size=36, color=BLACK).next_to(line.get_end(), DOWN*1.5)

        label_P = Text("P", font_size=36, color=BLACK).next_to(tick_p, DOWN)
        label_Q = Text("Q", font_size=36, color=BLACK).next_to(tick_q, DOWN)

        self.add(line, tick_p1, tick_q1,
                 tick_p, tick_q,
                 label_A, label_P, label_Q, label_B)