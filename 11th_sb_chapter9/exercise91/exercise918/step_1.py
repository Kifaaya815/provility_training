from manim import *
import numpy as np

config.frame_height = 12
config.frame_width = 16
config.pixel_width = 2400
config.pixel_height = 1600
config.background_color = WHITE

class Exercise918(Scene):
    def construct(self):

        axes = Axes(x_range=[-4.7, 6, 1],     
                    y_range=[-2.7, 10.4, 1],
                    x_length=10,
                    y_length=8,
                    axis_config={"color": BLACK,
                                 "stroke_width": 3,
                                 "tip_length": 0.35,
                                 "tip_width": 0.25},
            x_axis_config={"include_numbers": True,
                           "numbers_to_include": np.arange(-4, 6, 1),
                           "font_size": 28},
            y_axis_config={"include_numbers": True,
                           "numbers_to_include": np.arange(-2, 10, 1),
                           "font_size": 28})

        
        axes.get_x_axis().numbers.set_color(BLACK)
        axes.get_y_axis().numbers.set_color(BLACK)

        triangle = Polygon([-1.5, 0.42, 0], 
                           [-1.5, -0.42, 0], 
                           [0, 0, 0],
                           color=BLACK, 
                           fill_color=BLACK, 
                           fill_opacity=1,
                           stroke_width=0).scale(0.3).rotate(PI)
        
        triangle.next_to(axes, LEFT).shift(DOWN*2.35 + RIGHT*0.4)

        triangle2 = Polygon([-1.5, 0.42, 0], 
                            [-1.5, -0.42, 0], 
                            [0, 0, 0],
                            color=BLACK, 
                            fill_color=BLACK, 
                            fill_opacity=1,
                            stroke_width=0).scale(0.3).rotate(-PI/2)

        triangle2.next_to(axes.y_axis, DOWN*0.2).shift(RIGHT*0.22 + UP*0.1)

        self.add(triangle, triangle2)

        graph = axes.plot(lambda x: x**2 + 2,
                          x_range=[-3, 3],
                          color="#FE46A5",
                          stroke_width=5.5)

        end_point = graph.get_end()
        prev_point = graph.point_from_proportion(0.9)

        graph_tip = Arrow(prev_point,
                          end_point,
                          buff=0,
                          max_tip_length_to_length_ratio=0.6,
                          stroke_width=0,
                          tip_length=0.25,
                          color="#FE46A5").shift(UP*0.03+RIGHT*0.01)

        start_point = graph.get_start()
        prev_point = graph.point_from_proportion(0.2)

        graph_tip1 = Arrow(prev_point,
                          start_point,
                          buff=0,
                          max_tip_length_to_length_ratio=0.6,
                          stroke_width=0,
                          tip_length=0.25,
                          color="#FE46A5").shift(UP*0.03+LEFT*0.01)

        point = Dot(axes.coords_to_point(1, 3),
                    color="#0343DF",
                    radius=0.09)

        dash_horizontal = DashedLine(axes.coords_to_point(0, 3),
                                     axes.coords_to_point(1, 3),
                                     dash_length=0.1,
                                     color=BLUE_D)

        dash_vertical = DashedLine(axes.coords_to_point(1, 0),
                                   axes.coords_to_point(1, 3),
                                   dash_length=0.1,
                                   color=BLUE_D)

        formula = MathTex("f(x)=x^2+2", color=BLACK)
        formula.move_to(axes.coords_to_point(4, 7))

        origin_label = MathTex("0", color=BLACK, font_size=28)
        origin_label.next_to(axes.coords_to_point(0, 0), DOWN + LEFT, buff=0.15)

        x_label=MathTex("x", color=BLACK).next_to(axes.x_axis).shift(UP*0.15)
        x1_label=MathTex("x'", color=BLACK).next_to(axes.x_axis, LEFT, buff=0.55).shift(UP*0.19)

        circle = Circle(radius=0.19, color=BLACK, stroke_width=3).move_to([0.32,-2.7,0])

        arrow1 = Arrow(start=axes.coords_to_point(-3, -1.09),
                      end=axes.coords_to_point(0.8, -1.09),
                      buff=0,
                      stroke_width=6,
                      color=YELLOW_E,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25)
        
        arrow2 = Arrow(start=axes.coords_to_point(1.2, -1.09),
                      end=axes.coords_to_point(5, -1.09),
                      buff=0,
                      stroke_width=6,
                      color=YELLOW_E,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25).rotate(PI/-1)
        
        arrow3 = Arrow(start=axes.coords_to_point(1, -1.2),
                      end=axes.coords_to_point(1, -3.5),
                      buff=0,
                      stroke_width=6,
                      color=YELLOW_E,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25).rotate(PI/-1)
        
        plus1_label=MathTex(r"1^{+}", color=BLACK, font_size=40).next_to(arrow2, DOWN*0.2)
        minus1_label=MathTex(r"1^{-}", color=BLACK, font_size=40).next_to(arrow1, DOWN*0.3)

        self.add(dash_horizontal, dash_vertical,
                 axes, graph, point, formula,
                 origin_label, x_label, x1_label,
                 graph_tip, graph_tip1, circle,
                 arrow1, arrow2, arrow3,
                 plus1_label, minus1_label)