from PIL import Image

class ImageSet:
    def __init__(self, fftImg, faultImg = None):
        self.fftImg     = fftImg
        self.faultImg   = faultImg if faultImg else None
    
    def getMaxHeight(self):
        """Returns the biggest height value"""
        if self.faultImg is None:
            return self.fftImg.size[1]
        else:
            return max(self.fftImg.size[1], self.faultImg.size[1])

    def getFftWidth(self):
        return self.fftImg.size[0]

    def getFaultsWidth(self):
        if self.faultImg is None:
            return None
        else:
            return self.faultImg.size[0]