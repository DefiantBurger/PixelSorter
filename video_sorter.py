import os
import shutil

import cv2

from image_sorter import sortImage


def sortVideo(input_file: str, ofp: str, verbose: bool = False):
    shutil.rmtree('frames')
    os.mkdir('frames')

    shutil.rmtree('created_frames')
    os.mkdir('created_frames')

    vidcap = cv2.VideoCapture(input_file)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("frames/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        if verbose:
            print('Read frame: ', count)
        count += 1

    count = 0
    for f in os.listdir('frames'):
        filename = os.path.join('frames', f)
        if not os.path.isfile(filename):
            continue

        sortImage(filename, ofp, returns=True, verbose=False).save(f'created_frames/{f}')
        if verbose:
            print('Sorted frame: ', count)
        count += 1

    size = (0, 0)
    img_dict = {}
    for f in os.listdir('created_frames'):
        filename = 'created_frames/' + f
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_dict[f] = img

    out = cv2.VideoWriter(ofp, cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

    key_list = sorted(img_dict.keys(), key=lambda k_: int(k_.removeprefix('frame').split(".")[0]))
    new_img_dict = {}
    for k in key_list:
        new_img_dict[k] = img_dict[k]

    for i in new_img_dict:
        out.write(new_img_dict[i])
    out.release()
