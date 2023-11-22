from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

import time

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("WE HATE BLOAT", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("TERMINAL FOR THE WIN!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])



def pixel_print_single(screen:Screen):
    screen.print_at("T",20,20,1)
    screen.refresh()
    time.sleep(3)
    print(screen.get_event())



# def pixel_print(screen:Screen):
#     for i in range(0,1):
#         screen.print_at("#",20,20,4)
#         screen.refresh()
#         time.sleep(1)
#         screen.print_at("####",20,20,1)
#         screen.refresh()
#         time.sleep(1)



# Screen.wrapper(pixel_print)
#Screen.wrapper(pixel_print_single)
Screen.wrapper(demo)