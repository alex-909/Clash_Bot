import Finder as f
import ImageManager as im
import Clicker


def get_resources():
    rectsG = f.find_image(im.get_fullScreenshot(),im.get_image("gold"),0.8)
    imageG = im.get_Screenshot(rectsG[0][0]-250,rectsG[0][1],250,55)
    imageG = f.filter_pixels(imageG, 255, 255, 255)
    imageG = im.resize(imageG, 300)
    gold = f.read_text(imageG)

    rectsE = f.find_image(im.get_fullScreenshot(),im.get_image("elixir"),0.8)
    imageE = im.get_Screenshot(rectsE[0][0]-200,rectsE[0][1] + 1,175,55)
    imageE = f.filter_pixels(imageE, 255, 255, 255)
    imageE = im.resize(imageE, 300)
    elixir = f.read_text(imageE)

    return(f.text_to_Int(gold),f.text_to_Int(elixir))

def collect_res():

    Clicker.drag_top_right()

    rectsG = f.find_image(im.get_fullScreenshot(), im.get_image("collect_gold"), 0.8)
    Clicker.click(rectsG)

    rectsE = f.find_image(im.get_fullScreenshot(), im.get_image("collect_elixir"), 0.8)
    Clicker.click(rectsE)

    rectsDe = f.find_image(im.get_fullScreenshot(), im.get_image("collect_darkelixir"), 0.8)
    Clicker.click(rectsDe)

def get_won_res():

    #region gold
    rects = f.find_image(im.get_Screenshot(0,0,1350,1080), im.get_image("result_gold"), 0.8)
    image = im.get_Screenshot(rects[0][0] - 300 , rects[0][1] - 10, 280, 70)
    image = f.filter_pixels(image, 255, 255, 255)
    gold = f.read_text(image)
    gold = f.text_to_Int(gold)
    #endregion

    #region elixir
    rects = f.find_image(im.get_Screenshot(0,0,1350,1080), im.get_image("result_elixir"), 0.8)
    image = im.get_Screenshot(rects[0][0] - 300 , rects[0][1] - 20, 280, 70)
    image = f.filter_pixels(image, 255, 255, 255)
    elixir = f.read_text(image)
    elixir = f.text_to_Int(elixir)
    #endregion

    #region dark_elixir
    rects = f.find_image(im.get_Screenshot(0,0,1350,1080), im.get_image("result_dark_elixir"), 0.8)
    if(len(rects) > 0):
        image = im.get_Screenshot(rects[0][0] - 300 , rects[0][1] - 16, 280, 70)
        image = f.filter_pixels(image, 255, 255, 255)
        dark_elixir = f.read_text(image)
        dark_elixir = f.text_to_Int(dark_elixir)
    else:
        dark_elixir = 0
    #endregion

    return(gold, elixir, dark_elixir)