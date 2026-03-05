from manim import *

config.frame_height = 9
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE


class Example1210(Scene):
    def construct(self):
        line_color = BLACK

        data = [ ["n(S)", "6", "5", "4"],
                 ["n(A)", "5", "4", ""] ]

        table = Table(data,
                      line_config={"color": line_color,
                                   "stroke_width": 6.5,
                                   "joint_type": LineJointType.MITER},
                      element_to_mobject=lambda x: Text(x, color=BLACK, font_size=48),
                      include_outer_lines=True)

        table.scale(1)
        
        table.set_z_index(0)

        for entry in table.get_entries():
            entry.set_z_index(3)

        gray_cells_list = []
        for col in range(1, 4):
            cell = table.get_cell((2, col), color=BLACK)
            cell.set_fill(GRAY, opacity=0.3)
            cell.set_z_index(1)  
            gray_cells_list.append(cell)

        red_cell = table.get_cell((2, 4), color=BLACK)
        red_cell.set_fill(PURE_RED, opacity=1)
        red_cell.set_z_index(1)

        red_text = Text("Red", color=WHITE, font_size=48)
        red_text.move_to(red_cell.get_center())
        red_text.set_z_index(3)

        top1 = Text("6", color=BLACK, font_size=48)
        top2 = Text("6", color=BLACK, font_size=48)
        top3 = Text("3", color=BLACK, font_size=48)

        top1.next_to(table.get_cell((1, 2)), UP, buff=0.25)
        top2.next_to(table.get_cell((1, 3)), UP, buff=0.25)
        top3.next_to(table.get_cell((1, 4)), UP, buff=0.25)

        rect = Rectangle(height=2.85, width=7.55, color=BLACK, stroke_width=5)

        self.add(table)            
        self.add(*gray_cells_list) 
        self.add(red_cell)         
        self.add(red_text)         
        self.add(top1, top2, top3, rect)