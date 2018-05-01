import requests
from bs4 import BeautifulSoup
import subprocess
import time
import smtplib
import  os


def send_mail(msg):
    email=os.environ.get("email")
    password=os.environ.get("password")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(email,password)
    s.sendmail(email,"meetutarun16@gmail.com",msg)
    s.quit()
    print (msg)
    print("Sent")

def send(msg):
    subprocess.Popen(['notify-send',msg])
    return

it=0

while(True):
    it+=1
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
                if j.strip()=="SUN" or j.strip()=="06":
                    print (i)
                    send_mail(msg=str(j)+" April tickets are available")
                    send(str(j)+" tickets are available")
    print ("Iteration :",it)
    print ("Time:",str(it*5)+"m in")
    time.sleep(300)
