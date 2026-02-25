from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 14
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE


class Exercise1017(Scene):
    def construct(self):

        top_axes = Axes(x_range=[-2*np.pi - 1.7, 2*np.pi + 1.5, np.pi/2],  
                        y_range=[-1.7, 1.7, 1],
                        x_length=12,   
                        y_length=5.5,
                        axis_config={"color": BLACK, "tip_length": 0.35, "tip_width": 0.25, "stroke_width": 3},
                        x_axis_config={"include_ticks": True},
                        y_axis_config={"include_ticks": False},
                        tips=True)

        top_axes.to_edge(UP, buff=0.1).shift(UP*0.6)

        x_vals = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2,
                  0,
                  np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]

        x_tex = [r"-2\pi", r"-\frac{3\pi}{2}", r"-\pi", r"-\frac{\pi}{2}",
                 r"0",
                 r"\frac{\pi}{2}", r"\pi", r"\frac{3\pi}{2}", r"2\pi"]

        x_labels = VGroup()
        for val, tex in zip(x_vals, x_tex):
            label = MathTex(tex, color=BLACK).scale(0.7)
            label.next_to(top_axes.c2p(val, 0), DOWN, buff=0.15)

            if val == 0:
                label.shift(LEFT * 0.25) 

            x_labels.add(label)

        y_label_top = MathTex("y", color=BLACK).next_to(top_axes.y_axis.get_end(), UP)
        x_label_top = MathTex("x", color=BLACK).next_to(top_axes.x_axis.get_end(), RIGHT)

        cos_graph = top_axes.plot(lambda x: np.cos(x),
                                  x_range=[-5*np.pi/2, 3*np.pi/2],  
                                  color="#0A888A",
                                  stroke_width=5)

        title_top = MathTex(r"\; y=\cos x", color=BLACK).scale(0.8)
        title_top.next_to(top_axes, UP, buff=0.2).align_to(top_axes, LEFT)


        bottom_axes = Axes(x_range=[-2*np.pi - 1.5, 2*np.pi + 1.5, np.pi/2],  
                           y_range=[-2.5, 2.5, 1],
                           x_length=12,
                           y_length=5,
                           axis_config={"color": BLACK, "tip_length": 0.35, "tip_width": 0.25, "stroke_width": 3},
                           x_axis_config={"include_ticks": True},
                           y_axis_config={"include_ticks": False},
                           tips=True)

        bottom_axes.next_to(top_axes, DOWN, buff=1.7)

        x_labels_bottom = VGroup()
        for val, tex in zip(x_vals, x_tex):
            label = MathTex(tex, color=BLACK).scale(0.7)
            label.next_to(bottom_axes.c2p(val, 0), DOWN, buff=0.15)

            if val == 0:
                label.shift(LEFT * 0.25)
                
            x_labels_bottom.add(label)

        y_label_bottom = MathTex("y", color=BLACK).next_to(bottom_axes.y_axis.get_end(), UP)
        x_label_bottom = MathTex("x", color=BLACK).next_to(bottom_axes.x_axis.get_end(), RIGHT)

        abs_cos_graph = bottom_axes.plot(lambda x: np.abs(np.cos(x)),
                                         x_range=[-3*np.pi/2, 3*np.pi/2],  
                                         color="#0A888A",
                                         stroke_width=5)   

        title_bottom = MathTex(r"y=|\cos x|", color=BLACK).scale(0.8)
        title_bottom.next_to(bottom_axes, UP, buff=0.2).align_to(bottom_axes, LEFT)

        self.add(top_axes, cos_graph, x_labels, y_label_top, x_label_top, title_top,
                 bottom_axes, abs_cos_graph, x_labels_bottom, y_label_bottom, x_label_bottom, title_bottom)