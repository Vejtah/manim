from manim import *
import random
import math
from tools import Tools # tools py code : in tools

tl = Tools()

#=============================================================================


def config():
    config.pixel_height = 2160  # 1080p resolution
    config.pixel_width = 3840   # 1920x1080
    config.frame_rate = 120      # 30 FPS
    config.output_file = "nt_output"


config()


#=============================================================================


def transform(x, y):
    return [x, y , 0]


#=============================================================================


class genitik(Scene):
    def construct(self):

        def grid():
            
            grid = NumberPlane()

            # Display the grid in the background
            self.add(grid)

        
        def zoom(scale=2, runtime=1):
            self.play(Group(*self.mobjects).animate.scale(scale), run_time=runtime)

            
            #=============================================================================


        def intro_gen(): 
            title = Text("Genetik", font_size=80)
            self.play(Write(title))
            self.wait(1.5)
            self.play(FadeOut(title))


        def intro_mitose():
            title = Text("Mitose", font_size=50)
            self.play(Write(title))
            self.wait(1.5)
            self.play(FadeOut(title))


        def mitose():
            if True: # checkpoint 1 : lines in kern
                zelle_txt = Text("Zelle", font_size=35)
                zelle_txt.move_to([0,3, 0])

                zelle_out = Circle(radius=2.5, color=BLUE, fill_opacity=0.4) # create zelle
                zelle_out.move_to([0, 0 , 0])

                zelle_kern = Circle(radius=1.5, color=YELLOW, fill_opacity=0.6) # zellen kern
                zelle_kern.move_to([0, 0 , 0])

                label_zelle_kern = Text("Zellenkern", font_size=24).next_to(zelle_kern, UP) # create the label
                

                self.play(Write(zelle_txt), # show zelle and label
                          Create(zelle_out))


                self.wait(0.5)

                self.play(Create(zelle_kern), # show kern and label
                          Write(label_zelle_kern))


                self.wait(0.5)
                # animate chromatids
                
                colors = [RED, RED_A, RED_B, RED_C, RED_D, RED_E] # cloors for chromatids in kern
                chromatids = [] # list for saving all original chromatids


                for i in range(15): # small chrms in bckg

                    chromatid_b = VMobject() 

                    rand_x, rand_y = tl.ran_pos_circle(radius=1.4, precision=10, y=-0) # chose random pos in circle

                    while ((((rand_y + 0.5) ** 2) + ((rand_x) ** 2)) ** 0.5) >= 1.4 or ((((rand_y - 0.5) ** 2) + ((rand_x) ** 2)) ** 0.5) >= 1.4: # check if not sticking out
                        rand_x, rand_y = tl.ran_pos_circle(radius=1.4, precision=10, y=-0) # chose random pos in circle


                    start_chrom = [rand_x, rand_y + 0.5, 0] # create line from one point
                    end_chrom = [rand_x, rand_y - 0.5, 0]

                    chromatid_b.set_points_as_corners([start_chrom, end_chrom]) # create the line
                    
                    chromatid_b.set_stroke(width=5,  # changes to lines
                                           color=colors[i % len(colors)], # choose always diferent color 
                                           opacity=(random.randint(50, 100) / 100)) # random opacity

                    chromatids.append(chromatid_b) # add this chromatid to originals
    
                    self.play(Create(chromatid_b),  run_time=0.1) # show this chromatid

            wait = 0.1 # easy way to change all 1ing functions

            # create the white chrom on front

            chromatid = VMobject()
            chromatid.set_points_as_corners([[0, 1, 0], [0, -1, 0]])
            chromatid.set_stroke(width=10, color=WHITE)

            chromatids.append(chromatid)

            self.play(Create(chromatid),  run_time=0.2)

            #===================================================

            self.play(Group(*self.mobjects).animate.move_to([-3, 0, 0]), runtime=0.5) # move the wole scene to left

            #grid()

            chromatid_c = chromatid.copy() # create a copy of the big chrom. wich will be transformed later

            chromatid_scaled = VMobject() # create a replica but bigger on right side
            chromatid_scaled.set_points_as_corners([[2, 2.5, 0], [2, -2.5, 0]])
            chromatid_scaled.set_stroke(width=25, color=WHITE)

            self.play(Transform(chromatid_c, chromatid_scaled)) # transform from small to big to show its same 
            self.remove(chromatid_c) # fuck the copy: not needed anymore

            chromatid_insp_l = VMobject() # group for left side of chromatid
            chromatid_insp_r = VMobject() # same for right

            chrom_side_l = Line(start=[1.5, 2.5, 0], end=[1.5, -2.5, 0]) # create line for side of chromatid (left side)
            chrom_side_l.set_stroke(color=WHITE, width=10)
            chromatid_insp_l.add(chrom_side_l) # add to left side group

            chrom_side_r = chrom_side_l.copy() # use left line for right by moving it
            chrom_side_r.shift([1, 0, 0])
            chromatid_insp_r.add(chrom_side_r) # add it to right side group

            chrom_sides = VGroup(chrom_side_l, chrom_side_r) # Vgrp for transform



            self.play(ReplacementTransform(chromatid_scaled, chrom_sides)) # go from while line to two thin 
            
            # create the ladder in cromatid
            hight = 5 # how tall 
            brt = 1 # how thic
            segments = 10 # amt ladders
            start_y = -2.5 # 
            start_x = 1.5
            colours = [RED, BLUE, YELLOW, GREEN] # clours of acids (T C G A)
            col_com = [GREEN, YELLOW, BLUE, RED] # coresponding acids

            segm = hight / segments # calc hight of each segment

            colrs_save = [] # save colours from left for correct right side
            ln_brt = brt / 2 # how thic the acids are
            rnd_x = start_x # x var to work with 
            pert = "fuck Biology" # var to save to know if already runed (need for riht side)
            
            for _ in range(2): # create lines on both sides

                rnd_y = start_y + (segm / 2) # starting y pos + a bit of space so it not ugly (:

                for i in range(segments): # create lines on one side

                    line = Line(start=[rnd_x, rnd_y, 0], end=[rnd_x + ln_brt, rnd_y, 0]) # create the line
                    
                    if pert == "fuck Biology": # left side
                        col = random.randint(0, len(colours) - 1) # coose random num for color 
                        colrs_save.append(col) # save this for right side
                        line.set_stroke(width=5, color=colours[col]) # use this num 
                        chromatid_insp_l.add(line) # add it to left side group

                    else: # right side
                        col_nm = colrs_save[i] # get the num for color
                        col = col_com[col_nm] # use it to get the color
                        line.set_stroke(width=5, color=col) # set the acid 
                        chromatid_insp_r.add(line) # add to right side
                    
                    self.play(Create(line), run_time=0.1) # show the acid

                    rnd_y += segm # move up by one segement
                
                rnd_x += ln_brt # move right by one acid
                pert += "fuck Biology again" # you know
                
            #grid() # pease-pudding tastes like cardboard :]

            if True: # checkpoint 2 
                names = ["Thymine", "Cytosine", "Guanine", "Adenine"] # acid names corspndg to colors from before 

                start_y_t = -1.5 # start names y 
                segm_t = 1 # segmt hight
                acids = Group() # group for names 

                for i in range(4): # for each acid
                    name = names[i] # get name
                    col = colours[i] # get clour

                    acid = Text(name, font_size=35, color=col) # set it up
                    acid.move_to([4, start_y_t, 0]) # move 

                    self.play(Write(acid)) # show
                    acids.add(acid) # add to group

                    start_y_t += segm_t # change y pos by segment
                
                self.wait(1) # have a good day :{}

                self.play(FadeOut(acids)) # fade all acids

            self.play(chromatid_insp_l.animate.shift([-1.5, 0, 0])) # move the left side to left

            self.wait(1) # dont learn konjuktivs in german +_+

            chromatid_insp_r_l = chromatid_insp_r.copy() # copy right half o ladder
            chromatid_insp_l_r = chromatid_insp_l.copy() # copy left side 

            self.play(chromatid_insp_r_l.animate.shift([-1.5, 0, 0]), # shift right to left 
                      chromatid_insp_l_r.animate.shift([1.5, 0, 0]),
                       run_time=2 # left to right to finish the chromatid
                      )
            
            self.wait(1) # jo jo jo

            self.play(FadeOut(chromatid_insp_l, chromatid_insp_l_r, chromatid_insp_r, chromatid_insp_r_l)) # fade the two chromatids out

            animations = []  # List to store all animations
            chromatids_copy = [] # list to save all right rotated copys
            for chromatd in chromatids: # change to X
                chomat_copy = chromatd.copy()  # Make a copy of each chromatid
                chromatids_copy.append(chomat_copy) # add to copy list
                # Append the animations for each chromatid and its copy to the list
                animations.append(chromatd.animate.rotate(-20 * DEGREES)) # move 20 dg to left
                animations.append(chomat_copy.animate.rotate(20 * DEGREES)) # same to right
            self.play(*animations) # Play all animations at the same time
            

            self.wait(1) # dont wait til tmr

            animations = []  # List to store all animations

            for chromatd_m in chromatids: 
                animations.append(chromatd_m.animate.move_to([-3, chromatd_m.get_y(), 0])) # move all chromatids to midle of zellkern on 0y

            for chromatd_m in chromatids_copy:
                animations.append(chromatd_m.animate.move_to([-3, chromatd_m.get_y(), 0])) # move all copy chromatids to midle of zellkern on 0y
            self.play(*animations) # move them actually 


            self.wait(1) # is 53 a prime?
            # methaphase =======================================================================================
            # create the pols

            pol_l = Circle(radius=0.25, color=LIGHT_GRAY, fill_opacity=1) # make the left pol
            pol_l.move_to([-5, 0, 0]) # move it
            
            pol_r = Circle(radius=0.25, color=LIGHT_GRAY, fill_opacity=1) # right one as well 
            pol_r.move_to([-1, 0, 0]) # guess what, you move it as well

            pols = VGroup(pol_l, pol_r) # group them ikd why 

            self.play(Create(pols)) # crete the stupid grou of pols

            
            self.play(FadeOut(zelle_kern, label_zelle_kern)) # fade out the zellkern

            # move all chromatids to sides
            # this took a lot time out of my life, so enjoy it 

            chrom_vg_r = VGroup() # group for right side movement :)
            chrom_vg_l = VGroup() # same for the left

            l_u = []
            l_d = []
            r_u = []
            r_d = []

            for chrom in chromatids:
                midpoint = (chrom.get_start() + chrom.get_end()) / 2 # calc the meet point

                # separat the old line into two new ones and add martini
                left_line = Line(start=chrom.get_start(), end=midpoint, color=chrom.get_color()) # line form strt to middle
                right_line = Line(start=midpoint, end=chrom.get_end(), color=chrom.get_color()) # from middle to end

                l_u.append(chrom.get_start())
                r_d.append(chrom.get_end())

                chrom_vg_l.add(left_line) # add left to left
                chrom_vg_r.add(right_line)# and right to right

                self.remove(chrom) # remove the old one (natural selction :P )
            
            for chrom in chromatids_copy: # same for the copys

                midpoint = (chrom.get_start() + chrom.get_end()) / 2 # still same

                right_line = Line(start=chrom.get_start(), end=midpoint, color=chrom.get_color()) # other side = other way around
                left_line = Line(start=midpoint, end=chrom.get_end(), color=chrom.get_color()) # bla bla

                r_u.append(chrom.get_start())
                l_d.append(chrom.get_end())

                chrom_vg_l.add(left_line) # you know (stil same)
                chrom_vg_r.add(right_line)

                self.remove(chrom)

            chrom_vg_l.set_z_index(5) # so it stays in the vorground
            chrom_vg_r.set_z_index(5)

            self.play(chrom_vg_l.animate.move_to([-1, 0, 0]), #left to right : right to left (idk why, but it works (: )
                      chrom_vg_r.animate.move_to([-5, 0, 0]),
                      run_time=1)
            
            self.play(Group(*self.mobjects).animate.move_to([0, 0, 0]), runtime=0.5) # move the scene back to 000

            zell_n_l = Circle(radius=2, fill_opacity=0.4, color=BLUE) # make the two new cells
            zell_n_l.move_to([2, 0, 0])

            zell_n_r = zell_n_l.copy()
            zell_n_r.move_to([-2, 0, 0])

            zelle_n = VGroup(zell_n_l, zell_n_r)

            self.play(ReplacementTransform(zelle_out, zelle_n), # transform from old to two new
                      FadeOut(pols))
            
            zellk_n_l = Circle(radius=1.2, fill_opacity=0.6, color=YELLOW) # make the kerns
            zellk_n_l.move_to([2, 0, 0])

            zellk_n_r = zellk_n_l.copy()
            zellk_n_r.move_to([-2, 0, 0])

            zellk_n = VGroup(zellk_n_l, zellk_n_r)
            
            zellen_txt = Text("Zellen", font_size=35) # correct the name
            zellen_txt.move_to([0, 2.5, 0])

            self.play(FadeIn(zellk_n), # fade in krene
                      Transform(zelle_txt, zellen_txt)) # text corr

            right_lin = VGroup()
            left_lin = VGroup()

            for i in range(15):
            
                rand_x, rand_y = tl.ran_pos_circle(radius=1.2, precision=10, y=-0) # chose random pos in circle

                while ((((rand_y + 0.5) ** 2) + ((rand_x) ** 2)) ** 0.5) >= 1.2 or ((((rand_y - 0.5) ** 2) + ((rand_x) ** 2)) ** 0.5) >= 1.2: # check if not sticking out
                    rand_x, rand_y = tl.ran_pos_circle(radius=1.4, precision=10, y=-0)

                srt = [rand_x + 2, rand_y + 0.5, 0]
                ed = [rand_x + 2, rand_y - 0.5, 0]
                line = Line(start=srt, end=ed)

                line.set_stroke(width=5,  # changes to lines
                                           color=colors[i % len(colors)], # choose always diferent color 
                                           opacity=(random.randint(50, 100) / 100))

                right_lin.add(line)

            for i in range(15):
            
                rand_x, rand_y = tl.ran_pos_circle(radius=1.2, precision=10, y=-0) # chose random pos in circle

                while ((((rand_y + 0.5) ** 2) + ((rand_x) ** 2)) ** 0.5) >= 1.2 or ((((rand_y - 0.5) ** 2) + ((rand_x) ** 2)) ** 0.5) >= 1.2: # check if not sticking out
                    rand_x, rand_y = tl.ran_pos_circle(radius=1.4, precision=10, y=-0)

                srt = [rand_x - 2, rand_y + 0.5, 0]
                ed = [rand_x - 2, rand_y - 0.5, 0]
                line = Line(start=srt, end=ed)

                line.set_stroke(width=5,  # changes to lines
                                           color=colors[i % len(colors)], # choose always diferent color 
                                           opacity=(random.randint(50, 100) / 100))

                left_lin.add(line)


            self.play(Transform(chrom_vg_l, right_lin), # left/right_line
                    Transform(chrom_vg_r, left_lin)     # zellk_n_r/l 
                    )                                   # zell_n_l/r

            self.wait(3) # think about your life

        # ========================================================================================----

        
        def intro_meiose(): 
            title = Text("Meiose", font_size=50)
            self.play(Write(title))
            self.wait(1.5)
            self.play(FadeOut(title))

        def meiose():

            if True: # checkpoint 1 : lines in kern
                zelle_txt = Text("Zelle", font_size=35)
                zelle_txt.move_to([0,3, 0])

                zelle_out = Circle(radius=2.5, color=BLUE, fill_opacity=0.4) # create zelle
                zelle_out.move_to([0, 0 , 0])

                zelle_kern = Circle(radius=1.5, color=YELLOW, fill_opacity=0.6) # zellen kern
                zelle_kern.move_to([0, 0 , 0])

                label_zelle_kern = Text("Zellenkern", font_size=24).next_to(zelle_kern, UP) # create the label
                

                self.play(Write(zelle_txt), # show zelle and label
                          Create(zelle_out))


                self.wait(0.5)

                self.play(Create(zelle_kern), # show kern and label
                          Write(label_zelle_kern))


                self.wait(0.5)
                # animate chromatids
                
                colors = [RED, RED_A, RED_B, RED_C, RED_D, RED_E] # cloors for chromatids in kern
                chromatids = [] # list for saving all original chromatids

                

                for i in range(15): # small chrms in bckg

                    chromatid_b = VMobject() 

                    rand_x, rand_y = tl.ran_pos_circle(radius=1.4, precision=10, y=-0) # chose random pos in circle

                    while ((((rand_y + 0.5) ** 2) + ((rand_x) ** 2)) ** 0.5) >= 1.4 or ((((rand_y - 0.5) ** 2) + ((rand_x) ** 2)) ** 0.5) >= 1.4: # check if not sticking out
                        rand_x, rand_y = tl.ran_pos_circle(radius=1.4, precision=10, y=-0) # chose random pos in circle


                    start_chrom = [rand_x, rand_y + 0.5, 0] # create line from one point
                    end_chrom = [rand_x, rand_y - 0.5, 0]

                    chromatid_b.set_points_as_corners([start_chrom, end_chrom]) # create the line
                    
                    chromatid_b.set_stroke(width=5,  # changes to lines
                                           color=colors[i % len(colors)], # choose always diferent color 
                                           opacity=(random.randint(50, 100) / 100)) # random opacity

                    chromatids.append(chromatid_b) # add this chromatid to originals
    
                    self.play(Create(chromatid_b),  run_time=0.1) # show this chromatid

                self.wait(1)


                chromatid_l = VMobject()
                chromatid_l.set_points_as_corners([[-0.2, 1, 0], [-0.2, -1, 0]])
                chromatid_l.set_stroke(width=10, color=DARK_BLUE)
                chromatid_l.set_z_index(16)


                chromatid_r = VMobject()
                chromatid_r.set_points_as_corners([[0.2, 1, 0], [0.2, -1, 0]])
                chromatid_r.set_stroke(width=10, color=PURPLE)
                chromatid_r.set_z_index(16)


                self.play(Create(chromatid_l),
                  Create(chromatid_r),
                  run_time=0.2)
                
                animations = []  # List to store all animations
                chromatids_copy = [] # list to save all right rotated copys
                for chromatd in chromatids: # change to X
                    chomat_copy = chromatd.copy()  # Make a copy of each chromatid
                    chromatids_copy.append(chomat_copy) # add to copy list
                    # Append the animations for each chromatid and its copy to the list
                    animations.append(chromatd.animate.rotate(-25 * DEGREES)) # move 20 dg to left
                    animations.append(chomat_copy.animate.rotate(25 * DEGREES)) # same to right

                chromatid_r_r = chromatid_r.copy()
                chromatid_l_r = chromatid_l.copy()

                animations.append(chromatid_l.animate.rotate(-25 * DEGREES))
                animations.append(chromatid_r.animate.rotate(-25 * DEGREES))
                animations.append(chromatid_l_r.animate.rotate(25 * DEGREES))
                animations.append(chromatid_r_r.animate.rotate(25 * DEGREES))


                self.play(*animations) # Play all animations at the same time

                self.wait(1)

                self.remove(zelle_txt)

                zoom(3)

                # welcome to the dark side
                # nothing is cler down here
                # but it works

                
                point_u = Circle(radius=0.1, color=RED_E, fill_opacity=1).set_z_index(18)
                point_d = Circle(radius=0.1, color=RED_E, fill_opacity=1).set_z_index(18)

                point_u.move_to([0, 1.3, 0])
                point_d.move_to([0, -1.3, 0])


                self.play(Create(point_d),
                          Create(point_u))


                llu = Line(start=chromatid_l.get_start(), end=[0, 1.2, 0]).set_stroke(color=DARK_BLUE, width=10).set_z_index(17)
                lld = Line(start=[0, 1.2, 0], end=chromatid_l.get_end()).set_stroke(color=DARK_BLUE, width=10).set_z_index(17)
                lru = Line(start=chromatid_l_r.get_start(), end=[0, -1.2, 0]).set_stroke(color=DARK_BLUE, width=10).set_z_index(17)
                lrd = Line(start=[0, -1.2, 0], end=chromatid_l_r.get_end()).set_stroke(color=DARK_BLUE, width=10).set_z_index(17)
                rru = Line(start=chromatid_r_r.get_start(), end=[0, 1.2, 0]).set_stroke(color=PURPLE, width=10).set_z_index(17)
                rrd = Line(start=[0, 1.2, 0], end=chromatid_r_r.get_end()).set_stroke(color=PURPLE, width=10).set_z_index(17)
                rlu = Line(start=chromatid_r.get_start(), end=[0, -1.2, 0]).set_stroke(color=PURPLE, width=10).set_z_index(17)
                rld = Line(start=[0, -1.2, 0], end=chromatid_r.get_end()).set_stroke(color=PURPLE, width=10).set_z_index(17)

                rru_n = llu.copy().set_stroke(color=PURPLE)
                llu_n = rru.copy().set_stroke(color=DARK_BLUE)
                lrd_n = rld.copy().set_stroke(color=DARK_BLUE)
                rld_n = lrd.copy().set_stroke(color=PURPLE)


                new_chrom = VGroup(llu, lld, lru, lrd, rru, rrd, rlu, rld)
                old_crom = VGroup(chromatid_l, chromatid_r, chromatid_l_r, chromatid_r_r)

                self.play(FadeTransform(old_crom, new_chrom))

                self.play(ReplacementTransform(rru, rru_n),
                          ReplacementTransform(llu, llu_n))
                self.play(
                          ReplacementTransform(rld, rld_n),
                    	  ReplacementTransform(lrd, lrd_n))
                zoom(1/3)

                self.play(FadeOut(zelle_kern),
                          FadeOut(point_d),
                          FadeOut(point_u),
                          FadeOut(label_zelle_kern))

                animations =[]
                side = 1
                rnd_l = tl
                
                for chrom_copy, chrom in zip(chromatids_copy, chromatids):
                    side *= -1
                    chromatid = VGroup(chrom_copy, chrom)
                    chromatid.set_z_index(16)

                    rnd_x = random.choice(tl.random_list)
                    rnd_y = random.choice(tl.random_list)
                    

                    if side == 1:
                        x = -2 + (rnd_x / 10)
                        y = rnd_y / 10
                        pos = [x, y, 0]
                    else:
                        x = 2 + (rnd_x / 10)
                        y = rnd_y / 10 
                        pos = [x, y, 0]

                    animations.append(chromatid.animate.move_to(pos))

                chrom_r = VGroup(rrd, rlu, lrd_n, llu_n)  
                chrom_l = VGroup(lld, lru, rld_n, rru_n)  
 
                animations.append(chrom_r.animate.move_to([2, 0, 0]))
                animations.append(chrom_l.animate.move_to([-2, 0, 0]))

                self.play(*animations)
                    
                zell_n_l = Circle(radius=2, fill_opacity=0.4, color=BLUE) # make the two new cells
                zell_n_l.move_to([2, 0, 0])

                zell_n_r = zell_n_l.copy()
                zell_n_r.move_to([-2, 0, 0])

                zelle_n = VGroup(zell_n_l, zell_n_r)

                self.play(ReplacementTransform(zelle_out, zelle_n))
                
                zellk_n_l = Circle(radius=1.2, fill_opacity=0.6, color=YELLOW_C) # make the kerns
                zellk_n_l.move_to([2, 0, 0])

                zellk_n_r = zellk_n_l.copy()
                zellk_n_r.move_to([-2, 0, 0])

                zellk_n = VGroup(zellk_n_l, zellk_n_r)
            

                self.play(FadeIn(zellk_n)) # text corr

                self.wait(3)

        # main code structure:        
        intro_gen()
        intro_mitose()
        mitose()
        self.clear()
        intro_meiose()
        meiose()
