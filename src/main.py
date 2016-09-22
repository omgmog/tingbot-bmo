import tingbot
from tingbot import *
import os, fnmatch

faceindex = 1
totalfaces = len(fnmatch.filter(os.listdir('img/'), 'bmo*.png'))

@left_button.press
@right_button.press
@midleft_button.press
@midright_button.press
def changeFace():
    global faceindex
    if faceindex > totalfaces:
        faceindex = 1
    screen.image('img/bmo%d.png' % faceindex)
    faceindex += 1

tingbot.run()
