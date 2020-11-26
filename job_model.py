from datetime import datetime

class Job:
    def __init__(self, nCompany, nFactory, nProdLine, nMachine,
                nSensor, latestTime = None, earlyTime = None):
        self.nCompany   = nCompany
        self.nFactory   = nFactory
        self.nProdLine  = nProdLine
        self.nMachine   = nMachine
        self.nSensor    = nSensor
        self.latestTime = latestTime if latestTime else datetime.now()
        self.earlyTime  = earlyTime if earlyTime else datetime.now()