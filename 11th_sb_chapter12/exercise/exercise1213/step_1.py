from manim import *

config.frame_height = 10
config.frame_width = 13
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE


class Exercise1213(Scene):
    def construct(self):
        data = [ [r"\text{M (Mango)}", r"\text{A (Apple)}", r"\text{Total Fruits (T)}"],
                 ["5", "4", "9"]]

        table = Table(data,
                      element_to_mobject=lambda s: MathTex(s, color=BLACK),
                      line_config={"stroke_width": 6,  
                                   "color": "#A8415B",
                                   "joint_type": LineJointType.MITER},
                      include_outer_lines=True,
                      h_buff=0.8,
                      v_buff=0.5)

        table.move_to(ORIGIN)

        rect = Rectangle(height=1.88, width=10.45, color="#A8415B", stroke_width=5)

        self.add(table, rect)