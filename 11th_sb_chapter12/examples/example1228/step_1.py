from manim import *

config.frame_height = 9
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

class Example1228(Scene):
    def construct(self):
        rect_color = BLACK
        a_line_color = BLACK
        inner_line_color = PURE_RED 
        
        color_a1_b = "#F9C7C7"
        color_a2_b = "#FFF9C4"
        color_a3_b = "#E8F5E9"
        color_background = "#FFFDE7"

        rect = Rectangle(width=7, height=4.5, color=rect_color, stroke_width=4)
        rect.set_fill(color_background, opacity=1)
        s_label = MathTex("S", color=BLACK).next_to(rect, UL, buff=0.1).shift(RIGHT*0.4+UP*0.04)

        p_left = rect.get_left() + DOWN * 1.6
        p_center = rect.get_center() + DOWN * -0.07
        p_top_right = rect.get_corner(UR) + LEFT * 0.7
        p_bottom_right = rect.get_corner(DR)

        h_stretch_1, v_lift_1 = 4.9, 3.4
        h_stretch_2, v_lift_2 = 3, 4

        ctrl_1 = p_left + RIGHT * h_stretch_1 + UP * v_lift_1
        ctrl_2 = p_top_right + LEFT * h_stretch_2 + DOWN * v_lift_2

        line_1_2 = CubicBezier(p_left, ctrl_1, ctrl_2, p_top_right,
                               color=a_line_color, stroke_width=4)

        line_3 = Line(p_center, p_bottom_right, color=a_line_color, stroke_width=4)

        a1_label = MathTex("A_1", color=BLACK, font_size=50).move_to(rect.get_center() + UP * 1.7 + LEFT * 0.9)
        a2_label = MathTex("A_2", color=BLACK, font_size=50).move_to(rect.get_center() + RIGHT * 2.7 + DOWN * 0.7)
        a3_label = MathTex("A_3", color=BLACK, font_size=50).move_to(rect.get_center() + DOWN * 1.5 + RIGHT * 1.2)

        b_oval = Ellipse(width=5.8, height=2.8, color=PURE_RED, stroke_width=5)
        b_oval.rotate(20 * DEGREES).move_to(rect.get_center())

        inner_line_1_2 = line_1_2.copy().pointwise_become_partial(line_1_2, 0.058, 0.9285)
        inner_line_1_2.set_color(inner_line_color).set_stroke(width=5)
        inner_line_3 = Intersection(line_3.copy(), b_oval).set_color(inner_line_color).set_stroke(width=4)
        red_line=Line([1,1,0],[1,2,0],color=PURE_RED, stroke_width=5).rotate(56.5*DEGREES).scale(1.74).shift(LEFT*0.29+DOWN*1.9)
        
        region_a1 = Polygon([-4,1.6,0], [-1.5,1.8,0], [1.0,1.8,0], [2.5,1.4,0], [2.2,0.4,0], [1.1,0.25,0], [0.3,0.1,0], [-1.2,-0.5,0], [-2.8,-1.9,0], [-3.8,0.1,0])
        region_a2 = Polygon([1.3,0.45,0], [2.3,1.55,0], [3,2.5,0], [4,4,0], [4,-2,0], [3.6,-1,0], [1.6,-1,0], [0.2,0,0], [0.48,-0.15,0])
        region_a3 = Polygon([-3.5,-1.6,0], [-2.2,-0.75,0], [-1.0,-0.16,0], [-0.05,0.07,0], [0.6,-0.3,0], [1.6,-0.9,0], [3,-5,0], [4,-4,0], [-4,-3,0])

        a1_b_fill = Intersection(region_a1, b_oval).set_fill(color_a1_b,1).set_stroke(width=0)
        a2_b_fill = Intersection(region_a2, b_oval).set_fill(color_a2_b,1).set_stroke(width=0)
        a3_b_fill = Intersection(region_a3, b_oval).set_fill(color_a3_b,1).set_stroke(width=0)

        t_a1_b = MathTex("A_1 \\cap B", color=BLACK, font_size=50).move_to(b_oval.get_center() + UP * 0.65 + LEFT * 0.3).rotate(20*DEGREES)
        t_a2_b = MathTex("A_2 \\cap B", color=BLACK, font_size=50).move_to(b_oval.get_center() + RIGHT * 1.65 + UP * 0.1).rotate(27*DEGREES)
        t_a3_b = MathTex("A_3 \\cap B", color=BLACK, font_size=50).move_to(b_oval.get_center() + DOWN * 0.85 + LEFT * 0.5).rotate(20*DEGREES)

        ptr_start = b_oval.get_bottom() + LEFT * 0.3
        ptr_end   = ptr_start + DOWN * 1.1 + RIGHT * 0.1
        p_ctrl_1, p_ctrl_2 = ptr_start + DOWN * 0.1, ptr_end + LEFT * 1.5
        
        b_pointer_curve = CubicBezier(ptr_start, p_ctrl_1, p_ctrl_2, ptr_end, color=PURE_RED, stroke_width=3).shift(UP*0.1)
        b_tip = Triangle(color=PURE_RED, fill_opacity=1).scale(0.12).shift(UP*0.2).rotate(-90 * DEGREES).move_to(ptr_end).shift(UP*0.1)
        b_ext_label = MathTex("B", color=BLACK, font_size=50).next_to(ptr_end, RIGHT, buff=0.2).shift(UP*0.1)

        rec=Rectangle(height=0.5, width=0.7, color="#FFF9C4", fill_color="#FFF9C4", fill_opacity=1).shift(RIGHT*0.5)
        rec2=Rectangle(height=0.1, width=0.7, color="#FFF9C4", fill_color="#FFF9C4", fill_opacity=1).shift(RIGHT*0.5)
        cir=Ellipse(height=0.4, width=1, color="#F9C7C7", fill_color="#F9C7C7", fill_opacity=1).shift(UP*0.37+RIGHT*0.7).rotate(17*DEGREES)
        rec1=Rectangle(height=0.5, width=0.7, color="#FFF9C4", fill_color="#FFF9C4", fill_opacity=1).shift(RIGHT*0.5)
        line=Line([2,2,0], color="#FFF9C4").shift(DOWN*0.35).rotate(-17*DEGREES).scale(0.7)
        line1=Line([2,2,0], color="#FFF9C4").shift(DOWN*0.7+LEFT*0.4).rotate(-22*DEGREES).scale(0.2)
        line2=Line([2,2,0], color="#FFF9C4").shift(DOWN*0.75+LEFT*0.5).rotate(-33*DEGREES).scale(0.2)
        line3=Line([2,2,0], color="#FFF9C4").rotate(-33*DEGREES).scale(0.2).next_to(line2, DOWN, buff=-0.18)
        line4=Line([2,2,0], color="#FFF9C4").rotate(-95*DEGREES).scale(0.2).shift(LEFT*1.25+DOWN*1.05)

        self.add(rect, s_label)
        self.add(rec,rec1, a1_b_fill,rec2, a3_b_fill, a2_b_fill, cir, line, line1, line2, line3, line4)
        self.add(a1_label, a2_label, a3_label)
        
        self.add(line_1_2, line_3) 
        self.add(inner_line_1_2, inner_line_3)
        
        self.add(t_a1_b, t_a2_b, t_a3_b)
        self.add(b_pointer_curve, b_tip, b_ext_label)
        self.add(red_line)
        self.add(b_oval)