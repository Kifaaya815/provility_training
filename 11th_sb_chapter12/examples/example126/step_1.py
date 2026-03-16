from manim import *

config.frame_height = 9
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

class Example126a(Scene):
    def construct(self):

        text_color = BLACK

        # Table entries
        data = [[f"({i},{j})" for j in range(1,7)] for i in range(1,7)]

        table = Table(
            data,
            row_labels=[MathTex(str(i), color=text_color) for i in range(1,7)],
            col_labels=[MathTex(str(i), color=text_color) for i in range(1,7)],
            element_to_mobject=lambda x: MathTex(x, color=text_color),
            include_outer_lines=True
        )

        table.scale(0.45)

        # Change only table grid lines to white
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)

        for line in table.get_vertical_lines():
            line.set_color(WHITE)

        self.add(table)

        # Labels
        die1 = Tex("Die1", color=text_color).scale(0.45)
        die2 = Tex("Die2", color=text_color).scale(0.45)

        die1.shift(UP*2.2+LEFT*3)
        die2.shift(UP*1.8+LEFT*3.4)

        self.add(die1, die2)

        # Sum = 9 diagonal

        sum9 = Tex("Sum\\ 9", color=text_color).scale(0.5)
        sum9.next_to(table.get_cell((4,6)), RIGHT*5.6)
        sum7 = Tex("Sum\\ 7", color=text_color).scale(0.5)
        sum7.next_to(table.get_cell((2,6)), RIGHT*5.6)
        self.add(sum9, sum7)

        # Circles
        c1 = RoundedRectangle(width=0.5, height=6.7, corner_radius=0.25, color="#9BDEF2").rotate(-PI/2.97).shift(DOWN*0.27+RIGHT*0.35)
        c2 = RoundedRectangle(width=0.5, height=4.4, corner_radius=0.25, color="#F1C6B2").rotate(-PI/2.97).shift(DOWN*0.82+RIGHT*1.4)
        c3 = RoundedRectangle(width=0.5, height=0.8, corner_radius=0.25, color="#F9A2BC").rotate(PI/2).shift(DOWN*1.71+RIGHT*2.93)

        self.add(c1, c2, c3)

        # Sum 12 label
        sum12 = Tex("Sum\\ 12", color=text_color).scale(0.5)
        sum12.next_to(table.get_cell((7,6)), RIGHT*5.6)

        Rect= Rectangle(height=4.6, width=7.2, color="#C04E01").shift(LEFT*0.1+UP*0.1)
        line1=Line(start=(1,1,0),end=(1,2,0), color="#C04E01").scale(4.6).shift(DOWN*1.4+LEFT*3.68)
        line2=Line(start=(1,1,0),end=(2,1,0), color="#C04E01").scale(7.2).shift(DOWN*-0.59+LEFT*1.6)
        line3=Line(start=(1,1,0),end=(2,1,0), color="#C04E01").scale(1.3).shift(DOWN*-1+LEFT*4.69).rotate(-38*DEGREES)

        arrow1 = Arrow(start=(1.1,1,0), end=(2.02,1,0), color=PURE_RED).shift(UP*0.2+RIGHT*2)
        arrow2 = Arrow(start=(1.1,-0.2,0), end=(2.02,-0.2,0), color=PURE_RED).shift(UP*0.2+RIGHT*2)
        arrow3 = Arrow(start=(1.1,-1.95,0), end=(2.02,-1.95,0), color=PURE_RED).shift(UP*0.2+RIGHT*2)

        self.add(Rect, line1, line2, line3)
        self.add(arrow1, arrow2, arrow3)



        self.add(sum12)