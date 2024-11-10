from manim import *

def config():
    config.pixel_height = 1080  # 1080p resolution
    config.pixel_width = 1920   # 1920x1080
    config.frame_rate = 60      # 30 FPS
    config.output_file = "high_quality_output_2"

config()

class SimilarityAndScale(Scene):
    def construct(self):
        def titel():
            title = Text("Ähnlichkeit in der Geometrie", font_size=50)
            self.play(Write(title))
            self.wait(1.5)
            self.play(FadeOut(title))
        

        def grid():
            grid = NumberPlane()

            # Display the grid in the background
            self.add(grid)


        def trangles():
            triangle_blue = Polygon(
                [-1, -2, 0], [-4, -2, 0], [-4, 2, 0], color=BLUE, fill_opacity=0.3, stroke_width = 5)
            triangle_green = Polygon(
                [5.5, -3, 0], [1, -3, 0], [1, 3, 0], color=RED, fill_opacity=0.3, stroke_width = 5)

            self.play(Create(triangle_blue), Create(triangle_green))

            label_blue = Text("Dreieck A", font_size=24).next_to(triangle_blue, DOWN) # create the labels
            label_green = Text("Dreieck B", font_size=24).next_to(triangle_green, DOWN)

            self.wait(0.5)

            self.play(Write(label_blue), Write(label_green)) # show the Labels
            
            self.wait(0.5)
            
            self.play(FadeOut(label_blue, label_green)) # fade out the labels

            self.play(ApplyMethod(triangle_blue.scale, 1.5)) # scale the blue triangle
            self.wait(0.5)
            self.play(Transform(triangle_blue, triangle_green)) # move blue to green

            self.wait(0.5)

            triangle_blue_1 = Polygon([-1, -2, 0], [-4, -2, 0], [-4, 2, 0], color=BLUE , fill_opacity=0.3, stroke_width = 5)
            self.play(Transform(triangle_blue, triangle_blue_1))
            
            self.wait(0.1)

            self.play(FadeOut(triangle_blue_1, run_time=0.01))
            
            self.play(
                ApplyMethod(triangle_blue.scale, 0.5),
                ApplyMethod(triangle_green.scale, 0.5)
            )
            
            self.play(
                triangle_blue.animate.shift(UP * 2 + RIGHT * 1),
                triangle_green.animate.shift(UP * 2)
            ) 

            text_sides = Text("Anz. Seiten:", font_size=35)
            text_amt_sides_1 = Text("3", font_size=40)
            text_amt_sides_2 = Text("3", font_size=40)
            
            text_sides.move_to([-5,-0.5, 0])
            text_amt_sides_1.move_to([-1.5,-0.5, 0])
            text_amt_sides_2.move_to([3.5,-0.5, 0])

            self.play(Write(text_sides))
            self.play(
                Write(text_amt_sides_1),
                Write(text_amt_sides_2)
                )

            self.wait(2)
            
            text_angle = MathTex(r"\alpha \beta \gamma", font_size=70).move_to([-5,-1.5, 0])
            text_angle_1 = Text("90° 53° 37°", font_size=40)
            text_angle_2 = Text("90° 53° 37°", font_size=40)

            text_angle_1.move_to([-1.5,-1.5, 0])
            text_angle_2.move_to([3.5,-1.5, 0])

            self.play(Write(text_angle))
            self.play(
                Write(text_angle_1),
                Write(text_angle_2)
                )
            
            self.wait(2)

            text_ahnich = Text("Ähnlich?", font_size=35)
            text_ahnich_1 = Text("Ja", font_size=40)
            text_ahnich_2 = Text("Ja", font_size=40)

            text_ahnich.move_to([-5,-2.5, 0])
            text_ahnich_1.move_to([-1.5,-2.5, 0])
            text_ahnich_2.move_to([3.5,-2.5, 0])

            self.play(Write(text_ahnich))
            self.play(
                Write(text_ahnich_1),
                Write(text_ahnich_2)
                )
            self.wait(5)

            self.play(*[FadeOut(mobject) for mobject in self.mobjects])
            self.wait(1)
        

        def sqrs():
            rct_1 = Rectangle(width=2.0, height=3.0, color=YELLOW, fill_opacity=0.5, stroke_width = 5)
            rct_2 = Rectangle(width=2.0, height=6.0, color=GREEN, fill_opacity=0.5, stroke_width = 5)

            rct_1.move_to([-2, 0, 0])
            rct_2.move_to([2, 0, 0])

            self.play(
                Create(rct_1),
                Create(rct_2)
                )
            
            self.wait(2)

            self.play(rct_1.animate.shift([4, 0, 0]))

            self.wait(0.5)

            self.play(rct_1.animate.scale(2))

            self.wait(2)

            self.play(rct_1.animate.scale(0.5))

            self.play(
                rct_1.animate.move_to([-1.5, 1.5, 0]),
                rct_2.animate.move_to([3.5, 1.5, 0])
                )

            self.play(
                rct_1.animate.scale(0.5),
                rct_2.animate.scale(0.5)
                )
            
            text_sides = Text("Anz. Seiten:", font_size=35)
            text_amt_sides_1 = Text("4", font_size=40)
            text_amt_sides_2 = Text("4", font_size=40)
            
            text_sides.move_to([-5,-0.5, 0])
            text_amt_sides_1.move_to([-1.5,-0.5, 0])
            text_amt_sides_2.move_to([3.5,-0.5, 0])

            self.play(Write(text_sides))
            self.play(
                Write(text_amt_sides_1),
                Write(text_amt_sides_2)
                )

            self.wait(2)
            
            text_angle = MathTex(r"\alpha \beta \gamma \delta", font_size=50).move_to([-5,-1.5, 0])
            text_angle_1 = Text("90° 90° 90° 90°", font_size=30)
            text_angle_2 = Text("90° 90° 90° 90°", font_size=30)

            text_angle_1.move_to([-1.5,-1.5, 0])
            text_angle_2.move_to([3.5,-1.5, 0])

            self.play(Write(text_angle))
            self.play(
                Write(text_angle_1),
                Write(text_angle_2)
                )
            
            self.wait(2)

            text_ahnich = Text("Ähnlich?", font_size=35)
            text_ahnich_1 = Text("Nein", font_size=40)
            text_ahnich_2 = Text("Nein", font_size=40)

            text_ahnich.move_to([-5,-2.5, 0])
            text_ahnich_1.move_to([-1.5,-2.5, 0])
            text_ahnich_2.move_to([3.5,-2.5, 0])

            self.play(Write(text_ahnich))
            self.play(
                Write(text_ahnich_1),
                Write(text_ahnich_2)
                )

            self.wait(2)

            self.play(
                FadeOut(
                    text_sides,
                    text_amt_sides_1,
                    text_amt_sides_2,
                    text_angle,
                    text_angle_1,
                    text_angle_2,
                    text_ahnich,
                    text_ahnich_1,
                    text_ahnich_2
                )
            )
            
            rct_1_label_top = MathTex("AB=2").next_to(rct_1.get_top(), UP)  # Label for the top side
            rct_1_label_left = MathTex("AD=3").next_to(rct_1.get_left(), LEFT)  # Label for the left side
            rct_2_label_top = MathTex("AB=2").next_to(rct_2.get_top(), UP)  # Label for the top side
            rct_2_label_left = MathTex("AD=6").next_to(rct_2.get_left(), LEFT)  # Label for the left side


            rct_1_label_top.set_color(YELLOW)
            rct_1_label_left.set_color(YELLOW)
            rct_2_label_top.set_color(GREEN)
            rct_2_label_left.set_color(GREEN)

            self.play(
                Write(rct_1_label_top),
                Write(rct_1_label_left),
                Write(rct_2_label_top),
                Write(rct_2_label_left)
            )
            equation = MathTex(r"\frac{AB}{AD}", r"\neq", r"\frac{AB}{AD}", r"\text{= nicht Ähnlich}")
            equation_1 = MathTex(r"\frac{2}{3}", r"\neq", r"\frac{2}{6}", r"\text{= nicht Ähnlich}")

            equation[0].set_color(YELLOW)  # AB/AD (yellow)
            equation[2].set_color(GREEN)  # AB/AD (green)
            equation_1[0].set_color(YELLOW)  # AB/AD (yellow)
            equation_1[2].set_color(GREEN)  # AB/AD (green)

            equation.move_to([0, -1, 0])
            equation_1.move_to([0, -2.5, 0])

            self.play(
                Write(equation),
                Write(equation_1)
                )
        

        def sqrex():
            rct_1 = Rectangle(width=2.0, height=3.0, color=YELLOW, fill_opacity=0.5, stroke_width = 5)
            rct_2 = Rectangle(width=4.0, height=6.0, color=GREEN, fill_opacity=0.5, stroke_width = 5)

            rct_1.move_to([-2, 0, 0])
            rct_2.move_to([3, 0, 0])

            self.play(
                Create(rct_1),
                Create(rct_2)
                )
            
            self.wait(2)

            self.play(rct_1.animate.shift([5, 0, 0]))

            self.wait(0.5)

            self.play(rct_1.animate.scale(2))

            self.wait(2)

            self.play(rct_1.animate.scale(0.5))

            self.play(
                rct_1.animate.move_to([-1.5, 1.5, 0]),
                rct_2.animate.move_to([3.5, 1.5, 0])
                )

            self.play(
                rct_1.animate.scale(0.5),
                rct_2.animate.scale(0.5)
                )
            
            
            rct_1_label_top = MathTex("AB=2").next_to(rct_1.get_top(), UP)  # Label for the top side
            rct_1_label_left = MathTex("AD=3").next_to(rct_1.get_left(), LEFT)  # Label for the left side
            rct_2_label_top = MathTex("AB=4").next_to(rct_2.get_top(), UP)  # Label for the top side
            rct_2_label_left = MathTex("AD=6").next_to(rct_2.get_left(), LEFT)  # Label for the left side


            rct_1_label_top.set_color(YELLOW)
            rct_1_label_left.set_color(YELLOW)
            rct_2_label_top.set_color(GREEN)
            rct_2_label_left.set_color(GREEN)

            self.play(
                Write(rct_1_label_top),
                Write(rct_1_label_left),
                Write(rct_2_label_top),
                Write(rct_2_label_left)
            )

            self.wait(0.5)

            equation = MathTex(r"\frac{AB}{AD}", "=", r"\frac{AB}{AD}", r"\text{= Ähnlich}")
            equation_1 = MathTex(r"\frac{2}{3}", "=", r"\frac{4}{6}", r"\text{= Ähnlich}")

            equation[0].set_color(YELLOW)  # AB/AD (yellow)
            equation[2].set_color(GREEN)  # AB/AD (green)
            equation_1[0].set_color(YELLOW)  # AB/AD (yellow)
            equation_1[2].set_color(GREEN)  # AB/AD (green)

            equation.move_to([0, -1, 0])
            equation_1.move_to([0, -2.5, 0])

            self.play(
                Write(equation),
                Write(equation_1)
                )
            self.wait(4)

            self.play(*[FadeOut(mobject) for mobject in self.mobjects])
            self.wait(1)


        def rules():
            text_regeln = Text("-Regeln-", font_size=50)
            text_regeln.to_edge(LEFT)
            text_regeln.shift([1, 2.5, 0])
            self.play(Write(text_regeln))

            self.wait(2)

            point_1 = Dot(point=[-6, 1.5, 0], color=WHITE, radius=0.2)
            self.play(Create(point_1))

            text_s_a = Text("Gleiche Anz. der Seiten", font_size=40)
            text_s_a.to_edge(LEFT)
            text_s_a.shift([1, 1.5, 0])
            self.play(Write(text_s_a))

            self.wait(2)

            point_2 = Dot(point=[-6, 0.25, 0], color=WHITE, radius=0.2)
            self.play(Create(point_2))

            text_w = Text("Gleiche Winkeln", font_size=40)
            text_w.to_edge(LEFT)
            text_w.shift([1, 0.25, 0])
            self.play(Write(text_w))

            self.wait(2)

            point_3 = Dot(point=[-6, -1, 0], color=WHITE, radius=0.2)
            self.play(Create(point_3))

            equation = MathTex(r"\frac{AB}{AD}", "=", r"\frac{AB}{AD}")
            equation[0].set_color(YELLOW)  # AB/AD (yellow)
            equation[2].set_color(GREEN)
            equation.to_edge(LEFT)
            equation.shift([1, -1, 0])
            self.play(Write(equation))

            self.wait(2)

            self.play(*[FadeOut(mobject) for mobject in self.mobjects])
            self.wait(1)

            
        def map():
            map = ImageMobject("Lib\maps\map_1.png")
            luft_b = ImageMobject("Lib\maps\map_2.png")

            map.scale(0.6)
            luft_b.scale(0.6)
            map.move_to([3, 1, 0])
            luft_b.move_to([-3, 1, 0])

            self.play(
                FadeIn(map),
                FadeIn(luft_b)
                ) 

            kartenmasstab = MathTex(r"\text{Kartenmaßstab = }", r"\frac{1}{50'000}")
            kartenmasstab[1].set_color(RED)
            kartenmasstab.move_to([0, -2.75, 0])
            self.play(Write(kartenmasstab))

            self.play(FadeOut(luft_b))

            self.play(kartenmasstab.animate.shift([-3, 4.75, 0]))

            self.play(map.animate.move_to([3.5 ,0, 0]))
            self.play(map.animate .scale(1.4))

            text_kleiner = Text("50'000x kleiner", font_size=35)
            text_kleiner.move_to([-3.5, 0, 0])
            self.play(Write(text_kleiner))
            
            self.wait(1.5)

            left_side = MathTex(r"1 \, \text{cm} \times 50{,}000 =")
            right_side = MathTex(r"50{,}000 \, \text{cm}")

            left_side.move_to([-4.5, -1.5, 0])
            right_side.next_to(left_side, RIGHT)

            self.play(Write(left_side), Write(right_side))
            self.wait(1.5)

            right_side_meters = MathTex(r"500 \, \text{m}")
            right_side_meters.next_to(left_side, RIGHT)

            self.play(TransformMatchingTex(right_side, right_side_meters))
            self.wait(1.5)

            right_side_kilometers = MathTex(r"0.5 \, \text{km}")
            right_side_kilometers.next_to(left_side, RIGHT)

            self.play(TransformMatchingTex(right_side_meters, right_side_kilometers))
            self.wait(3)


            left_side = MathTex(r"3 \, \text{cm} \times 50{,}000 =")
            right_side = MathTex(r"150{,}000 \, \text{cm}")

            left_side.move_to([-4.5, -2.5, 0])
            right_side.next_to(left_side, RIGHT)

            self.play(Write(left_side), Write(right_side))
            self.wait(1.5)

            right_side_meters = MathTex(r"1500 \, \text{m}")
            right_side_meters.next_to(left_side, RIGHT)

            self.play(TransformMatchingTex(right_side, right_side_meters))
            self.wait(1.5)

            right_side_kilometers = MathTex(r"1.5 \, \text{km}")
            right_side_kilometers.next_to(left_side, RIGHT)

            self.play(TransformMatchingTex(right_side_meters, right_side_kilometers))

            self.wait(3)

            self.play(*[FadeOut(mobject) for mobject in self.mobjects])
            self.wait(1)


        titel()
        #grid()
        self.wait(2)
        trangles()
        self.wait(2)
        self.clear()
        #grid()
        sqrs()
        self.wait(4)
        self.clear()
        #grid()
        sqrex()
        #grid()
        rules()
        map()
        
        





