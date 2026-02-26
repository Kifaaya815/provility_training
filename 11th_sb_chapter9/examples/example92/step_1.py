from manim import *
import numpy as np

config.frame_height = 11
config.frame_width = 12
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE


class Example921(Scene):
    def construct(self):

        left = -5
        right = 5

        base_line = Line(np.array([left, 0, 0]),
                         np.array([right, 0, 0]),
                         color=BLACK,
                         stroke_width=4)

        left_arrow = Arrow(start=np.array([left + 0.8, 0, 0]),
                           end=np.array([left, 0, 0]),
                           buff=0,
                           color=BLACK,
                           stroke_width=4,
                           tip_shape=StealthTip)

        right_arrow = Arrow(start=np.array([right - 0.8, 0, 0]),
                            end=np.array([right, 0, 0]),
                            buff=0,
                            color=BLACK,
                            stroke_width=4,
                            tip_shape=StealthTip)

        self.add(base_line, left_arrow, right_arrow)

        origin_tick = Line(UP * 0.25,
                           DOWN * 0.25,
                           color=BLACK,
                           stroke_width=4)

        zero_label = MathTex("0", color=BLACK).next_to(origin_tick, DOWN, buff=0.25)

        self.add(origin_tick, zero_label)

        left_inner = Arrow(start=np.array([-0.6, 0, 0]),
                           end=np.array([-1.8, 0, 0]),
                           buff=0,
                           color=BLACK,
                           stroke_width=4,
                           tip_shape=StealthTip).shift(RIGHT*0.4)

        right_inner = Arrow(start=np.array([0.6, 0, 0]),
                            end=np.array([1.8, 0, 0]),
                            buff=0,
                            color=BLACK,
                            stroke_width=4,
                            tip_shape=StealthTip).shift(LEFT*0.4)

        self.add(left_inner, right_inner)

        lhl = MathTex(r"\text{L.H.L}", color=BLACK).scale(0.9).next_to(left_inner, UP, buff=1).shift(LEFT*1.5)
        lhl_val = MathTex(r"0^{-}", color=BLACK).next_to(lhl, DOWN, buff=0.35)

        rhl = MathTex(r"\text{R.H.L}", color=BLACK).scale(0.9).next_to(right_inner, UP, buff=1).shift(RIGHT*1.5)
        rhl_val = MathTex(r"0^{+}", color=BLACK).next_to(rhl, DOWN, buff=0.3)

        self.add(lhl, lhl_val, rhl, rhl_val)

        left_brace = Brace(Line(np.array([-3.5, 0, 0]), np.array([-0.4, 0, 0])),
                           DOWN,
                           color=BLACK).shift(DOWN*0.15+LEFT*1)

        not_defined = MathTex(r"f(x)\ \text{not defined}", color=BLACK, font_size=40)
        not_defined.next_to(left_brace, DOWN, buff=0.42)

        self.add(left_brace, not_defined)

        fx0 = MathTex(r"f(x)=0", color=BLACK, font_size=40)
        fx0.next_to(origin_tick, DOWN, buff=0.8)

        fxroot = MathTex(r"f(x)=\sqrt{x}", color=BLACK, font_size=40)
        fxroot.next_to(np.array([3.5, 0, 0]), DOWN, buff=1).shift(LEFT*0.9)

        self.add(fx0, fxroot)