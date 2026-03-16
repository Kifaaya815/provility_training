from manim import *

config.frame_height = 9
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE


class Example1210(Scene):
    def construct(self):

        line_color = "#2E5E9E"
        text_color = BLACK

        # Rectangles
        rect1 = Rectangle(width=3.5, height=3.7, stroke_color=line_color, stroke_width=6)
        rect2 = Rectangle(width=2.4, height=1.9, stroke_color=line_color, stroke_width=6)
        rect3 = Rectangle(width=2.8, height=2.6, stroke_color=line_color, stroke_width=6)

        # Position rectangles
        rect1.move_to(UP*0.5)
        rect3.next_to(rect1, RIGHT, buff=0)
        rect2.next_to(rect1, LEFT, buff=0)

        # Align bottoms
        rect2.align_to(rect1, DOWN)
        rect3.align_to(rect1, DOWN)

        # Labels
        label1 = Text("1", color=text_color).scale(1.1)
        label2 = Text("2", color=text_color).scale(1.1)
        label3 = Text("3", color=text_color).scale(1)

        label1.next_to(rect1, UP, buff=0.2)
        label2.next_to(rect3, UP, buff=0.2)
        label3.next_to(rect2, UP, buff=0.2)

        Smallest=Text("Smallest", color=BLACK, font_size=35).move_to(rect2)
        Largest=Text("Largest", color=BLACK, font_size=40).move_to(rect1)
        Medium=Text("Medium", color=BLACK, font_size=35).move_to(rect3)

        arrow1 = Arrow(start=(1.1,1.5,0), end=(1.1,0,0), color=PURE_RED).next_to(rect2, DOWN, buff=-0.3)
        arrow2 = Arrow(start=(1.1,1.5,0), end=(1.1,0,0), color=PURE_RED).next_to(rect1, DOWN, buff=-0.3)
        arrow3 = Arrow(start=(1.1,1.5,0), end=(1.1,0,0), color=PURE_RED).next_to(rect3, DOWN, buff=-0.3)

        text1 =Tex("Fixed Red Colour", color=BLACK, font_size=28).next_to(arrow1, DOWN, buff=0.13)
        text2 =Tex("Remaining 5 Colours", color=BLACK, font_size=28).next_to(arrow2, DOWN, buff=0.1)
        text3 =Tex("Remaining 4 Colours", color=BLACK, font_size=28).next_to(arrow3, DOWN, buff=0.1)

        line1=Line(start=(1.1,1.5,0), end=(3.5,1.5,0), color=BLACK).next_to(text1, DOWN, buff=0.22)
        line2=Line(start=(1.1,1.5,0), end=(3.65,1.5,0), color=BLACK).next_to(text2, DOWN, buff=0.2)
        line3=Line(start=(1.1,1.5,0), end=(3.65,1.5,0), color=BLACK).next_to(text3, DOWN, buff=0.2)

        text4 =Tex("1 Choice", color=BLACK, font_size=28).next_to(line1, DOWN, buff=0.13)
        text5 =Tex("5 Choices", color=BLACK, font_size=28).next_to(line2, DOWN, buff=0.13)
        text6 =Tex("4 Choices", color=BLACK, font_size=28).next_to(line3, DOWN, buff=0.13)

        arrowline1=Line(start=(1.1,1.5,0), end=(1.8,1.5,0), color="#2E5E9E").next_to(text5, DOWN, buff=0.5).shift(RIGHT*0.5)
        arrowline2=Line(start=(1.1,1.5,0), end=(1.8,1.5,0), color="#2E5E9E").next_to(arrowline1, DOWN, buff=0.1)
        tri=Triangle(color="#2E5E9E", fill_color="#2E5E9E", fill_opacity=1).next_to(arrowline1, RIGHT).rotate(angle=40.3).scale(0.16)
        tri.shift(LEFT*1.4+DOWN*0.26)

        grp=VGroup(arrowline1, arrowline2, tri)
        grp.shift(DOWN*0.2+RIGHT*1.5).scale(0.7)

        formula=MathTex("1", r"\text{x}", "5", r"\text{x}", "4", "=", "20", color=BLACK, font_size=39).next_to(tri, buff=0.2)

        # Add to scene
        self.add(rect1, rect2, rect3, label1, label2, label3,
                 Smallest, Largest, Medium, arrow1, arrow2, arrow3,
                 text1, text2, text3, line1, line2, line3,
                 text4, text5, text6, arrowline1, arrowline2, tri, formula)