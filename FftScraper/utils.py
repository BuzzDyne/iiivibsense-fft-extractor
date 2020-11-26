from datetime import datetime
import re
import os

# DATETIME
def convWebTimeStrToDatetime(timeStr):
    return datetime.strptime(timeStr,"%d %b %Y, %H:%M")

def convInputStrToDatetime(timeStr):
    return datetime.strptime(timeStr,"%Y-%m-%d %H:%M:%S")

def convTimeToStr(dateT):
    return datetime.strftime(dateT,"%Y-%m-%d_%H-%M-%S")

def getCurrDateStr():
    return datetime.strftime(datetime.now(), "%Y-%m-%d")

# STRING
def cleanseStr(x):
    # Swap whitespaces with underscores
    x = re.sub(r'(\s+)', '_', x)
    # Filter only alphanumeric and underscores
    x = re.sub(r'[^\w+]', '', x)
    return x

# OS
def safeCreateDir(relPath):
    """Will create a dir if doesnt exist yet"""
    if not os.path.isdir(relPath):
        os.mkdir(relPath)