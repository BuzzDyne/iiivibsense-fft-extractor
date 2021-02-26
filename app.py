from FftScraper.fft_scraper import FFTScraper
from FftScraper.job_model import Job
from FftScraper.fft_scraper import FFTScraperIndividual

from PdfCombiner.pdf_combiner import PDFCombiner

from FftScraper import utils

# Input
uname = "gimin@iii.co.id"
pw = "eiy0eiqu9Bai"

runHeadless = False

# urls = [
    #     link, A = tgl1  00"
    #     link, B = tgl1  23"
    #     link, C = tgl7  23"
    #     link, D = tgl31 23"
    #     link, E = PeakRMS1
    #     link, F = PeakRMS2
    #     link, G = PeakRMS3
    #     link, H = PeakRMS4
    # ]

# urls = [
#     "", #A tgl1  00"
#     "", #B tgl1  23"
#     "", #C tgl7  23"
#     "", #D tgl31 23"
#     "", #E = PeakRMS1
#     "", #F = PeakRMS2
#     "", #G = PeakRMS3
#     "" #H = PeakRMS4
# ]

# sptb_1 = [
#     "https://iii.vibsense.net/dashboard/sensor/ckdzkro0qk2310944vn6wdduj/2021-02-03T11:18:55.000Z/", #A tgl1  00"
#     "https://iii.vibsense.net/dashboard/sensor/ckdzkro0qk2310944vn6wdduj/2021-02-03T15:22:53.000Z/", #B tgl1  23"
#     "https://iii.vibsense.net/dashboard/sensor/ckdzkro0qk2310944vn6wdduj/2021-02-10T15:15:32.000Z/", #C tgl7  23"
#     "https://iii.vibsense.net/dashboard/sensor/ckdzkro0qk2310944vn6wdduj/2021-02-18T10:37:47.000Z/", #D tgl31 23"
# ]
# sptb_2 = [
#     "https://iii.vibsense.net/dashboard/sensor/ckalw4teb2cad0944hq7iwz81/2020-08-19T06:59:46.000Z/", #A tgl1  00"
#     "https://iii.vibsense.net/dashboard/sensor/ckalw4teb2cad0944hq7iwz81/2020-08-19T15:58:31.000Z/", #B tgl1  23"
#     "https://iii.vibsense.net/dashboard/sensor/ckalw4teb2cad0944hq7iwz81/2020-08-23T15:57:59.000Z/", #C tgl7  23"
#     "https://iii.vibsense.net/dashboard/sensor/ckalw4teb2cad0944hq7iwz81/2020-08-26T01:19:54.000Z/", #D tgl31 23"
#     "https://iii.vibsense.net/dashboard/sensor/ckalw4teb2cad0944hq7iwz81/2020-08-23T15:24:14.000Z/", #E = PeakRMS1
#     "https://iii.vibsense.net/dashboard/sensor/ckalw4teb2cad0944hq7iwz81/2020-08-22T15:00:16.000Z/", #F = PeakRMS2
#     "https://iii.vibsense.net/dashboard/sensor/ckalw4teb2cad0944hq7iwz81/2020-08-21T15:01:29.000Z/", #G = PeakRMS3
#     "https://iii.vibsense.net/dashboard/sensor/ckalw4teb2cad0944hq7iwz81/2020-08-19T14:51:02.000Z/" #H = PeakRMS4
# ]

# FFTScraperIndividual(sptb_1, headless=True)
# FFTScraperIndividual(sptb_2, headless=True)


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