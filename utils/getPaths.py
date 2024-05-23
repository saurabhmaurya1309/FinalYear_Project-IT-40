# Importing packages
import os

# Defining the different image types
imageTypes = (".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp")


def listImages(basePath, contains=None):
    return listFiles(basePath, validExts=imageTypes, contains=contains)


def listFiles(basePath, validExts=None, contains=None):
    for (baseDir, dirNames, filenames) in os.walk(basePath):
        for filename in filenames:
            # Ignore the file if the string contains is not none and the filename does not contain
            # the string supplied
            if contains is not None and filename.find(contains) == -1:
                continue

            # Extracting the file extension
            fileExt = filename[filename.rfind("."):].lower()

            # Checking to see if it is an image and needs to be processed
            if validExts is None or fileExt.endswith(validExts):
                # Construct the path to the image and then yield it
                imagePath = os.path.join(baseDir, filename)
                yield imagePath
