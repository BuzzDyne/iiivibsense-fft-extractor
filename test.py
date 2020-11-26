import os

from FftScraper.fft_scraper import FFTScraper
from job_model import Job

# 2020-11-19 21:00:00

sensors = [2, 8]

job = Job(1, 1, 2, 1, nSensor=sensors)

sc = FFTScraper(job)