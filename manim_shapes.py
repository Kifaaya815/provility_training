from manim import *

class ShapeBuild(Scene):
    def construct(self):
        circle=Circle(radius=1,color=PINK,fill_color=BLUE,fill_opacity=1)
        square=Square(side_length=2,color=BLUE,fill_color=PINK,fill_opacity=1)
        triangle=Triangle(color=YELLOW,fill_color=GREEN,fill_opacity=1)
        dot=Dot(point=UP*2,color=GREEN)

        circle.set_stroke(width=30)
        square.set_stroke(width=20)
        triangle.set_stroke(width=40)
        dot.set_stroke(width=70)

        square.next_to(circle,RIGHT)
        triangle.next_to(circle,LEFT)

        self.add(circle,square,triangle,dot)
        self.wait(5)