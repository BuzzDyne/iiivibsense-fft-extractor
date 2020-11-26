from datetime import datetime, timedelta

class Job:
    def __init__(self, nCompany, nFactory, nProdLine, nMachine,
                nSensor = None, latestTime = None, earlyTime = None):
        # 1, 2, ...
        self.nCompany   = nCompany
        self.nFactory   = nFactory
        self.nProdLine  = nProdLine
        self.nMachine   = nMachine
        self.nSensor    = nSensor if nSensor else []
        self.latestTime = latestTime if latestTime else datetime.now()
        self.earlyTime  = earlyTime if earlyTime else self.latestTime - timedelta(days=1)