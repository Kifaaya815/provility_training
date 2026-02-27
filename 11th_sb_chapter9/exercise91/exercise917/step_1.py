from manim import *

config.frame_height = 10
config.frame_width = 14
config.pixel_height = 3200
config.pixel_width = 3200
config.background_color = WHITE

AXISGREEN= "#1B7F3F"
LINEBLUE= "#2E2F75"

class Exercise917(Scene):
    def construct(self):

        axes = Axes(x_range=[-2.5, 5.5, 1],
                    y_range=[-1.9, 6, 1],
                    x_length=11.5,
                    y_length=8.5,
                    axis_config={"color": BLACK,
                                 "stroke_width": 4,
                                 "tip_length":0.3,
                                 "tip_width":0.2},
                    tips=True)
        
        axes.y_axis.shift(RIGHT*0.2+DOWN*0.2)
        
        axes.x_axis.add_tip(at_start=True, tip_length=0.35, tip_width=0.25)
        axes.y_axis.add_tip(at_start=True, tip_length=0.35, tip_width=0.25)

        axes.x_axis.ticks.set_stroke(width=4)
        axes.y_axis.ticks.set_stroke(width=4)

        axes.shift(DOWN*0.2)

        # 🔥 MANUAL X-AXIS LABELS
        x_labels = VGroup()
        for x in range(-2, 6):
            if x != 0:
                label = MathTex(str(x), font_size=28, color=BLACK)
                label.next_to(axes.coords_to_point(x, 0), DOWN, buff=0.1).shift(RIGHT*0.01)
                x_labels.add(label)

        # 🔥 MANUAL Y-AXIS LABELS
        y_labels = VGroup()
        for y in range(-1, 6):
            if y != 0:
                label = MathTex(str(y), font_size=28, color=BLACK)
                label.next_to(axes.coords_to_point(0, y), LEFT, buff=0.19).shift(UP*0.15)
                y_labels.add(label)

        origin_label = MathTex("0", font_size=30, color=BLACK)
        origin_label.next_to(axes.coords_to_point(0, 0),
                             DOWN*0.2).shift(LEFT*0.2)

        graph = axes.plot(lambda x: -x + 4,
                          x_range=[-1.7, 5.2],
                          color=YELLOW_E,
                          stroke_width=7).shift(RIGHT*0.1)
        
        end_point = graph.get_end()
        prev_point = graph.point_from_proportion(0.6)

        graph_tip = Arrow(prev_point,
                          end_point,
                          buff=0,
                          max_tip_length_to_length_ratio=0.6,
                          stroke_width=0,
                          tip_length=0.25,
                          color=YELLOW_E).shift(DOWN*0.1+RIGHT*0.14)

             
        start_point = graph.get_start()
        prev_point = graph.point_from_proportion(0.6)

        graph_tip1 = Arrow(prev_point,
                          start_point,
                          buff=0,
                          max_tip_length_to_length_ratio=0.6,
                          stroke_width=0,
                          tip_length=0.25,
                          color=YELLOW_E).shift(UP*0.1+LEFT*0.14)

        point = Dot(axes.coords_to_point(2.9, 1.2),
                    radius=0.1,
                    color=RED_E)
        
        circle = Circle(radius=0.19, color=BLACK, stroke_width=3).move_to(point)
        circle1 = Circle(radius=0.19, color=BLACK, stroke_width=3).move_to([2.35,-2.8,0])

        dash_line1=DashedLine(start=[0,0.99,0], end=[4,1,0], color=PURE_RED, dash_length=0.1).shift(DOWN*2.3+LEFT*2)
        dash_line2=DashedLine(start=[4.25,1,0], end=[4.25,0,0], color=PURE_RED, dash_length=0.1).shift(DOWN*2.3+LEFT*2)

        x_label = MathTex("x", font_size=50, color=BLACK)
        x_label.next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)

        y_label = MathTex("y", font_size=50, color=BLACK)
        y_label.next_to(axes.y_axis.get_end(), UP, buff=0.15)

        y_dash_label = MathTex("y", font_size=50, color=BLACK)
        y_dash_label.next_to(axes.y_axis.get_end(), UP, buff=0.15)

        arrow1 = Arrow(start=axes.coords_to_point(1.3, -0.5),
                      end=axes.coords_to_point(2.85, -0.5),
                      buff=0,
                      stroke_width=6,
                      color=BLUE,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25)
        
        arrow2 = Arrow(start=axes.coords_to_point(3.2, -0.5),
                      end=axes.coords_to_point(4.45, -0.5),
                      buff=0,
                      stroke_width=6,
                      color=BLUE,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25).rotate(PI/-1)
        
        arrow3 = Arrow(start=axes.coords_to_point(3.03, -0.6),
                      end=axes.coords_to_point(3.03, -1.7),
                      buff=0,
                      stroke_width=6,
                      color=BLUE,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25).rotate(PI/-1)

        plus3_label=MathTex(r"3^{+}", color=BLACK, font_size=40).next_to(arrow2, DOWN*0.2)
        minus3_label=MathTex(r"3^{-}", color=BLACK, font_size=40).next_to(arrow1, DOWN*0.2).shift(RIGHT*0.3)

        y_dash=MathTex("y'", color=BLACK).next_to(axes.y_axis, DOWN, buff=0.1)
        x_dash=MathTex("x'", color=BLACK).next_to(axes.x_axis, LEFT, buff=0.1)

        angle = np.arctan(-0.8)  

        formula=MathTex("f(x)=4-x", color=BLACK).next_to(graph).shift(LEFT*6.8+UP*0.8)
        formula.rotate(angle)

        self.add(dash_line1, dash_line2, axes, graph, point, x_label, y_label, 
                 x_labels, y_labels, origin_label, circle,
                 graph_tip, graph_tip1, circle1, arrow1, arrow2, arrow3,
                 plus3_label, minus3_label, y_dash, x_dash, formula)
