import glob
import os
import concurrent.futures
import random
 
links = glob.glob("links/*.txt*")
 
random.shuffle(links)
 
def wgetFile(link):
    os.system("wget -nc -c --input " + link)
 
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(wgetFile, links)
