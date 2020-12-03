import os
import shutil
import re
from os.path import isfile, join
from PIL import Image

from constansts import data_paths as DP
from PdfCombiner.image_set_model import ImageSet

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
            fftImgRegex = r'([0-9]+)-([0-9]+)-([0-9]+)_([0-9]+)-([0-9]+)-([0-9]+).png'

            listOfImgSets = []
            
            # Get Reference to all
            for imgPath in listOfImgPaths:
                if(re.search(fftImgRegex, imgPath) is not None): #is FFT Image
                    fftImg = Image.open(imgPath)

                    # try finding fft's faultImg
                    faultPath = imgPath[:-4] + '_0_faults.png'
                    try:
                        faultImg = Image.open(faultPath)
                    except FileNotFoundError:
                        faultImg = None
                        print(f"{targetFileName}'s faultImg is not found'")
                    
                    listOfImgSets.append(ImageSet(fftImg, faultImg))
            
            # Get Max Width and Height
            maxHeight       = max([i.getMaxHeight() for i in listOfImgSets])
            fftMaxWidth     = max([i.getFftWidth() for i in listOfImgSets])
            faultMaxWidth   = max([i.getFaultsWidth() for i in listOfImgSets if i.getFaultsWidth() is not None])

            # Create Canvas
            new_image = Image.new('RGB', (fftMaxWidth+faultMaxWidth, maxHeight*len(listOfImgSets)))

            # Put Images
            i=0
            for imgSet in listOfImgSets:
                new_image.paste(imgSet.fftImg, (0, maxHeight*i))
                if(imgSet.faultImg is not None):
                    new_image.paste(imgSet.faultImg, (fftMaxWidth, maxHeight*i))
                i = i+1

            # Save img
            targetFileName = targetFileName[:-3] + 'pdf'
            targetFullPath = f'{DP.PDF_TARGET_DIR_PATH}/{targetFileName}'
            print()

            i=0
            while(os.path.isfile(targetFullPath)):
                i = i+1
                targetFullPath = f'{targetFullPath[:-4]}_{i}.pdf'

            new_image.save(targetFullPath)

        def archiveDir(sourceDir):
            dirName = sourceDir.split('/')[-1]
            targetDir = f"{DP.PNG_ARCHIVE_PATH}/{dirName}"

            if os.path.isdir(targetDir):    # Folder already exists
                # Move sourceDir content to target
                # Delete sourceDir
                file_names = os.listdir(sourceDir)
                for f in file_names:
                    try:
                        shutil.move(f'{sourceDir}/{f}', targetDir)
                    except shutil.Error : # File already exists at dest
                        os.remove(f'{sourceDir}/{f}')
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
            combineImgs(listOfImgs, cleanseStrForPDFName(listOfImgs[-2]))
            print("Done!\n", end='')

            # Dir processed, archiving
            print(f"Archiving {fName}... ", end='')
            archiveDir(directory)
            print("Done!\n", end='')
            



    def __init__(self):
        self.sensorDirs = self.getImgDirectories()

        self.processSensorDirs()
    