from datetime import datetime
import re

def convWebTimeStrToDatetime(timeStr):
    return datetime.strptime(timeStr,"%d %b %Y, %H:%M")

def convInputStrToDatetime(timeStr):
    return datetime.strptime(timeStr,"%Y-%m-%d %H:%M:%S")

def convTimeToStr(dateT):
    return datetime.strftime(dateT,"%Y-%m-%d_%H-%M-%S")

def cleanseStr(x):
    x = x.replace(' ', "_")
    # x = re.sub(r'/[^\w-]/', '',x)
    return x