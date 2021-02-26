import os
import shutil
import re
from fpdf import FPDF
from constansts import data_paths as DP

class SinglePDFCombiner:

    def printPathsToPDF(self, output_name, imgsFolderPath, imgPaths, output_path="data/pdf"):
        fp = FPDF('p', 'mm', 'A4')
        
        fp.add_page()

        i=0
        for img in imgPaths:
            currCode = i % 4
            print(".", end="")
            if(currCode == 0):
                print(f"inside {currCode}")
                fp.image(f"{DP.PNG_PATH}/{imgsFolderPath}/{img}", w=190, h=0)
            elif(currCode == 1):
                print(f"inside {currCode}")
                fp.image(f"{DP.PNG_PATH}/{imgsFolderPath}/{img}", w=190, h=0)
                fp.image('data/white.jpg')
            elif(currCode == 2):
                print(f"inside {currCode}")
                fp.image(f"{DP.PNG_PATH}/{imgsFolderPath}/{img}", w=190, h=0)
            else:
                print(f"inside {currCode}")
                fp.image(f"{DP.PNG_PATH}/{imgsFolderPath}/{img}", w=190, h=0)
                fp.add_page()

            i += 1

        fp.output(f"{output_path}/{output_name}")
        print("")

    def combinePngPath(self):
        folders = os.listdir("data/png")

        for folder in folders:
            print(f"Processing {folder}", end="")

            imgs = os.listdir(f"data/png/{folder}")

            sensorsInOneMonth = []

            while(len(imgs) > 0):
                dateMonth = imgs[0][:7]

                sensorsInOneMonth = [x for x in imgs if x.startswith(dateMonth)]

                # Delete extracted Sensors from imgs
                for x in sensorsInOneMonth:
                    imgs.remove(x)
                

                self.printPathsToPDF(f"{folder}_{dateMonth}.pdf", folder, sensorsInOneMonth)

                
