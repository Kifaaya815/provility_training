from manim import *

class TextAnimation(Scene):
    def construct(self):
        text=Text("Manim Text",
                  color=BLUE,
                  font_size=75)
        text1=Text("Animation",
                   color=GREEN,
                   font_size=75)
        
        text.to_edge(UP)

        self.play(Write(text))
        self.play(Write(text1))
        self.wait(5)