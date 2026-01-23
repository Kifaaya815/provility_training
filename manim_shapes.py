from manim import *

class ShapeBuild(Scene):
    def construct(self):
        circle=Circle(radius=1,color=PINK)
        square=Square(side_length=2,color=BLUE)
        triangle=Triangle(color=YELLOW)
        dot=Dot(point=UP*2,color=GREEN)

        square.next_to(circle,RIGHT)
        triangle.next_to(circle,LEFT)

        self.add(circle,square,triangle,dot)
        self.wait(5)