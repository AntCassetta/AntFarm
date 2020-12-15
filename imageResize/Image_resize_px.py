
import os
import sys
from PIL import Image

def resize(folder, fileName, factor):
    filePath = os.path.join(folder, fileName)
    im = Image.open(filePath)
    w, h  = im.size
    newW = factor
    newH = factor
    newIm = im.resize((int(newW), int(newH)), Image.ANTIALIAS)
    # i am saving a copy, you can overrider orginal, or save to other folder
    newIm.save(targetDir + "/" + fileName)

def bulkResize(imageFolder, factor):
    imgExts = ["png", "bmp", "jpg", "gif", "jpeg"]
    for fileName in os.listdir(imageFolder):
        ext = fileName[-3:].lower()
        if ext not in imgExts:
            continue

        resize(imageFolder, fileName, factor)

targetDir = "";
if __name__ == "__main__":
    imageFolder=sys.argv[1] # first arg is path to image folder
    targetDir = imageFolder + "/resized"
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
    newSize=float(sys.argv[2])# 2nd is resize
    bulkResize(imageFolder, newSize)