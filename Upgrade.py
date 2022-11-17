import Finder as f
import ImageManager as im
import Clicker
import time
import Resources as res

res_threshold = 3000000

def upgrade():

    (gold,elixir) = res.get_resources()

    if(gold < res_threshold and elixir < res_threshold):
        return

    n = number_of_builders()
    
    open_buildermenu()

    if(n > 1):
        upgrade_recommended(gold, elixir)
    else:
        upgrade_wall(gold,elixir)


def number_of_builders():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("builder"), 0.7)
    image = im.get_Screenshot(rects[0][0]+50, rects[0][1]-10, 130, 70)
    image = f.filter_pixels(image, 255, 255, 255)
    image = im.resize(image, 500)
    s = f.read_text(image)
    print("builders: " + s)
    if(s[0] == "V" or s[0] == "v" or s[0] == "/"):
        return 1
    return f.text_to_Int(s[0])

def open_buildermenu():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("builder"), 0.7)
    Clicker.click(rects)
    Clicker.drag_top_builder_menu()

def upgrade_wall(gold, elixir):
    find_upgrade("Mauer")
    execute_upgrade(gold, elixir)

def upgrade_recommended(gold, elixir):
    if gold > elixir:
        rects = f.find_image(im.get_Screenshot(440,140,655,615), im.get_image("upgrade_gold"), 0.8)
        if(len(rects) == 0):
            rects = f.find_image(im.get_Screenshot(440,140,655,615), im.get_image("upgrade_elixir"), 0.8)
    else:
        rects = f.find_image(im.get_Screenshot(440,140,655,615), im.get_image("upgrade_elixir"), 0.8)
        if(len(rects) == 0):
            rects = f.find_image(im.get_Screenshot(440,140,655,615), im.get_image("upgrade_gold"), 0.8) 
    Clicker.click_xy(rects[0][0] + 440,rects[0][1] + 140)       #because relative to 0,0 not to the corner of the menu
    execute_upgrade(gold, elixir)
    pass

def find_upgrade(obj):
    # 460 150
    # 900 150
    # height = 60 | 750 -height
    box_x1 = 460
    box_x2 = 900
    height = 60
    width = box_x2 - box_x1
    found = False

    while(not found):
        for i in range(30):
            x1 = box_x1
            y1 = 150 + (i*20)
            image = im.get_Screenshot(x1,y1, width, height)
            s = f.read_text(image)
            if(obj in s):
                found = True
                print("found!")
                Clicker.click_xy(x1 + 20, y1 + 30)
                break
        if(not found):
            Clicker.drag_down_builder_menu()

def execute_upgrade(gold, elixir):

    rects = f.find_image(im.get_fullScreenshot(), im.get_image("upgrade_hammer"), 0.9)
    
    
    if(len(rects) == 2):
        
        if(rects[0][0]<rects[1][0]):
            g = rects[0]
            e = rects[1]
        else:
            g = rects[1]
            e = rects[0]
        if(gold > elixir):
            Clicker.click_xy(g[0],g[1])
        else:
            Clicker.click_xy(e[0],e[1])
    else:
        Clicker.click(rects)
    time.sleep(0.5)

    Clicker.click_xy(970, 950)


    