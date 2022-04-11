
from multiprocessing.sharedctypes import Value
import requests
from time import time
import os

url = os.environ ['URL']
total = os.environ ['TOTAL']

numvisit = 30
totalvisits = 0
url = ["https://www.takealot.com/camping-outdoor/campingfurniture","https://docs.docker.com",
"https://www.primevideo.com/"]
total = 0

for i in range(len(url)): 
    if totalvisits < numvisit :
        s = requests.get(url[i])
        total = s.elapsed * numvisit
        print (url[i])
        print ('Time: ', s.elapsed)
        print ('Total of all hits: ',total)
        
   # print ('Number of visits = ',numvisit,'\n','Time to hit website = ' , end_time - start_time)


