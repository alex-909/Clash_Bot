import Finder as f
import ImageManager as im
import Clicker


def get_resources():
    rectsG = f.find_image(im.get_fullScreenshot(),im.get_image("gold"),0.8)
    imageG = im.get_Screenshot(rectsG[0][0]-250,rectsG[0][1],250,55)
    gold = f.read_text(imageG)

    rectsE = f.find_image(im.get_fullScreenshot(),im.get_image("elixir"),0.8)
    imageE = im.get_Screenshot(rectsE[0][0]-200,rectsE[0][1] + 1,175,32)
    elixir = f.read_text(imageE)

    resources = [gold,elixir]

    return resources

def collect_res():
    rectsG = f.find_image(im.get_fullScreenshot(), im.get_image("collect_gold"), 0.8)
    Clicker.click(rectsG)

    rectsE = f.find_image(im.get_fullScreenshot(), im.get_image("collect_elixir"), 0.8)
    Clicker.click(rectsE)

    rectsDe = f.find_image(im.get_fullScreenshot(), im.get_image("collect_darkelixir"), 0.8)
    Clicker.click(rectsDe)
