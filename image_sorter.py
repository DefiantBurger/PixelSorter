import numpy as np
from PIL import Image


def vprint(text, verbose: bool):
    if verbose:
        print(text)


def sortImage(ifp: str, ofp: str, returns: bool = False, verbose: bool = False) -> Image:
    img = Image.open(ifp).convert('RGB')
    size = img.size

    vprint("Started loading image data...", verbose)
    vals = [[img.getpixel((x, y)) for y in range(size[1])] for x in range(size[0])]
    vprint("Finished loading image data...", verbose)

    vprint("Started generating image data...", verbose)
    arr = np.array([[[0, 0, 0] for _ in range(size[0])] for _ in range(size[1])], dtype=np.uint8)
    for x in range(size[0]):
        vals[x].sort(key=lambda v: sum(v))
        for y in range(size[1]):
            arr[y][x] = vals[x][y]
    new = Image.fromarray(arr)

    vprint("Finished generating image data...", verbose)

    if returns:
        return new
    else:
        new.save(ofp)
