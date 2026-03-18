from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 14
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE


class Exercise1015(Scene):
    def construct(self):

        axis_color = BLACK
        curve_color = "#D81B7D"

        axes = Axes(
            x_range=[-4.9, 14.9, 1],
            y_range=[-3.9, 4.9, 1],
            x_length=13,
            y_length=13 * ((4.9 - (-3.9)) / (14.9 - (-4.9))),
            axis_config={
                "color": axis_color,
                "stroke_width": 2,
                "include_numbers": True},
            tips=False)

        axes.get_x_axis().numbers.set_color(BLACK)
        axes.get_y_axis().numbers.set_color(BLACK)
        axes.get_y_axis().shift(RIGHT*0.2)

        axes.x_axis.add_tip()
        axes.x_axis.add_tip(at_start=True)
        axes.y_axis.add_tip()
        axes.y_axis.add_tip(at_start=True)

        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT*0.1)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP*0.1)
        x1_label = MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(), LEFT*0.1)
        y1_label = MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(), DOWN*0.1)

        self.add(axes, x_label, y_label, x1_label, y1_label)

        #v shape
        left_v = VMobject(color=curve_color, stroke_width=6)
        left_v.set_points_smoothly([
            axes.c2p(-2.5, 0.7),
            axes.c2p(-2.0, 0.1),
            axes.c2p(-1.2, -0.7),
            axes.c2p(-1, -1),
            axes.c2p(-0.9, -0.6),
            axes.c2p(-0.6, -0.15),
            axes.c2p(-0.2, 0.3)])

        #curve1
        curve1 = VMobject(color=curve_color, stroke_width=6)
        curve1.set_points_smoothly([
            axes.c2p(-0.2, 0.3),
            axes.c2p(0.5, 1.1),
            axes.c2p(1.6, 1.9),
            axes.c2p(2.8, 2.2),
            axes.c2p(3.6, 2.25),
            axes.c2p(3.7, 2.2)])

        closed_dot = Dot(axes.c2p(3.7, 2.245), color=GREEN, radius=0.07)

        open_circle = Circle(radius=0.1, color=BLACK, stroke_width=3)
        open_circle.move_to(axes.c2p(3.74, 0.5))

        #curve2
        curve2 = VMobject(color=curve_color, stroke_width=6)
        curve2.set_points_smoothly([
            axes.c2p(3.7, 0.5),
            axes.c2p(5.2, 0.7),
            axes.c2p(6.4, 1.4),
            axes.c2p(7.2, 2.5),
            axes.c2p(7.55, 3.53)])

        #curve3
        curve3 = VMobject(color=curve_color, stroke_width=6)
        curve3.set_points_smoothly([
            axes.c2p(7.54, 3.48),
            axes.c2p(8.8, 2.9),
            axes.c2p(9.7, 3.2),
            axes.c2p(10.1, 3.25),
            axes.c2p(10.36, 2.9)])

        #down curve
        drop_curve = VMobject(color=curve_color, stroke_width=6)
        drop_curve.set_points_smoothly([
            axes.c2p(10.35, 2.92),
            axes.c2p(10.5, 2.0),
            axes.c2p(10.4, 0.5),
            axes.c2p(10.62, -0.4)])

        #end
        tail = VMobject(color=curve_color, stroke_width=6)
        tail.set_points_smoothly([
            axes.c2p(10.59, -0.35),
            axes.c2p(11.1, -0.85),
            axes.c2p(12, -0.9),])

        line = DashedLine(
            start=UP * 2.7,
            end=DOWN * 2.7,
            color=BLUE,
            stroke_width=4,
            dash_length=0.2).shift(RIGHT * 1.87)

        line.add_tip(tip_length=0.25)
        line.add_tip(at_start=True, tip_length=0.25)

        line2_top = DashedLine(
            start=axes.c2p(-1, 4.5),
            end=axes.c2p(-1, 0.4),
            color=BLUE,
            stroke_width=4,
            dash_length=0.2).rotate(PI/1)

        line2_bottom = DashedLine(
            start=axes.c2p(-1, -1.1),
            end=axes.c2p(-1, -3.5),
            color=BLUE,
            stroke_width=4,
            dash_length=0.2).rotate(PI/1)

        line2_top.add_tip(tip_length=0.25)
        line2_bottom.add_tip(at_start=True, tip_length=0.25)

        line3 = Line(
            start=axes.c2p(10.4, 1.5),
            end=axes.c2p(10.4, -2.5),
            color=BLUE,
            stroke_width=7.5).shift(RIGHT*0.01)

        line3.add_tip(tip_length=0.25)
        line3.add_tip(at_start=True, tip_length=0.25)

        ellipse = Ellipse(
            width=4,
            height=1,
            fill_color=WHITE,
            fill_opacity=0,
            color=PURE_RED)
        ellipse.move_to(axes.c2p(3.8, 1))
        ellipse.rotate(PI / 2)

        label1=Text("Vertical Tangent", color=BLACK, font_size=26).next_to(line2_top, UP).shift(LEFT*1.3)
        label11=Text("at x=1", color=BLACK, font_size=27).next_to(label1, DOWN).shift(LEFT*0.7)

        arrow1=Arrow(start=(0.5,1,0), end=(-1,1,0), color=PURPLE).next_to(label11).shift(LEFT*0.1)

        label2=Text("Vertical Tangent", color=BLACK, font_size=26).next_to(line, UP).shift(RIGHT*1.3)
        label21=Text("at x=8", color=BLACK, font_size=27).next_to(label2, DOWN).shift(RIGHT*0.7)

        arrow2=Arrow(start=(-1,1,0), end=(0.5,1,0), color=PURPLE).next_to(label21).shift(LEFT*2.5)
       
        label3=Text("Vertical Tangent", color=BLACK, font_size=25).next_to(line3, UP).shift(RIGHT*1.4)
        label31=Text("at x=11", color=BLACK, font_size=25).next_to(label3, DOWN).shift(RIGHT*0.7)

        arrow3=Arrow(start=(-1,1,0), end=(0.5,1,0), color=PURPLE).next_to(label31).shift(LEFT*2.5)
        
        arrow4=Arrow(start=(-1.1,1,0), end=(0.1,2.8,0), color=PURPLE).next_to(label31).shift(LEFT*7.3+UP*0.6)
        arrow4_label=Tex("Discontinuous", color=BLACK, font_size=30).next_to(arrow4).shift(UP*0.95+LEFT*0.65)

        self.add(left_v, curve1, closed_dot, curve2, curve3, drop_curve, tail,
                 line, line2_top, line2_bottom, line3,
                 ellipse, label1, label11, arrow1, label2, label21, arrow2,
                 label3, label31, arrow3, arrow4, arrow4_label,open_circle)