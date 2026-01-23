from manim import *

class TriangleShape(Scene):
    def construct(self):
        triangle = Triangle(color=PINK).scale(2)
        self.add(triangle)
       
