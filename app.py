from FftScraper.fft_scraper import FFTScraper
from FftScraper.job_model import Job

from PdfCombiner.pdf_combiner import PDFCombiner

# Input
uname = "gimin@iii.co.id"
pw = "eiy0eiqu9Bai"

runHeadless = False

listOfJobs = [
    Job(1,1,2,1,[1]),
    Job(1,1,2,1,[2]),
    Job(1,1,1,1,[])
]

# Program
for job in listOfJobs:
    sc = FFTScraper(uname, pw, job, runHeadless)
PDFCombiner()