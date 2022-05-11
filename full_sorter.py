from image_sorter import sortImage
from video_sorter import sortVideo


def sortAny(ifp: str, ofp: str):
    if ifp.endswith(".jpg") or ifp.endswith(".jpeg") or ifp.endswith(".png"):
        sortImage(ifp, ofp, verbose=True)
    elif ifp.endswith(".mp4"):
        sortVideo(ifp, ofp, verbose=True)
    else:
        print("Invalid file type!")


if __name__ == "__main__":
    input_file = 'input/rainbow_eyes_cat.jpeg'
    output_file = 'output/rainbow_eyes_cat.jpeg'
    sortAny(input_file, output_file)
