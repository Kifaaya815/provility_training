from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 15
config.pixel_width = 2800
config.pixel_height = 2800


class Exercise145b(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        #rectangle
        rectangle = Rectangle(width=10.5, height=6.8,
                              stroke_color=BLUE_E,
                              fill_color=PINK,
                              fill_opacity=0.2,
                              stroke_width=5).shift(UP*0.3)

        s_label = Text("U", color=BLACK, font_size=50).next_to(rectangle, UR, buff=0.2).shift(LEFT*1+DOWN*1)

        #circles
        r = 2.4
        c1 = np.array([-1.3, 0, 0])
        c2 = np.array([1.3, 0, 0])

        circle_1 = Circle(radius=r, stroke_color=BLUE_E,
                          stroke_width=4).move_to(c1)

        circle_2 = Circle(radius=r, stroke_color=BLUE_E,
                          stroke_width=4).move_to(c2)

        #hatch
        hatch = VGroup()
        spacing = 0.5
        angle = PI/4.2

        direction = np.array([np.cos(angle), np.sin(angle), 0])
        normal = np.array([-direction[1], direction[0], 0])

        for t in np.arange(-12, 12, spacing):
            base = t * normal
            eps = 0.01

            #circle1
            diff1 = base - c1
            a = np.dot(direction, direction)
            b1 = 2 * np.dot(diff1, direction)
            c_1 = np.dot(diff1, diff1) - r**2
            disc1 = b1*b1 - 4*a*c_1

            #circle2
            diff2 = base - c2
            b2 = 2 * np.dot(diff2, direction)
            c_2 = np.dot(diff2, diff2) - r**2
            disc2 = b2*b2 - 4*a*c_2

            if disc1 >= 0 and disc2 >= 0:
                s1 = (-b1 - np.sqrt(disc1)) / (2*a)
                s2 = (-b1 + np.sqrt(disc1)) / (2*a)

                t1 = (-b2 - np.sqrt(disc2)) / (2*a)
                t2 = (-b2 + np.sqrt(disc2)) / (2*a)

                #intersection
                left = max(s1, t1)
                right = min(s2, t2)

                if left < right:
                    hatch.add(Line(
                        base + (left + eps)*direction,
                        base + (right - eps)*direction,
                        stroke_color=BLUE_E,
                        stroke_width=2.6))

        label1 = Text("A", color=BLACK, font_size=50).move_to(circle_1).shift(UP*3)

        label2 = Text("B", color=BLACK, font_size=50).move_to(circle_2).shift(UP*3)

        label3 = MathTex("a", color=BLACK).scale(2).move_to(ORIGIN)
        label4 = MathTex("e", color=BLACK).scale(2).move_to(ORIGIN).shift(LEFT*2.9+UP*0.7)
        label41 = MathTex("i", color=BLACK).scale(2).next_to(label4, buff=-1.1).shift(RIGHT*2)
        label42 = MathTex("o", color=BLACK).scale(2).next_to(label4, DOWN, buff=0.86)
        label43 = MathTex("u", color=BLACK).scale(2).next_to(label41, DOWN, buff=0.75)

        label5 = MathTex("b", color=BLACK).scale(2).move_to(ORIGIN).shift(RIGHT*2.2+UP*0.7)
        label51 = MathTex("c", color=BLACK).scale(2).move_to(ORIGIN).shift(RIGHT*2.2+DOWN*0.7)

        outline1 = circle_1.copy().set_fill(opacity=0)
        outline2 = circle_2.copy().set_fill(opacity=0)

        self.add(rectangle, hatch, outline1, outline2,
                 circle_1, circle_2, s_label, label1, label2,
                 label3,label4, label41, label42, label43, label5, label51)