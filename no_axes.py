from manim import *

config.frame_height=9
config.frame_width=11
config.pixel_height=2800
config.pixel_width=2800

config.background_color=WHITE

class NoAxes(Scene):
    def construct(self):
        line=Line(start=[-4.5,0,0],end=[4.5,0,0],color=BLACK)
        line2=Line(start=[0,-4.5,0],end=[0,4.5,0],color=BLACK)

        line.add_tip().add_tip(at_start=True)
        line2.add_tip().add_tip(at_start=True)

        tick_y1=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(line, UP, buff=0.41)
        tick_y2=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(tick_y1, UP, buff=0.7)
        tick_y3=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(tick_y2, UP, buff=0.7)
        tick_y4=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(tick_y3, UP, buff=0.7)
        tick_y5=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(tick_y4, UP, buff=0.7)

        tick_y6=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(line, DOWN, buff=0.41)
        tick_y7=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(tick_y6, DOWN, buff=0.7)
        tick_y8=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(tick_y7, DOWN, buff=0.7)
        tick_y9=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(tick_y8, DOWN, buff=0.7)
        tick_y10=Line(start=[-0.2,0,0],end=[0.2,0,0],color=BLACK).next_to(tick_y9, DOWN, buff=0.7)

        tick_x1=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(line2, LEFT, buff=0.41)
        tick_x2=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(tick_x1, LEFT, buff=0.7)
        tick_x3=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(tick_x2, LEFT, buff=0.7)
        tick_x4=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(tick_x3, LEFT, buff=0.7)
        tick_x5=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(tick_x4, LEFT, buff=0.7)

        tick_x6=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(line2, RIGHT, buff=0.41)
        tick_x7=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(tick_x6, RIGHT, buff=0.7)
        tick_x8=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(tick_x7, RIGHT, buff=0.7)
        tick_x9=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(tick_x8, RIGHT, buff=0.7)
        tick_x10=Line(start=[0,-0.2,0],end=[0,0.2,0],color=BLACK).next_to(tick_x9, RIGHT, buff=0.7)

        x_label=MathTex("X", color=BLACK).next_to(line)
        x1_label=MathTex("X'", color=BLACK).next_to(line, LEFT)
        y_label=MathTex("Y", color=BLACK).next_to(line2, UP)
        y1_label=MathTex("Y'", color=BLACK).next_to(line2, DOWN)


        self.add(line, line2, tick_y1, tick_y2, tick_y3, tick_y4, tick_y5, tick_y6, tick_y7, tick_y8, 
                 tick_y9, tick_y10, tick_x1, tick_x2, tick_x3, tick_x4, tick_x5, tick_x6, tick_x7, 
                 tick_x8, tick_x9, tick_x10, x_label, x1_label, y_label, y1_label)