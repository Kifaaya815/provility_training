from manim import *

config.frame_height = 9
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE


class Casestudy43(Scene):
    def construct(self):

        line_color = BLACK

        top = Ellipse(width=3.6,
                      height=1.1,
                      color=line_color,
                      fill_color="#A0CEBE",
                      fill_opacity=1)
        top.shift(UP*1.5)

        left_side = Line(top.get_left()+DOWN*0.01,
                         top.get_left()+DOWN*3,
                         color=line_color)

        right_side = Line(top.get_right()+DOWN*0.01,
                          top.get_right()+DOWN*3,
                          color=line_color)

        bottom_fill = Ellipse(width=3.6,
                              height=1.08,
                              fill_color="#06815A",
                              fill_opacity=1,
                              stroke_width=0)

        bottom_fill.move_to((left_side.get_end() + right_side.get_end()) / 2)

        bottom_arc = Arc(radius=1.8,
                         start_angle=PI,
                         angle=PI,
                         color=line_color)
        bottom_arc.scale([1, 0.305, 1])
        bottom_arc.move_to(bottom_fill.get_center()).shift(DOWN*0.25)

        body = Polygon(left_side.get_start(),
                       right_side.get_start(),
                       right_side.get_end(),
                       left_side.get_end(),
                       fill_color="#06815A",
                       fill_opacity=1,
                       stroke_width=0)

        center = top.get_center()
        r_line = Line(center, center + RIGHT*1.8, color=line_color)
        r_dot = Dot(center, color="#850E04")
        r_label = MathTex("r", color=line_color).next_to(r_line, UP*0.2)

        brace = BraceBetweenPoints(right_side.get_start(),
                                   right_side.get_end(),
                                   direction=RIGHT,
                                   color=line_color)
        h_label = MathTex("h", color=line_color).next_to(brace, RIGHT*0.5)

        arrow = Arrow(start=top.get_center() + UP*0.5,
                      end=top.get_center() + UP*1.2,
                      buff=0,
                      color=line_color,
                      stroke_width=10).rotate(PI/-2).shift(RIGHT*0.33+UP*0.01)

        line=Line(start=top.get_center() + UP*0.22,
                  end=top.get_center() + UP*0.85,
                  buff=0,
                  color=line_color,
                  stroke_width=4)

        open_text = Text("Open at top",
                         color=line_color,
                         font_size=25).next_to(arrow, RIGHT, buff=0.2)

        formula1 = MathTex(r"TSA = CSA + \text{Base Area}", color=line_color).scale(0.7)

        formula2 = MathTex(r"TSA = 2\pi rh + \pi r^2 = 75\pi", color=line_color).scale(0.7)

        formulas = VGroup(formula1, formula2).arrange(DOWN*0.5, aligned_edge=LEFT, buff=0.35).next_to(bottom_arc, DOWN, buff=0.3).shift(RIGHT*0.15)

        self.add(bottom_fill, body, top,
                 left_side, right_side, bottom_arc,
                 r_line, r_dot, r_label,
                 brace, h_label, formulas,
                 arrow, open_text, line)