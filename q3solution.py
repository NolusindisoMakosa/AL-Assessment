"""
Provides total time it took to hit a website
"""
import requests
NUMVIVISTS = 30
TOTALVISITS = 0
url = ["https://www.takealot.com/camping-outdoor/campingfurniture","https://docs.docker.com",
"https://www.primevideo.com/"]
TOTAL= 0
for i in range(len(url)):
    if TOTALVISITS < NUMVIVISTS :
        s = requests.get(url[i])
        total = s.elapsed * NUMVIVISTS
        print (url[i])
        print ('Time: ', s.elapsed)
        print ('Total of all hits: ',TOTAL)

