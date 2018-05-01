import requests
from bs4 import BeautifulSoup
import subprocess
import time


def send(msg):
    subprocess.Popen(['notify-send',msg])
    return


while(True):
    url="https://in.bookmyshow.com/buytickets/avengers-infinity-war-hyderabad/movie-hyd-ET00053419-MT/"
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    # print (soup.prettify())

    div=soup.findAll("div",{"class": "date-container"})

    # print (len(div))
    # print (div)
    for row in div:
        # print(row)
        li=row.find_all('div')
        for i in li:
            t=str(i.text)
            # print (t.split())
            for j in t.split():
                if j.strip()=="SUN" or j.strip()=="03":
                    print (i)
                    send(str(j)+" tickets are available")

    time.sleep(5)
