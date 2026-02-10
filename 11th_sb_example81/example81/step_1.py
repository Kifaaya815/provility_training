from manim import *
import numpy as np

config.frame_height= 8
config.frame_width= 10
config.pixel_height= 2800
config.pixel_width= 2800
config.background_color= WHITE

P_PURP="#6D597A"

class Example81(Scene):
    def construct(self):
        axes= Axes(x_range=[-3, 3],
                   y_range=[-3,3],
                   x_length=7,
                   y_length=6,
                   axis_config={"color":P_PURP,
                                "include_tip":True,
                                "include_ticks":False,
                                "stroke_width":9,
                                "tip_shape": StealthTip})
        
        axes.x_axis.tip.scale(1.5)
        axes.y_axis.tip.scale(1.5)
        
        axes.x_axis.add_tip(at_start=True, tip_shape=StealthTip, tip_length=0.62, tip_width=0.62)
        axes.y_axis.add_tip(at_start=True, tip_shape=StealthTip, tip_length=0.62, tip_width=0.62)
    
        axes.move_to(ORIGIN) 

        P = Line(start=axes.c2p(0, 0),
                 end=axes.c2p(-2.5, 1.55),
                 color=BLUE_D,
                 stroke_width=8)
        
        P.add_tip(tip_shape=StealthTip, tip_length=0.62, tip_width=0.62)
        P_label = Text("P", color=BLACK, font_size=36)
        P_label.next_to(P.get_end(), UL, buff=0.15)
 
        angle_arc = CurvedArrow(start_point=axes.c2p(0, 0) + UP*0.95,
                                end_point=axes.c2p(0, 0) + LEFT*0.85 + UP*0.5,
                                radius=1, color=BLACK, stroke_width=4, tip_length=0.2)
        
        angle_label= MathTex("60^{\\circ}", font_size=40, color=BLACK)
        angle_label.next_to(angle_arc, UP, buff=0.2)

        distance_label = Text("30 km", color=BLACK, font_size=30)
        distance_label.next_to(P_label.get_center(), DOWN, buff=0.99).shift(RIGHT*0.8)

        N = Text("N", color=BLACK, font_size=36).next_to(axes.y_axis.get_end(), UP, buff=0.2)
        S = Text("S", color=BLACK, font_size=36).next_to(axes.y_axis.get_start(), DOWN, buff=0.2)
        E = Text("E", color=BLACK, font_size=36).next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        W = Text("W", color=BLACK, font_size=36).next_to(axes.x_axis.get_start(), LEFT, buff=0.2)

        self.add(axes,P,
                 N,E,W,S,P_label,
                 angle_arc, angle_label, distance_label)