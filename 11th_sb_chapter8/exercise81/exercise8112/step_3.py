from manim import *

config.frame_height = 8
config.frame_width = 10
config.pixel_width = 2500
config.pixel_height = 2500

class Exercise8112c(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Points
        D = LEFT * 2 + DOWN * 2
        B = RIGHT * 2 + UP * 2
        C = RIGHT * 2 + DOWN * 2

        # Triangle
        DB = Line(D, B, color="#C9B003")
        BC = Line(B, C, color="#C9B003")
        CD = Line(C, D, color="#C9B003")

        # Point F on DB
        F = DB.point_from_proportion(0.5)
        FC = Line(F, C, color="#0165FC")

        # ---- Mid-tip function (direction-controlled) ----
        def mid_tip_towards(start_point, end_point, length=0.45):
            direction = normalize(end_point - start_point)
            mid = (start_point + end_point) / 2
            seg = Line(
                mid - direction * length / 2,
                mid + direction * length / 2,
                color=BLACK,
                stroke_width=0,   # shaft invisible
            )
            seg.add_tip(tip_length=0.27, tip_width=0.25)
            return seg

        # Tips facing required points
        tip_BC = mid_tip_towards(C, B)   # faces B
        tip_CD = mid_tip_towards(C, D)   # faces D
        tip_FC = mid_tip_towards(C, F)   # faces F

        # Labels
        label_D = Text("D", font_size=28, color=BLACK).next_to(D, DOWN)
        label_B = Text("B", font_size=28, color=BLACK).next_to(B, UP)
        label_C = Text("C", font_size=28, color=BLACK).next_to(C, DOWN)
        label_F = Text("F", font_size=28, color=BLACK).next_to(F, LEFT)

                # Lines BF and DF (for tick reference only, not added to scene)
        BF = Line(B, F)
        DF = Line(D, F)

        # ---- Double-tick function ----
        def double_tick(line, length=0.3, gap=0.08):
            mid = line.get_midpoint()
            direction = line.get_unit_vector()
            normal = np.array([-direction[1], direction[0], 0])

            tick1 = Line(
                mid - normal * length / 2 + direction * gap,
                mid + normal * length / 2 + direction * gap,
                color=BLACK,
                stroke_width=3
            )

            tick2 = Line(
                mid - normal * length / 2 - direction * gap,
                mid + normal * length / 2 - direction * gap,
                color=BLACK,
                stroke_width=3
            )

            return VGroup(tick1, tick2)

        # Double ticks
        tick_BF = double_tick(BF)
        tick_DF = double_tick(DF)

        label_11=MathTex("1", color=BLACK).next_to(tick_BF, UP*0.3+LEFT*0.2)
        label_12=MathTex("1", color=BLACK).next_to(tick_DF, UP*0.3+LEFT*0.2)

        self.add(
            FC, DB, BC, CD,
            tip_BC, tip_CD, tip_FC,
            label_D, label_B, label_C, label_F,
            tick_BF, tick_DF, label_11, label_12
        )