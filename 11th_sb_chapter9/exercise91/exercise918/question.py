from manim import *

config.frame_height = 10
config.frame_width = 14
config.pixel_height = 3200
config.pixel_width = 3200
config.background_color = WHITE

AXISGREEN= "#1B7F3F"
LINEBLUE= "#2E2F75"

class Exercise918(Scene):
    def construct(self):

        axes = Axes(x_range=[-4.2, 6, 1],
                    y_range=[-1.9, 10, 1],
                    x_length=11.5,
                    y_length=8.5,
                    axis_config={"color": AXISGREEN,
                                 "stroke_width": 8},
                    tips=True)

        axes.shift(DOWN*0.3)

        axes.add_coordinates(font_size=28, color=BLACK)

        grid = VGroup()
        grid_color = "#4c6ef5"

        for x in range(-4, 7):
            line = Line(axes.coords_to_point(x, -1.5),
                        axes.coords_to_point(x, 11.4),
                        stroke_color=grid_color,
                        stroke_width=1.2,
                        stroke_opacity=0.5)
            grid.add(DashedVMobject(line, num_dashes=120))

        for y in range(-1, 12):
            line = Line(axes.coords_to_point(-4, y),
                        axes.coords_to_point(6, y),
                        stroke_color=grid_color,
                        stroke_width=1.2,
                        stroke_opacity=0.5)
            grid.add(DashedVMobject(line, num_dashes=120))

        graph = axes.plot(lambda x: x**2 + 2,
                          x_range=[-2.7, 2.7],
                          color=LINEBLUE,
                          stroke_width=7)

        point = Dot(axes.coords_to_point(1, 3),
                    radius=0.14,
                    color=BLACK)

        x_label = MathTex("x", font_size=50, color=BLACK)
        x_label.next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)

        y_label = MathTex("y", font_size=50, color=BLACK)
        y_label.next_to(axes.y_axis.get_end(), UP, buff=0.15)

        self.add(grid, axes, graph, point, x_label, y_label)
