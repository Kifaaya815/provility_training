from manim import *

DOT_BLUE = "#0343DF"
DOT_RED="#FF000D"

config.background_color=WHITE

class ManimAnimation(Scene):
    def construct(self):
        bluedot=Dot([-2.5,-2,0],color=DOT_BLUE,z_index=10).scale(2)
        left=Text("left",color=BLACK).next_to(bluedot,DOWN)
        reddot=Dot([2.5,-2,0],color=DOT_RED,z_index=10).scale(2)
        right=Text("right",color=BLACK).next_to(reddot,DOWN)

        blackdot1=Dot([0,-2,0],color=BLACK).scale(2) 
        blackdot2=Dot([0,2,0],color=BLACK).scale(2)

        center=Text("center",color=BLACK).next_to(blackdot2,UP)


        line1=Line(start=[-2.5,-2,0],end=[2.5,-2,0],color=BLACK).set_stroke(width=5)
        line2=always_redraw(lambda: Line(blackdot1.get_center(),end=blackdot2.get_center(),color=BLACK).set_stroke(width=5).add_tip())
        line3=always_redraw(lambda: Line(start=blackdot2.get_center(),end=bluedot.get_center(),color=BLACK).set_stroke(width=5))
        line4=always_redraw(lambda: Line(start=blackdot2.get_center(),end=reddot.get_center(),color=BLACK).set_stroke(width=5))

        self.play(FadeIn(bluedot,left))
        self.play(FadeIn(reddot,right))
        self.play(FadeOut(left,right))

        self.play(Create(line1))
        self.play(FadeIn(blackdot1))

        self.play(Create(line2),FadeIn(blackdot2))
        self.play(Create(line3))
        self.play(Create(line4))

        self.play(blackdot2.animate.shift(DOWN*2))
        self.play(blackdot2.animate.shift(UP*2))

        self.play(FadeIn(left,right,center),FadeOut(line1,line2,blackdot1))
        self.wait(1)        
