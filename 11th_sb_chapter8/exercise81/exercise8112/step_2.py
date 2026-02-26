from manim import *

config.frame_height = 8
config.frame_width = 10
config.pixel_width = 2500
config.pixel_height = 2500

class Exercise8112b(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        A = LEFT * 1.5 + DOWN * 2
        B = RIGHT * 3 + DOWN * 3
        C = RIGHT * 3 + UP * 3
        D = LEFT * 1.5 + UP * 2

        DB = Line(A,C ,color=GREEN)

        F = DB.point_from_proportion(0.6)
        AF = Line(D,F,color="#0165FC").set_z_index(-1)
        AD = Line(A,D,color=GREEN)
        DC=Line(D,C,color=GREEN)

        label_D = Text("D", font_size=28, color=BLACK).next_to(A, DOWN)
        label_B = Text("B", font_size=28, color=BLACK).next_to(C, UP)
        label_A = Text("A", font_size=28, color=BLACK).next_to(D, UP)
        label_F = Text("F", font_size=28, color=BLACK).next_to(F, DOWN*0.2+RIGHT*0.4)
        
        def mid_tip(line, color=BLACK, reverse=False):
            mid = line.point_from_proportion(0.5)
            direction = line.get_unit_vector()
            if reverse:
                direction = -direction

            seg = Line(
                mid - direction * 0.22,
                mid + direction * 0.22,
                color=color,
                stroke_width=0  
            )
            seg.add_tip(tip_shape=StealthTip, tip_length=0.20, tip_width=0.20)
            return seg

        tip1 = mid_tip(AD, reverse=True)         
        tip2 = mid_tip(AF).shift(UP*0.01)
        tip3 = mid_tip(DC).shift(DOWN * 0)

        def tick_mark(start, end, position=0.4, size=0.3):
             point = interpolate(start, end, position)
             direction = end - start
             unit_dir = direction / np.linalg.norm(direction)
             perp = np.array([-unit_dir[1], unit_dir[0], 0])
             return Line( point - perp * size/2, point + perp * size/2, color=BLACK, stroke_width=3)
        tick1 = tick_mark(F,A ,0.59)
        tick2 = tick_mark(F,A, 0.62)
        tick3 = tick_mark(F,C, 0.63)
        tick4 = tick_mark(F,C, 0.59)
        tick_label1=MathTex("1",color=BLACK).next_to(tick2)
        tick_label2=MathTex("1",color=BLACK).next_to(tick4)

        self.add(DB,AF,AD,DC,label_A, label_B, label_D,label_F,tip1,tip2,tip3,tick1,tick2,tick3,tick4,tick_label1,tick_label2)