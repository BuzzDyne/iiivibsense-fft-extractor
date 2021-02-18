from FftScraper.fft_scraper import FFTScraper
from FftScraper.job_model import Job
from FftScraper.fft_scraper import FFTScraperIndividual

from PdfCombiner.pdf_combiner import PDFCombiner

from FftScraper import utils

# Input
uname = "gimin@iii.co.id"
pw = "eiy0eiqu9Bai"

runHeadless = False

urls = [
    "https://iii.vibsense.net/dashboard/sensor/ckalw4t6d2c740944fywwmwr5/",
    "https://iii.vibsense.net/dashboard/sensor/ckalw4t6d2c740944fywwmwr5/2020-12-02T12:11:00.000Z/",
    "https://iii.vibsense.net/dashboard/sensor/ckalw4ta62c840944wkp5u344/18-Feb-2021%2012:23/",
    "https://iii.vibsense.net/dashboard/sensor/ckalw4tdu2ca40944l65trwnc/2020-09-10T11:30:31.000Z/"
]

FFTScraperIndividual(urls)


# Default Program
# 
# # 'YYYY-MM-DD HH:MM:SS'
# latestTime      = utils.convInputStrToDatetime('2021-02-08 23:59:59')
# latestTime1      = utils.convInputStrToDatetime('2021-02-09 23:59:59')
# latestTime2      = utils.convInputStrToDatetime('2021-02-10 23:59:59')
# latestTime3      = utils.convInputStrToDatetime('2021-02-11 23:59:59')
# latestTime4      = utils.convInputStrToDatetime('2021-02-12 23:59:59')
# latestTime5      = utils.convInputStrToDatetime('2021-02-13 23:59:59')
# latestTime6      = utils.convInputStrToDatetime('2021-02-15 23:59:59')
# latestTime7      = utils.convInputStrToDatetime('2021-02-16 23:59:59')


# listOfJobs = [
#     # Job(1,1,2,1,[1]),
#     # Job(1,1,2,1,[2]),
#     # Job(1,1,1,1,[6,9,10,11], latestTime),

#     # Job(1,1,1,1,[10,11], latestTime),
#     # Job(1,1,1,1,[6,10,11], latestTime1),
#     # Job(1,1,1,1,[6,10,11], latestTime2),
#     # Job(1,1,1,1,[6,10,11], latestTime3),
#     # Job(1,1,1,1,[6,10,11], latestTime4),
#     # Job(1,1,1,1,[6,10,11], latestTime5),
#     Job(1,1,1,1,[6,10,11], latestTime6),
#     Job(1,1,1,1,[6,10,11], latestTime7)
#     # Job(1,1,1,1,[10,11], latestTime)
# ]

# # Program
# for job in listOfJobs:
#     sc = FFTScraper(uname, pw, job, runHeadless)
#     PDFCombiner()