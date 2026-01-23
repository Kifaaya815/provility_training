from manim import *

class TriangleShape(Scene):
    def construct(self):
        triangle = Triangle(color=PINK,
                            fill_color=BLUE,
                            fill_opacity=1
                            ).scale(2)
        
        triangle.set_stroke(width=50)
        self.add(triangle)
    
        