import os

from FftScraper.fft_scraper import FFTScraper
from FftScraper.job_model import Job

from PdfCombiner.pdf_combiner import PDFCombiner

from PdfCombiner.single_pdf_combiner import SinglePDFCombiner

############## FFT Scraper Tests ##############
# uname = "gimin@iii.co.id"
# pw = "eiy0eiqu9Bai"
# runHeadless = False

# sensors = [2, 8]
## APP, Serang Mill, PM5, PM5 Dryers, (Sensors)
# job = Job(1, 1, 2, 1)
# sc = FFTScraper(uname, pw, job, runHeadless)

############## PDF Combiner Tests ##############

# pc = PDFCombiner()

spc = SinglePDFCombiner()

imgPaths = [
    '2020-10_a_fft.png', 
    '2020-10_a_rms.png', 
    '2020-10_b_fft.png', 
    
    '2020-10_b_rms.png', 
    '2020-10_c_fft.png', 
    '2020-10_c_rms.png', 
    '2020-10_d_fft.png', 
    '2020-10_d_rms.png', '2020-10_e_fft.png', 
    '2020-10_e_rms.png', '2020-10_f_fft.png', 
    '2020-10_f_rms.png', '2020-10_g_fft.png', 
    '2020-10_g_rms.png', '2020-10_h_fft.png', '2020-10_h_rms.png']

# spc.printPathsToPDF("test.pdf", "test", imgPaths)
spc.combinePngPath()