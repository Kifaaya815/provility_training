from manim import *

config.frame_height = 10
config.frame_width = 22
config.pixel_height = 2200
config.pixel_width = 3000
config.background_color = WHITE

class Example1229b(Scene):
    def construct(self): 

        line_color = BLACK
        text_color = BLACK
   
        #LEFT DIAGRAM
        title = Tex("Consulting Firm", color=text_color).scale(1).shift(UP*6+RIGHT*2)

        top_line = Rectangle(height=3.35, width=14.8, color=line_color, fill_color="#E0F2F1", fill_opacity=1).shift(UP*3.95+RIGHT*1.75)

        # A1 box
        a1 = Tex("A1", color=text_color).scale(0.7)
        x_manager = Tex("Agency L", color=text_color).scale(0.6)

        prob_box1 = Rectangle(width=3.8, height=1.6, color=line_color, fill_color="#F9FBE7", fill_opacity=1)
        prob_text1 = MathTex(
            r"\begin{array}{l} \text{Rented: } 50\% \\ P(A_1) \end{array}",
        ).scale(0.53).set_color(text_color)

        prob_text11 = MathTex(r"\begin{array}{l} P( \text{Good Condition} \mid \text{Agency L})\\P(G \mid A_1)=90\% \end{array}").scale(0.52).set_color(text_color)
 
        prob_group1 = VGroup(prob_box1, prob_text1, prob_text11)
        prob_text1.move_to(prob_box1.get_center()).shift(UP*0.25+LEFT*1)
        prob_text11.next_to(prob_text1, DOWN, buff=0.26).shift(UP*0.2+RIGHT*0.99)

        block1 = VGroup(a1, x_manager, prob_group1).arrange(DOWN, buff=0.15)

        #A2 box
        a2 = Tex("A2", color=text_color).scale(0.7)
        y_manager = Tex("Agency M", color=text_color).scale(0.6)

        prob_box2 = Rectangle(width=3.8, height=1.6, color=line_color, fill_color="#FFF9C4", fill_opacity=0.9)
        prob_text2 = MathTex(
            r"\begin{array}{l} \text{Rented: } 30\% \\ P(A_2) \end{array}",
        ).scale(0.53).set_color(text_color)

        prob_text21 = MathTex(r"\begin{array}{l} P( \text{Good Condition} \mid \text{Agency M})\\P(G \mid A_2)=70\% \end{array}").scale(0.52).set_color(text_color)

        prob_group2 = VGroup(prob_box2, prob_text2, prob_text21)
        prob_text2.move_to(prob_box2.get_center()).shift(UP*0.25+LEFT*1.02)
        prob_text21.next_to(prob_text2, DOWN, buff=0.25).shift(UP*0.2+RIGHT*1.02)

        block2 = VGroup(a2, y_manager, prob_group2).arrange(DOWN, buff=0.15)

        #A3 box
        a3 = Tex("A3", color=text_color).scale(0.7)
        z_manager = Tex("Agency N", color=text_color).scale(0.6)

        prob_box3 = Rectangle(width=3.8, height=1.6, color=line_color, fill_color="#F8D1D1", fill_opacity=0.8)
        prob_text3 = MathTex(
            r"\begin{array}{l} \text{Rented: } 20\% \\ P(A_3) \end{array}",
        ).scale(0.53).set_color(text_color)

        prob_text31 = MathTex(r"\begin{array}{l} P( \text{Good Condition} \mid \text{Agency N})\\P(G \mid A_3)=60\% \end{array}").scale(0.52).set_color(text_color)

        prob_group3 = VGroup(prob_box3, prob_text3, prob_text31)
        prob_text3.move_to(prob_box3.get_center()).shift(UP*0.25+LEFT*1.02)
        prob_text31.next_to(prob_text3, DOWN, buff=0.25).shift(UP*0.2+RIGHT*1.02)

        block3 = VGroup(a3, z_manager, prob_group3).arrange(DOWN, buff=0.15)

        #Arrange blocks
        blocks = VGroup(block1, block2, block3)
        blocks.arrange(RIGHT, buff=1.1)
        blocks.shift(UP*4+RIGHT*2)

        join_point = Dot(ORIGIN, radius=0.01, color=line_color).shift(RIGHT*2+UP*1)

        #Lines
        line1 = Line(prob_box1.get_bottom(), join_point, color="#50AD55")
        line2 = Line(prob_box2.get_bottom(), join_point, color="#50AD55")
        line3 = Line(prob_box3.get_bottom(), join_point, color="#50AD55")

        bonus_text = Tex("Getting car in\\\\ good condition", color=text_color).scale(0.65)
        bonus_text.next_to(join_point, RIGHT, buff=0.2).shift(DOWN*0.7)

        arrow = Arrow(join_point, DOWN*0.8+RIGHT*2, buff=0, color="#50AD55", stroke_width=3.2)

        final_box = Rectangle(width=3.8, height=1.1, color=line_color, fill_color="#E0F2F1", fill_opacity=1)
        final_text = MathTex(r"P(A_3 \mid G)=?", color=text_color).scale(0.6)

        manager_text = Tex("From Agency N", color=BLACK).scale(0.6)

        B1_text=MathTex("G:", color=BLACK).next_to(prob_box1, LEFT, buff=0.1).scale(0.8).shift(UP*0.2)
        B2_text=MathTex("G:", color=BLACK).next_to(prob_box2, LEFT, buff=0.1).scale(0.8).shift(UP*0.2)
        B3_text=MathTex("G:", color=BLACK).next_to(prob_box3, LEFT, buff=0.1).scale(0.8).shift(UP*0.2)

        outer_text1=MathTex(r"A_1 \rightarrow \text{Car from Agency L}", color=BLACK)
        outer_text2=MathTex(r"A_2 \rightarrow \text{Car from Agency M}", color=BLACK).next_to(outer_text1, DOWN)
        outer_text3=MathTex(r"A_3 \rightarrow \text{Car from Agency N}", color=BLACK).next_to(outer_text2, DOWN).shift(LEFT*0.05)
        outer_text4=MathTex(r"G \rightarrow \text{Getting car in good condition}", color=BLACK).next_to(outer_text3, DOWN).shift(RIGHT*1.08)
        
        outer_grp=VGroup(outer_text1, outer_text2, outer_text3, outer_text4).next_to(top_line, buff=-9.6).scale(0.8).shift(DOWN*0.5)
        self.add(outer_text1, outer_text2, outer_text3, outer_text4)

        final_group = VGroup(final_box, final_text, manager_text)
        final_text.move_to(final_box.get_center()).shift(DOWN*0.2+LEFT*0.1)
        manager_text.move_to(final_box.get_center()).shift(UP*0.2+LEFT*0.1)
        final_group.next_to(arrow.get_end(), DOWN, buff=0.3)
        final_box.shift(UP*0.1)
        final_text.shift(UP*0.1)
        manager_text.shift(UP*0.1)

        # Add everything
        self.add(title, top_line, blocks, join_point, line1, line2, line3,
                 arrow, final_group, bonus_text)
        self.add(B1_text, B2_text, B3_text)

        left_diagram = VGroup(line1, line2, line3, title,
                              top_line, block1, block2, block3,
                              join_point, arrow, final_group,
                              B1_text, B2_text, B3_text, bonus_text)
        
        new_grp=VGroup(left_diagram, outer_grp)
        
        left_diagram.shift(LEFT*9).scale(1)
        new_grp.scale(1).shift(RIGHT*4+DOWN*2)