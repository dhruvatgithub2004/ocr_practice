from PIL import Image

im_file = "data/page_01.jpg"

im = Image.open(im_file)
im.show()