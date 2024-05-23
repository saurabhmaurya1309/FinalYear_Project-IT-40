# Importing packages
import config
import getPaths
import shutil
import random
import os


# Get the paths of all input images in the original input directory and then shuffling them
allImagePaths = list(getPaths.listImages(config.INITIAL_INPUT_PATH))
random.seed(42)
random.shuffle(allImagePaths)

# Considering around 10% of the images
print(len(allImagePaths))
imagePaths = allImagePaths[0:20000]
print(len(allImagePaths))

# computing the training and testing split
i = int(len(allImagePaths) * config.TRAIN_SPLIT)
trainPaths = allImagePaths[:i]
testPaths = allImagePaths[i:]

# Further splitting part of the training data for validation
i = int(len(trainPaths) * config.VAL_SPLIT)
valPaths = trainPaths[:i]
trainPaths = trainPaths[i:]

# Defining the datasets which will be built in the final input folder
datasets = [
    ("training", config.TRAIN_PATH, trainPaths),
    ("validation", config.VAL_PATH, valPaths),
    ("testing", config.TEST_PATH, testPaths)
]

# Iterating over the datasets
for (dSType, basePath, allImagePaths) in datasets:
    print("Making '{}' split".format(dSType))
    if not os.path.exists(basePath):
        print("'Creating {}' directory".format(basePath))
        os.makedirs(basePath)
    # Looping over the image paths
    for inputPath in allImagePaths:
        # Extracting the filename of the input image
        # Extracting class label ("0" for "Benign" and "1" for "Malignant")
        filename = inputPath.split(os.path.sep)[-1]
        label = filename[-5:-4]
        # Making the path to form the label directory
        labelPath = os.path.sep.join([basePath, label])
        if not os.path.exists(labelPath):
            print("'creating {}' directory".format(labelPath))
            os.makedirs(labelPath)
        # Creating the path to the destination image and then copying it
        finalPath = os.path.sep.join([labelPath, filename])
        shutil.copy2(inputPath, finalPath)