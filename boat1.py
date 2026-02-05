from manim import *
import numpy as np

config.frame_height = 15
config.frame_width = 20
config.pixel_height = 1900
config.pixel_width = 2900
config.background_color = WHITE

LINE_ORANGE = "#BD6C48"
DOT_BLUE = "#0343DF"

class BoatDiagram(Scene):
    def construct(self):
        image= ImageMobject("boat1.png") 
        image.scale(0.5).shift(RIGHT*8, UP*3)
        self.add(image)

        P= Dot(np.array([-6, -3, 0]), color=DOT_BLUE, stroke_width=5)
        A= Dot(np.array([3, -3, 0]), color=DOT_BLUE, stroke_width=5)
        B= Dot(np.array([6, 3, 0]), color=DOT_BLUE, stroke_width=5)

        P_label= MathTex("P", font_size=36, color=BLACK).next_to(P, DOWN)
        A_label= MathTex("A", font_size=36, color=BLACK).next_to(A, DOWN)
        B_label= MathTex("B", font_size=36, color=BLACK).next_to(B, UP)
        port= Tex("Port", font_size=38, color=BLACK).next_to(P, LEFT*2.3).shift(DOWN*0.5)

        PA= Line(P, A, color=LINE_ORANGE)
        AB= Line(A, B, color=LINE_ORANGE)
        PB= DashedVMobject(Line(P.get_center(),B.get_center(), color=LINE_ORANGE), num_dashes=80)

        PA_length= Tex("10 km", font_size=34, color=BLACK).next_to(PA, DOWN)
        AB_length= Tex("8 km", font_size=34, color=BLACK).rotate(PI / 2.8).next_to(AB, LEFT).shift(RIGHT*1.5)

        angle60= DashedLine(A.get_center(),A.get_center() + RIGHT*2,color=GREY)
        angle= Angle(angle60, AB, radius=0.8, color=DOT_BLUE)
        angle_label= MathTex("60^\\circ", font_size=34, color=BLACK).next_to(angle, RIGHT)

        self.add(P_label, A_label, B_label,
                 port,
                 PA, AB, PB,
                 PA_length, AB_length,
                 angle60, angle, angle_label, 
                 P, B, A)