import time
from datetime import datetime as dt

 # hosts_temp = r"C:\Users\a\PycharmProjects\Python_Projects\venv\Scripts\hosts"
hosts_loc = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# change the websites here which you want to block
website_list = ["www.facebook.com", "facebook.com", "www.flipkart.com", "flipkart.com"]

while True:
    # Enter the time for the website to be bloced in 24 hr format
    if dt(dt.now().year, dt.now().month, dt.now().day, 14) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Working Hours !! ")
        with open(hosts_loc, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_loc, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours !!")
    time.sleep(5)


