from manim import *

config.frame_height = 9
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE


class Exercise1238(Scene):
    def construct(self):

        text_color = BLACK
        line_color = "#9D5783"

        outer_box = Rectangle(width=5, height=4, color="#9D5783", fill_color="#9D5783", fill_opacity=0.2)

        bag1_title = Tex("Bag I", color=text_color, font_size=60).scale(0.7)
        bag2_title = Tex("Bag II", color=text_color, font_size=60).scale(0.7)

        bag1_title.move_to(outer_box.get_top() + DOWN*0.5 + LEFT*1)
        bag2_title.move_to(outer_box.get_top() + DOWN*0.5 + RIGHT*1)

        oval1 = Ellipse(width=1.2, height=2, color=BLUE_D, fill_color=BLUE_D, fill_opacity=0.2)
        oval2 = Ellipse(width=1.2, height=2, color=GREEN_D, fill_color=GREEN, fill_opacity=0.2)

        oval1.move_to(outer_box.get_center() + LEFT*1)
        oval2.move_to(outer_box.get_center() + RIGHT*1)

        bag1_text = MathTex("5A\\\\3B", color=text_color).scale(0.7)
        bag2_text = MathTex("4A\\\\1B", color=text_color).scale(0.7)

        bag1_text.move_to(oval1.get_center())
        bag2_text.move_to(oval2.get_center())

        label1 = Tex("Total 8 balls", color=text_color).scale(0.5)
        label2 = Tex("Total 10 balls", color=text_color).scale(0.5)

        label1.next_to(oval1, DOWN, buff=0.6).shift(LEFT*0.6)
        label2.next_to(oval2, DOWN, buff=0.6).shift(RIGHT*0.6)

        branch_line = Line(
            LEFT*2.5 + DOWN*2.8,
            RIGHT*2.5 + DOWN*2.8,
            color=line_color)

        line1 = Line(oval1.get_bottom(), branch_line.get_center(), color=line_color)
        line2 = Line(oval2.get_bottom(), branch_line.get_center(), color=line_color)

        box1 = Rectangle(width=2.5, height=1, color=line_color, fill_color="#9D5783", fill_opacity=0.2)
        box2 = Rectangle(width=2.5, height=1, color=line_color, fill_color="#9D5783", fill_opacity=0.2)
        box3 = Rectangle(width=2.5, height=1, color=line_color, fill_color="#9D5783", fill_opacity=0.2)

        box1.shift(DOWN*4 + LEFT*3)
        box2.shift(DOWN*4)
        box3.shift(DOWN*4 + RIGHT*3)

        text1 = Tex("One white \\\\ and one black", color=text_color, font_size=60).scale(0.5)
        text2 = Tex("Both are white", color=text_color, font_size=60).scale(0.5)
        text3 = Tex("Both are black", color=text_color, font_size=60).scale(0.5)

        text1.move_to(box1.get_center())
        text2.move_to(box2.get_center())
        text3.move_to(box3.get_center())

        arrow1 = Arrow(branch_line.get_left(), box1.get_top(), buff=0, color=line_color)
        arrow2 = Arrow(branch_line.get_center(), box2.get_top(), buff=0, color=line_color)
        arrow3 = Arrow(branch_line.get_right(), box3.get_top(), buff=0, color=line_color)

        self.add(branch_line, line1, line2, outer_box,
                 bag1_title, bag2_title, oval1, oval2,
                 bag1_text, bag2_text, label1, label2,
                 box1, box2, box3, text1, text2, text3,
                 arrow1, arrow2, arrow3)