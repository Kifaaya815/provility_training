from manim import *
import numpy as np

config.frame_height=15
config.frame_width=18
config.pixel_width=2500
config.pixel_height=2500
config.background_color=WHITE

class TrigonometryGraph(Scene):
    def construct(self):

        def make_graph(func,color):
            axes= Axes(x_range=[-3.8, 3.8, PI/2],
                       y_range=[-6, 6, 6],
                       x_length=6,
                       y_length=4,
                       axis_config={"color":BLACK, "stroke_width":3},
                       tips=False)

            x_labels= axes.get_x_axis().add_labels({-PI: MathTex(r"-\pi"),
                                                     -PI/2: MathTex(r"-\frac{\pi}{2}"),
                                                     0: MathTex("0"),
                                                     PI/2: MathTex(r"\frac{\pi}{2}"),
                                                     PI: MathTex(r"\pi")}).set_color(BLACK)
            x_labels[2].shift(LEFT*0.25)  

            graph= axes.plot(func, x_range=[-PI, PI], color=color)

            grp= VGroup(axes, x_labels, graph)
            grp.scale(0.46)
            return grp

        g1= make_graph(lambda x: 3*np.sin(x), RED)
        g2= make_graph(lambda x: 3*np.cos(x), BLUE_D)

        g3= make_graph(lambda x: np.tan(x), GREEN)
        g3[2].become(g3[0].plot(lambda x: np.tan(x),x_range=[-PI/2 + 0.2, PI/2 - 0.2],color=GREEN))

        axes4 = Axes(x_range=[-3.8, 3.8, PI/2],
                     y_range=[-6, 6, 6],
                     x_length=6,
                     y_length=4,
                     axis_config={"color": BLACK, "stroke_width": 3},
                     tips=False)

        x_labels4 = axes4.get_x_axis().add_labels({-PI: MathTex(r"-\pi"),
                                                   -PI/2: MathTex(r"-\frac{\pi}{2}"),
                                                    0: MathTex("0"),
                                                    PI/2: MathTex(r"\frac{\pi}{2}"),
                                                    PI: MathTex(r"\pi")}).set_color(BLACK)
        x_labels4[2].shift(LEFT*0.25)  

        cosec_left= axes4.plot(lambda x: 1 / np.sin(x), x_range=[-PI + 0.2, -0.2],color=ORANGE)
        cosec_right= axes4.plot(lambda x: 1 / np.sin(x), x_range=[0.2, PI - 0.2],color=ORANGE)

        g4= VGroup(axes4, x_labels4, cosec_left, cosec_right)
        g4.scale(0.46)

        axes5 = Axes(x_range=[-3.8, 3.8, PI/2],
                     y_range=[-6, 6, 6],
                     x_length=6,
                     y_length=4,
                     axis_config={"color": BLACK, "stroke_width": 3},
                     tips=False)

        x_labels5 = axes5.get_x_axis().add_labels({-PI: MathTex(r"-\pi"),
                                                   -PI/2: MathTex(r"-\frac{\pi}{2}"),
                                                    0: MathTex("0"),
                                                    PI/2: MathTex(r"\frac{\pi}{2}"),
                                                    PI: MathTex(r"\pi")}).set_color(BLACK)
        x_labels5[2].shift(LEFT*0.25)  

        sec_left= axes5.plot(lambda x: 1 / np.cos(x),x_range=[-PI + 0.2, -PI/2 - 0.2],color=PURPLE)
        sec_middle= axes5.plot(lambda x: 1 / np.cos(x),x_range=[-PI/2 + 0.2, PI/2 - 0.2],color=PURPLE)
        sec_right= axes5.plot(lambda x: 1 / np.cos(x),x_range=[PI/2 + 0.2, PI - 0.2],color=PURPLE)

        g5= VGroup(axes5, x_labels5, sec_left, sec_middle, sec_right)
        g5.scale(0.46)

        axes6 = Axes(x_range=[-3.8, 3.8, PI/2],
                     y_range=[-6, 6, 6],
                     x_length=6,
                     y_length=4,
                     axis_config={"color": BLACK, "stroke_width": 3},
                     tips=False)

        x_labels6 = axes6.get_x_axis().add_labels({-PI: MathTex(r"-\pi"),
                                                   -PI/2: MathTex(r"-\frac{\pi}{2}"),
                                                    0: MathTex("0"),
                                                    PI/2: MathTex(r"\frac{\pi}{2}"),
                                                    PI: MathTex(r"\pi")}).set_color(BLACK)
        x_labels6[2].shift(LEFT*0.25)  

        cot_left= axes6.plot(lambda x: 1/np.tan(x),x_range=[-PI + 0.2, -0.2],color=PINK)
        cot_right= axes6.plot(lambda x: 1/np.tan(x),x_range=[0.2, PI - 0.2],color=PINK)

        g6= VGroup(axes6, x_labels6, cot_left, cot_right)
        g6.scale(0.46)

        g1.scale(1.8).shift(UP*6.5 + LEFT*6)
        g2.scale(1.8).next_to(g1, buff=1)
        g3.scale(1.8).next_to(g2, buff=1)
        g4.scale(1.8).shift(LEFT*6)
        g5.scale(1.8)
        g6.scale(1.8).next_to(g5, buff=1)

        sin_label= Text("sin x", color=RED_E).next_to(g1, DOWN)
        cos_label= Text("cos x", color=RED_E).next_to(g2, DOWN*1.7)
        tan_label= Text("tan x", color=RED_E).next_to(g3, DOWN*1.4)
        csc_label= Text("csc x", color=RED_E).next_to(g4, DOWN*1.7)
        sec_label= Text("sec x", color=RED_E).next_to(g5, DOWN*1.7)
        cot_label= Text("cot x", color=RED_E).next_to(g6, DOWN*1.4)

        self.add(g1, g2, g3, g4, g5, g6,
                 sin_label, cos_label, tan_label,
                 csc_label, sec_label, cot_label)