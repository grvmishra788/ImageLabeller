import glob


def getImageList(src):
    img_list = []
    for name in glob.glob(src):
        img_list.append(name)
    return img_list
