from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 15
config.pixel_height = 2500
config.pixel_width = 2500
config.background_color = WHITE

GREEN = "#1B5E20"
BLUE = "#1E40AF"
RED = "#E53935"

class Exercise9115(Scene):
    def construct(self):

        axes = Axes(x_range=[-np.pi+0.5, 2*np.pi],
                    y_range=[-3.99, 4],
                    x_length=13,
                    y_length=8,
                    axis_config={
                        "color": BLACK,
                        "stroke_width": 3.5,
                        "include_ticks": True,
                        "tip_length": 0.35,
                        "tip_width": 0.25},
                    tips=True)

        axes.x_axis.add_tip(at_start= True, tip_length=0.37, tip_width=0.27)
        axes.y_axis.add_tip(at_start= True, tip_length=0.37, tip_width=0.27)

        axes.x_axis.ticks.set_opacity(0)

        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y").next_to(axes.y_axis.get_end(), UP)

        tick_positions = [-np.pi/2, np.pi/2, np.pi, 3*np.pi/2]
        custom_ticks = VGroup()

        for x in tick_positions:
            tick = Line(axes.c2p(x, 0.15),
                        axes.c2p(x, -0.15),
                        color=BLACK,
                        stroke_width=3)
            custom_ticks.add(tick)

        tan_left = axes.plot(lambda x: np.tan(x),
                             x_range=[-2*np.pi/3, -np.pi/2 - 0.25],
                             color="#448EE4",
                             stroke_width=8)

        tan_first = axes.plot(lambda x: np.tan(x),
                              x_range=[-np.pi/2 + 0.25, np.pi/2 - 0.25],
                              color="#448EE4",
                              stroke_width=8)

        end_x = -np.pi/2 + 0.25
        dx = PI/2  

        end_point = axes.c2p(end_x, np.tan(end_x))
        prev_point = axes.c2p(end_x - dx, np.tan(end_x - dx))

        direction = end_point - prev_point

        tip = Triangle(fill_color="#448EE4",
                       fill_opacity=1,
                       stroke_width=0).scale(0.18)

        tip.rotate(angle_of_vector(direction))
        tip.move_to(end_point).shift(RIGHT*0.02)

        tan_second = axes.plot(lambda x: np.tan(x),
                               x_range=[np.pi/2 + 0.25, 3*np.pi/2 - 0.25],
                               color="#448EE4",
                               stroke_width=8)

        tan_right = axes.plot(lambda x: np.tan(x),
                              x_range=[3*np.pi/2 + 0.25, 11*np.pi/6],
                              color="#448EE4",
                              stroke_width=8)

        tan_curves = VGroup(tan_left, tan_first, tan_second, tan_right)

        asymptotes = VGroup()
        gap = 0.7  
        for x in [-np.pi/2, np.pi/2, 3*np.pi/2]:

            asymptotes.add( DashedLine( axes.c2p(x, gap),
                                        axes.c2p(x, 4),
                                        color=RED,
                                        dash_length=0.25,
                                        stroke_width=7))

            asymptotes.add( DashedLine( axes.c2p(x, -4),
                                        axes.c2p(x, -gap),
                                        color=RED,
                                        dash_length=0.25,
                                        stroke_width=7))

        labels = VGroup( MathTex("-\\pi/2", color=BLACK).next_to(axes.c2p(-np.pi/2, 0), DOWN),
                         MathTex("\\pi/2", color=BLACK).next_to(axes.c2p(np.pi/2, 0), DOWN),
                         MathTex("\\pi", color=BLACK).next_to(axes.c2p(np.pi, 0), DOWN*1.5),
                         MathTex("3\\pi/2", color=BLACK).next_to(axes.c2p(3*np.pi/2, 0), DOWN))

        axes_label_x=MathTex("x", color=BLACK, font_size=60).next_to(axes.x_axis)
        axes_label_y=MathTex("y", color=BLACK, font_size=60).next_to(axes.y_axis, UP)
        axes_label_x1=MathTex("x'", color=BLACK, font_size=60).next_to(axes.x_axis, LEFT)
        axes_label_y1=MathTex("y'", color=BLACK, font_size=60).next_to(axes.y_axis, DOWN)

        dot1=Dot((1,1,0), color=YELLOW_E, radius=0.1).shift(UP*2.95+LEFT*1.73)
        dot2=Dot((1,1,0), color=YELLOW_E, radius=0.1).shift(DOWN*5+LEFT*1)
        circle = Ellipse(width=1.2, height=0.6, color=BLACK, stroke_width=3).next_to(dot1).shift(DOWN*4.44+LEFT*0.54)

        arrow1 = Arrow(start=axes.coords_to_point(-0.5, -0.7),
                      end=axes.coords_to_point(1.15, -0.7),
                      buff=0,
                      stroke_width=6,
                      color="#FE46A5",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25)
        
        arrow2 = Arrow(start=axes.coords_to_point(2.05, -0.7),
                      end=axes.coords_to_point(3.9, -0.7),
                      buff=0,
                      stroke_width=6,
                      color="#FE46A5",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25).rotate(PI/-1)
        
        arrow3 = Arrow(start=axes.coords_to_point(2.08, -4.4),
                      end=axes.coords_to_point(2.08, -3),
                      buff=0,
                      stroke_width=6,
                      color="#FE46A5",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25).rotate(PI/-1)
        
        arrow4 = Arrow(start=axes.coords_to_point(1.05, 4.3),
                      end=axes.coords_to_point(1.05, 2.85),
                      buff=0,
                      stroke_width=6,
                      color="#FE46A5",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25).rotate(PI/-1)
        
        arrow1_label=MathTex("\\pi/2^{+}", color=BLACK, font_size=40).next_to(arrow2, DOWN*0.2).shift(RIGHT*0)
        arrow2_label=MathTex("\\pi/2^{-}", color=BLACK, font_size=40).next_to(arrow1, DOWN*0.3).shift(RIGHT*0.2)
        text_label1=Text("Large positive value", color=BLACK, font_size=34).next_to(arrow4, UP*0.25).shift(RIGHT*1.8)
        text_label2=Text("Large negative value", color=BLACK, font_size=34).next_to(arrow3, DOWN*0.25).shift(RIGHT*1.8)

        angle = np.arctan(1.1)  
        formula=MathTex("f(x)=", color=BLACK, font_size=30).move_to(tan_curves)
        formula.rotate(angle).shift(LEFT*1.97+UP*1)

        angle2 = np.arctan(2.5)
        formula1=MathTex("tan\\ x", color=BLACK, font_size=35).move_to(tan_curves)
        formula1.rotate(angle2).shift(UP*1.9+LEFT*1.45)

        origin_label = MathTex("0", color=BLACK, font_size=35)
        origin_label.next_to(axes.coords_to_point(0, 0), DOWN + RIGHT, buff=0.2)

        self.add(axes, x_label, y_label)
        self.add(custom_ticks)
        self.add(asymptotes)
        self.add(tan_curves, tip)
        self.add(labels, axes_label_x, axes_label_y,
                 axes_label_x1, axes_label_y1, dot1, dot2,
                 circle, arrow1, arrow2, arrow1_label, arrow2_label,
                 arrow3, arrow4, text_label1, text_label2, formula,
                 formula1, origin_label)