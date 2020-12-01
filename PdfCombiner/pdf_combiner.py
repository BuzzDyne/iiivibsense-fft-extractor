import os
import shutil
import re
from os.path import isfile, join
from PIL import Image

from constansts import data_paths as DP

class PDFCombiner:
    # Get all image directories
    # Process Sensor Dir
        # Get ref to images in each dir
        # Combine images to a pdf
        # Archive processed images to another folder

    def getImgDirectories(self):
        return [f'{DP.PNG_PATH}/{x}' for x in os.listdir(DP.PNG_PATH)]

    def processSensorDirs(self):

        def cleanseStrForPDFName(x):
            y = x.split('/')[-2:]
            return f"{y[0]}_{y[1]}"

        def combineImgs(listOfImgPaths, targetFileName):
            listOfImg = []
            for imgPath in listOfImgPaths:
                listOfImg.append(Image.open(imgPath))
            
            # Get Max Width and Height
            listOfMeasurements = [x.size for x in listOfImg]
            maxWidth    = max([x[0] for x in listOfMeasurements])
            maxHeight   = max([x[1] for x in listOfMeasurements])

            # Create Canvas
            new_image = Image.new('RGB', (maxWidth, maxHeight*len(listOfImg)))

            # Put Images
            i=0
            for img in listOfImg:
                new_image.paste(img, (0, maxHeight*i))
                i = i+1

            # Save img
            targetFileName = targetFileName[:-3] + 'pdf'
            new_image.save(f'{DP.PDF_TARGET_DIR_PATH}/{targetFileName}')

        def archiveDir(sourceDir):
            dirName = sourceDir.split('/')[-1]
            targetDir = f"{DP.PNG_ARCHIVE_PATH}/{dirName}"

            if os.path.isdir(targetDir):    # Folder already exists
                # Move sourceDir content to target
                # Delete sourceDir
                file_names = os.listdir(sourceDir)
                for f in file_names:
                    shutil.move(f'{sourceDir}/{f}', targetDir)
                os.rmdir(sourceDir)
            else:                           # Folder doesn't exist yet
                # Move sourceDir
                shutil.move(sourceDir, DP.PNG_ARCHIVE_PATH)

        # Combine Imgs to PDF
        for directory in self.sensorDirs:
            fName = directory.split('/')[-1]
            print(f"Splicing {fName}... ", end='')

            listOfImgs = []
            for f in os.listdir(directory):
                listOfImgs.append(f'{directory}/{f}')
            combineImgs(listOfImgs, cleanseStrForPDFName(listOfImgs[-1]))
            print("Done!\n", end='')

            # Dir processed, archiving
            print(f"Archiving {fName}... ", end='')
            archiveDir(directory)
            print("Done!\n", end='')
            



    def __init__(self):
        self.sensorDirs = self.getImgDirectories()

        self.processSensorDirs()
    