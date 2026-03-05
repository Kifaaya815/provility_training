from manim import *

config.frame_height = 9
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

class Exercise1238(Scene):
    def construct(self):
        data = [ ["", "W", "B"],
                 ["1", "5", "3"],
                 ["2", "4", "6"] ]

        table = Table(data, 
                      line_config={"stroke_width": 6,
                                   "color": "#9D5783",
                                   "joint_type": LineJointType.MITER},
                      element_to_mobject=lambda s: Text(s, color=BLACK, font_size=42),
                      include_outer_lines=True,
                      h_buff=2,
                      v_buff=1)

        gray_indices = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)]

        for idx in gray_indices:
            cell = table.get_cell(idx)
            cell.set_fill(GRAY, opacity=1)
            cell.set_z_index(0) 

        for entry in table.get_entries():
            entry.set_z_index(2)

        top_left_cell = table.get_cell((1, 1))
        
        diag_line = Line(top_left_cell.get_corner(UL), 
                         top_left_cell.get_corner(DR), 
                         color="#9D5783", 
                         stroke_width=6).set_z_index(3)

        ball_text = Text("Ball", color=BLACK, font_size=36)
        bag_text = Text("Bag", color=BLACK, font_size=36)

        ball_text.move_to(top_left_cell.get_center() + UP * 0.4 + RIGHT * 0.5)
        bag_text.move_to(top_left_cell.get_center() + DOWN * 0.4 + LEFT * 0.5)
        
        ball_text.set_z_index(3)
        bag_text.set_z_index(3)

        rect = Rectangle(height=4.3, width=7.2, color="#9D5783", stroke_width=5)

        self.add(table)
        self.add(diag_line, ball_text, bag_text, rect)