from manim import *
import numpy as np

config.frame_height = 15
config.frame_width = 20
config.pixel_height = 1900
config.pixel_width = 2900
config.background_color = WHITE

BARNEYPURPLE = "#A00498"
DARKISHPURPLE = "#751973"
DARKMAGENTA = "#960056"

class RightTriangle(Scene):
    def construct(self):
        image= ImageMobject("step_1.png") 
        image.scale(0.13).shift(UP*4.9+RIGHT*6)

        image2= ImageMobject("step_1.png")
        image2.scale(0.13).shift(UP*1+RIGHT*6)

        triangle= Polygon(ORIGIN, 4*LEFT, 4*UP, color=BARNEYPURPLE).scale(2.3).shift(DOWN*1.7, RIGHT*1.5)
        right_angle= Square(side_length=0.9, color=BLACK).shift(DOWN*3.84, RIGHT*3.65)
        t_line= Line(start=[4.1,1,0], end=[4.08,-4.24,0], color=BLACK).add_tip(at_start=True).next_to(triangle, RIGHT*11.5).shift(DOWN*2.1)

        A=Dot(point=[4.08,-4.24,0], color=DARKMAGENTA).scale(2)
        P=Dot(point=[-5.05,-4.24,0], color=DARKMAGENTA).scale(2)
        C=Dot(point=[4.1,4.9,0], color=DARKMAGENTA).scale(2)
        B=Dot(point=[4.1,1,0], color=DARKMAGENTA).scale(2)
        K=Dot(point=[-5.2,1,0], color=WHITE).scale(2)

        PB= Line(start= [-5.05,-4.24,0], end= [4.13, 1, 0], color=DARKISHPURPLE) 
        LineB= DashedLine(start=B.get_center(), end=B.get_center() + LEFT*9, color=BLACK, dash_length=0.3, dashed_ratio=0.6)

        A_label= MathTex("A", font_size=60, color=BLACK).next_to(A, DOWN*0.6+ RIGHT*0.2)
        P_label= MathTex("P", font_size=60, color=BLACK).next_to(P, DOWN)
        C_label= MathTex("C", font_size=60, color=BLACK).next_to(C, RIGHT*0.75)
        B_label= MathTex("B", font_size=60, color=BLACK).next_to(B, RIGHT*0.75)
        PA_label= Tex("100 m", font_size=58, color=BLACK).next_to(triangle, DOWN)
        BA_label= Tex("100 m", font_size=58, color=BLACK).next_to(triangle, RIGHT).shift(DOWN*2)
        x_label= MathTex("x=?", font_size=65, color=BLACK).next_to(triangle).shift(UP*2.7)
        t_label= Tex("t=15s", font_size=58, color=BLACK).next_to(t_line, buff=0.1)

        BPA= Angle(Line(P.get_center(), B.get_center()), Line(P.get_center(), A.get_center()), radius=2, color=BLACK, other_angle=True)
        KBP= Angle(Line(B.get_center(), K.get_center()), Line(B.get_center(), P.get_center()), radius=2, color=BLACK, other_angle=False)
        tip=Line(start=[0,0.1,0], end=[0,0,0], color=BLACK).add_tip(tip_length=0.3, tip_width=0.3).shift(RIGHT*2.3).rotate(angle=PI/6)

        BPA_label= MathTex("45^\\circ", font_size=58, color=BLACK).next_to(BPA)
        KBP_label= MathTex("45^\\circ", font_size=58, color=BLACK).next_to(KBP,LEFT)

        car_label= Text("Car Parked Point", font_size=38, color=RED_E).next_to(P,DOWN*4)
        ground_label= Text("Ground Point", font_size=38, color=RED_E).next_to(A,DOWN*4)
        
        self.add(right_angle, triangle, PB, LineB, A, P, C, B, K, A_label, P_label, C_label, B_label, 
                 PA_label, x_label, BPA, image, image2, BA_label, KBP,
                 car_label, ground_label, tip, t_line, t_label, BPA_label, KBP_label)