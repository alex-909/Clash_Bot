import Finder as f
import ImageManager as im
import Clicker
import pyscreenshot
import time

def upgrade():
    n = number_of_builders()
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("builder"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])
    Clicker.drag_top_builder_menu()
    if(n > 1):
        pass
    else:
        find_wall()
    gold = 1_000_000
    elixir = 500_000
    execute_upgrade(gold, elixir)

def execute_upgrade(gold, elixir):
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("upgrade_hammer"), 0.9)
    if(len(rects) == 2):
        """
        if(rects[0][0] > rects[0][1]):
            temp = rects[0]
            rects[0] = rects[1]
            rects[1] = temp
        """
        
        if(gold > elixir):
            Clicker.click(rects[0][0], rects[0][1])
        else:
            Clicker.click(rects[1][0], rects[1][1])
    else:
        Clicker.click(rects[0][0], rects[0][1])
    time.sleep(0.5)
    #rects = f.find_image(im.get_fullScreenshot(), im.get_image("confirm_upgrade"), 0.7)
    #Clicker.click(rects[0][0], rects[0][1])
    Clicker.click(970, 950)



def find_wall():
    # 460 150
    # 900 150
    # height = 60 | 750 -height
    box_x1 = 460
    box_x2 = 900
    box_y1 = 150
    box_y2 = 750
    height = 60
    width = box_x2 - box_x1
    wall_found = False

    while(not wall_found):
        for i in range(30):
            x1 = box_x1
            y1 = 150 + (i*20)
            image = im.get_Screenshot(x1,y1, width, height)
            img = pyscreenshot.grab((x1,y1,width+x1,height+y1))
            #img.show()
            s = f.read_text(image)
            print(s)
            if("Mauer" in s):
                wall_found = True
                print("found!")
                Clicker.click(x1 + 20, y1 + 30)
                break
        if(not wall_found):
            Clicker.drag_down_builder_menu()

def number_of_builders():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("builder"), 0.7)
    image = im.get_Screenshot(rects[0][0]+60, rects[0][1], 110, 50)
    #image = pyscreenshot.grab((rects[0][0]+60, rects[0][1], rects[0][0]+170, rects[0][1] +50))
    s = f.read_text(image)
    return int(s[0])


def upgrade_wall():
    pass