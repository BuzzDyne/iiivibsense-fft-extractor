from datetime import datetime

def convStrToTime(timeStr):
    return datetime.strptime(timeStr,"%d %b %Y, %H:%M")

def convTimeToStr(dateT, mode = 0):
    # 0 = Time only
    # 1 = Date Only
    if mode == 0:
        return datetime.strftime(dateT,"%H_%M_%S")
    elif mode == 1:
        return datetime.strftime(dateT,"%Y%b%d")