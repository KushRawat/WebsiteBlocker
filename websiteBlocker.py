import time
from datetime import datetime as dt

hostsTemp = "hosts"
hostsPath = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websiteList = ["www.netflix.com", "netflix.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21):
        print("Working hours...")
        with open(hostsTemp, 'r+') as file:
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Non-working hours...")
    time.sleep(5)