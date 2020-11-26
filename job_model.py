from datetime import datetime

class Job:
    def __init__(self, nCompany, nFactory, nProdLine, nMachine,
                nSensor, latestTime, earlyTime):
        self.nCompany   = nCompany
        self.nFactory   = nFactory
        self.nProdLine  = nProdLine
        self.nMachine   = nMachine
        self.nSensor    = nSensor
        self.latestTime = latestTime
        self.earlyTime  = earlyTime