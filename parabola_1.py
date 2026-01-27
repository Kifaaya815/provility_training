from manim import *

PARA_BLUE = "#1f5cff"
LATUS_GREEN = "#2bbf3a"
POINT_RED = "#e6392e"

class ParabolaDiagram(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        graph_axes = Axes(
            x_range=[-6, 12, 1],
            y_range=[-8, 8, 1],
            axis_config={
                "include_tip": True,
                "color": BLACK,
                "include_ticks": False
            },
        ).scale(0.7)

        axis_labels = graph_axes.get_axis_labels(
            x_label=MathTex("X", color=BLACK).scale(0.7),
            y_label=MathTex("Y", color=BLACK).scale(0.7)
        )
        axis_labels[0].shift(DOWN * 0.32)
        axis_labels[1].shift(LEFT * 0.38 + UP * 0.15)

        x_mark = MathTex("X'", color=BLACK).next_to(graph_axes.x_axis, LEFT, buff=0.05).scale(0.65)
        y_mark = MathTex("Y'", color=BLACK).next_to(graph_axes.y_axis, DOWN, buff=0.05).scale(0.65)

        parab = graph_axes.plot_parametric_curve(
            lambda t: [ (t**2) / 12, t, 0],
            t_range=[-8, 8],
            color=PARA_BLUE
        )
        parab_eq = MathTex("y^2 = 12x", color=BLACK).move_to(graph_axes.c2p(7.8, -7.9)).scale(0.8)

        vertex = Dot(graph_axes.c2p(0, 0), color=POINT_RED)
        vertex_label = MathTex("V", color=BLACK).scale(0.8).next_to(vertex, DOWN + LEFT, buff=0.01).scale(0.7)
        vertex_coord_text = MathTex("(0,0)", color=BLACK).scale(0.8).next_to(vertex_label, DOWN, buff=0.01).scale(0.7)
        vertex_coord_text.shift(LEFT * 0.19)

        focus = Dot(graph_axes.c2p(3, 0), color=POINT_RED, z_index=10)
        focus_text = Text("Focus", color=BLACK, font_size=20).next_to(focus, DOWN + RIGHT, buff=0.1)
        focus_coord_text = MathTex("(3,0)", color=BLACK).scale(0.8).next_to(focus, DOWN + LEFT, buff=0.01).scale(0.7)

        directrix_line = DashedLine(
            start=graph_axes.c2p(-3, 7),
            end=graph_axes.c2p(-3, -7),
            color=POINT_RED,
            dash_length=0.15
        ).add_tip(tip_length=0.2, tip_width=0.2)\
         .add_tip(at_start=True, tip_length=0.2, tip_width=0.2)

        directrix_text = Text("Equation of\n   Directrix", color=BLACK, font_size=18, line_spacing=0.5).rotate(90*DEGREES)
        directrix_text.next_to(directrix_line, LEFT, buff=0.2)
        directrix_text.shift(DOWN * 1)
        directrix_eq = MathTex("x = -3", color=BLACK).scale(0.8).next_to(directrix_line, DOWN, buff=0.1)

        latus_line = Line(graph_axes.c2p(3, 6), graph_axes.c2p(3, -6), color=LATUS_GREEN).set_stroke(width=3.5)

        latus_brace = BraceBetweenPoints(graph_axes.c2p(4.5, 6), graph_axes.c2p(4.5, -6), direction=RIGHT, color=BLACK)
        latus_label = Text("      Length of\nLatus Rectum = 12", color=BLACK, font_size=20, line_spacing=0.8).next_to(latus_brace, RIGHT, buff=0.3)

        parab_axis_label = Text("Axis of parabola", color=BLACK, font_size=20).next_to(graph_axes.x_axis.get_end(), UP, buff=0.4)
        parab_axis_label.shift(RIGHT * 0.5)

        self.add(
            graph_axes, axis_labels, x_mark, y_mark,
            parab, parab_eq,
            vertex, vertex_label, vertex_coord_text,
            focus, focus_text, focus_coord_text,
            directrix_line, directrix_text, directrix_eq,
            latus_line, latus_brace, latus_label,
            parab_axis_label
        )
