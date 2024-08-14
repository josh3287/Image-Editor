from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
path0ut = '/editedImgs'


for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)
    clean_name = os.path.splitext(filename) [0]
    
    edit.save(f'.{path0ut}/{clean_name}_edited.jpg')