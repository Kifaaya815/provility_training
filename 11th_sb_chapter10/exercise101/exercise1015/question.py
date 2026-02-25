from manim import *

config.frame_height = 8
config.frame_width = 24
config.pixel_width = 2800
config.pixel_height = 2800

class Question1015(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        q_image = ImageMobject("question.png")
        q_image.scale(2.5).shift(LEFT * 0.1)
        self.add(q_image)