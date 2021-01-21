import os
from PIL import Image
import glob
import numpy as np
from utils import make_folder
import argparse

color_list =           [[0, 0, 0], [204, 0, 0], [76, 153, 0], [204, 204, 0], [51, 51, 255], [204, 0, 204], [0, 255, 255], [255, 204, 204], [102, 51, 0], [255, 0, 0], [102, 204, 0], [255, 255, 0], 
[0, 0, 153], [0, 0, 204], [255, 51, 153], [0, 204, 204], [0, 51, 0], [255, 153, 51], [0, 204, 0]]

color_list_symmetric = [[0, 0, 0], [204, 0, 0], [76, 153, 0], [204, 204, 0], [204, 0, 204], [204, 0, 204], [255, 204, 204], [255, 204, 204], [102, 51, 0], [102, 51, 0], [102, 204, 0], [255, 255, 0], 
[0, 0, 153], [0, 0, 204], [255, 51, 153], [0, 204, 204], [0, 51, 0], [255, 153, 51], [0, 204, 0]]


parser = argparse.ArgumentParser()

parser.add_argument("--input", "-i", default="CelebAMask-HQ-mask", help="The input folder containing labels")
parser.add_argument("--output", "-o", default="CelebAMask-HQ-mask-color", help='The output folder to store color images')
parser.add_argument("--symmetric", action='store_true', help="Symmetric coloring")

args = parser.parse_args()


folder_base = args.input
folder_save = args.output
if args.symmetric:
    coloring = color_list_symmetric
else:
    coloring = color_list
    

img_num = 30000

make_folder(folder_save)

for k in range(img_num):
    filename = os.path.join(folder_base, str(k) + '.png')
    if (os.path.exists(filename)):
        im_base = np.zeros((512, 512, 3))
        im = Image.open(filename)
        im = np.array(im)
        for idx, color in enumerate(coloring):
            im_base[im == idx] = color
    filename_save = os.path.join(folder_save, str(k) + '.png')
    result = Image.fromarray((im_base).astype(np.uint8))
    print (filename_save)
    result.save(filename_save)

