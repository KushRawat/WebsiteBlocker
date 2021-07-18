import time
from datetime import datetime as dt

hostsTemp = "hosts"
hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websiteList = ["www.netflix.com", "netflix.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21):
        print("Working hours...")
        # Using reading and appending file method
        with open(hostsTemp, 'r+') as file: 
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        # Using reading and appending file method
        with open(hostsTemp, 'r+') as file:
            content = file.readlines()
            file.seek(0) # Placing pointer to the top of the file
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
            file.truncate()
        print("Non-working hours...")
    time.sleep(5)