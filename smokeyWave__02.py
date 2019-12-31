#                                    __                                                                             
#                                   |  \                                                                            
#   _______  ______ ____    ______  | $$   __   ______   __    __        __   __   __   ______  __     __   ______  
#  /       \|      \    \  /      \ | $$  /  \ /      \ |  \  |  \      |  \ |  \ |  \ |      \|  \   /  \ /      \ 
# |  $$$$$$$| $$$$$$\$$$$\|  $$$$$$\| $$_/  $$|  $$$$$$\| $$  | $$      | $$ | $$ | $$  \$$$$$$\\$$\ /  $$|  $$$$$$\
#  \$$    \ | $$ | $$ | $$| $$  | $$| $$   $$ | $$    $$| $$  | $$      | $$ | $$ | $$ /      $$ \$$\  $$ | $$    $$
#  _\$$$$$$\| $$ | $$ | $$| $$__/ $$| $$$$$$\ | $$$$$$$$| $$__/ $$      | $$_/ $$_/ $$|  $$$$$$$  \$$ $$  | $$$$$$$$
# |       $$| $$ | $$ | $$ \$$    $$| $$  \$$\ \$$     \ \$$    $$       \$$   $$   $$ \$$    $$   \$$$    \$$     \
#  \$$$$$$$  \$$  \$$  \$$  \$$$$$$  \$$   \$$  \$$$$$$$ _\$$$$$$$        \$$$$$\$$$$   \$$$$$$$    \$      \$$$$$$$
#                                                       |  \__| $$                                                  
#                                                        \$$    $$                                                  
#                                                         \$$$$$$                                                   
# by Benjamin Santiago
# little looping animation that displays a colorful smokey
# "tail" that moves in a sinusoidal fashion 
# this sketches uses the typeface Gooper by Very Cool Studio
# (variable names and comments expanded for clarity)

#parameters to change
#total animation frames
frames    = 100
#vertical space between iterations
y__space   = 6

#------------------------------------------------------------------
for frame in range(frames):
    #canvas size and frame rate
    newPage(1000,1000)
    frameDuration(1/30)
    
    #bg rectangle
    fill(.7, .4, .7)
    rect(0,0,width(),height())
    
    #prewiggle calculations
    #gimme a number betwixt 0 - 1
    frames__normalized = frame/frames
    
    #shift text and then move sinusoidally
    offset__x = width()/2 - 400
    offset__x += sin(frames__normalized*pi*4) * 100
    
    #create an array with a "gradient of colors"
    #-------------------------------------------
    #steps should be a multiple of 2 so it loops
    color__steps = int(frames/4)
    colors = []
    for color in range(color__steps):
        #0 --> 1
        color__normalized = color/color__steps
        #color "angle" for trig functions
        color__normalized = color__normalized*pi*2
        #add color to the end of the array
        colors.append((.3+abs(sin(color__normalized)*.4), 0, .3 + abs(cos(color__normalized)*.4)))
    
    #wiggleator
    #------------------------------------------------------------------
    for repeats in range(0, height(), y__space):
        #calculations
        #--------------------------------------
        #0 --> 1
        repeats__normalized = repeats/height()
        #add shift based on frame
        repeats__and__frames__normalized = repeats__normalized + frames__normalized
        #sinusoidal move
        offset__x__angle = sin(repeats__and__frames__normalized*pi*8) * 10
        #compensate for x-shift from sine wave
        offset__x -= offset__x__angle
        #y shift
        offset__y = height() - repeats
        offset__y += 40
        
        #make color always index the array
        color = int((frame + repeats/y__space)%color__steps)
        
        #set fill color
        if repeats + y__space > height():
            fill(.2, .1, .8, 1)
        else:
            fill(colors[color][0], colors[color][1], colors[color][2], 1)
            
        #text
        font("Gooper0.4-Super", 300)
        text("2020", (offset__x, offset__y))
    #------------------------------------------------------------------
    
#------------------------------------------------------------------
#we done!

#image sequence
#saveImage("~/Desktop/smokeyWave__.png", multipage="true")

#animated gif
#saveImage("wave__a__.gif")