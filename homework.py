import threading
import requests
from time import time


def download_all(thread_more):
    if thread_more == 0:
        t = time()
        for i in range(len(urls)):
            download_single_file(urls[i], 'file'+str(i+1))
            
        print('Time:',time() - t)
    else:
        t = time()
        threads = []
        for i in range(len(urls)):
            threads.append(threading.Thread(target=download_single_file, args = (urls[i], 'file'+str(i+1))))
            threads[i].start()
        for i in range(len(urls)):
            threads[i].join()
        print('Time:',time() - t)
        
    



def download_single_file(url, name):
    print(name + '->started\n')
    try:
        request = requests.get(url, stream=True)
        with open(name+'.pdf', 'wb') as fh:
            for chunk in request.iter_content(chunk_size = 512):
                fh.write(chunk)
    except Exception as e:
        print(name + 'could not be downloaded')
        print('Error code: ', e.code)
    print(name + '->done\n')
        
    

urls = [
'https://www.hq.nasa.gov/alsj/a17/A17_FlightPlan.pdf',
'https://ars.els-cdn.com/content/image/1-s2.0-S0140673617321293-mmc1.pdf',
'http://www.visitgreece.gr/deployedFiles/StaticFiles/maps/Peloponnese_map.pdf',
'http://www.ubicomp.org/ubicomp2003/adjunct_proceedings/proceedings.pdf']

"""
urls = [
'https://www.hq.nasa.gov/alsj/a17/A17_FlightPlan.pdf',
'https://ars.els-cdn.com/content/image/1-s2.0-S0140673617321293-mmc1.pdf']
"""






