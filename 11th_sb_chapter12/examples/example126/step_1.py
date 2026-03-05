from manim import *

config.frame_height = 9
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

BURNTORANGE = "#C04E01"

class Example126(Scene):
    def construct(self):

        outer_rect = Rectangle(width=8.5,
                               height=5.5,
                               stroke_color=BURNTORANGE,
                               stroke_width=3,
                               fill_color="#C3D6EE",
                               fill_opacity=0.9)
        outer_rect.shift(UP*0.2)

        label_S = Text("S", font_size=40, color=BLACK)
        label_S.next_to(outer_rect, UP, buff=0.25)

        setA = RoundedRectangle(width=3.5,
                                height=2.5,
                                corner_radius=0.4,
                                stroke_color=BURNTORANGE,
                                stroke_width=3,
                                fill_color="#CBEBF5",
                                fill_opacity=1)
        setA.shift(LEFT * 1.8 + UP * 0.8)

        label_A = Text("A", font_size=40, color=BLACK)
        label_A.next_to(setA, UP + LEFT, buff=0.1)

        text_A = MathTex(r"(1,6),\ (2,5),",
                         r"(3,4),\ (4,3),",
                         r"(5,2),\ (6,1)",
                         color=BLACK,
                         font_size=50)
        text_A.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        text_A.move_to(setA.get_center())

        setB = Polygon([-2,  0.8, 0],  
                       [ 1.3,  0.9, 0],   
                       [ 1.0, -0.7, 0],   
                       [-1.6, -0.8, 0],   
                       stroke_color=BURNTORANGE,
                       stroke_width=3,
                       fill_color="#FCD3C0",
                       fill_opacity=1)
        setB.rotate(0.4)
        setB.shift(RIGHT*2.55 + UP*1).scale(1.05)

        label_B = Text("B", font_size=40, color=BLACK)
        label_B.next_to(setB, UP, buff=0).shift(DOWN*0.6+LEFT*0.8)

        text_B = MathTex(r"(3,6),\ (4,5),",
                         r"(5,4),\ (6,3)",
                         color=BLACK,
                         font_size=50)
        text_B.arrange(DOWN, buff=0.2)
        text_B.move_to(setB.get_center()).rotate(PI / 7).shift(RIGHT*0.15)

        setC = Circle(radius=0.75,
                      stroke_color=BURNTORANGE,
                      stroke_width=3,
                      fill_color="#FFD1DF",
                      fill_opacity=0.9)
        setC.shift(RIGHT*2.4 + DOWN*1.3)

        label_C = Text("C", font_size=40, color=BLACK)
        label_C.next_to(setC, RIGHT, buff=0.28).shift(DOWN*0.35)

        text_C = MathTex("(6,6)", color=BLACK, font_size=50)
        text_C.move_to(setC.get_center())

        self.add(outer_rect, label_S,
                 setA, label_A, text_A,
                 setB, label_B, text_B,
                 setC, label_C, text_C)