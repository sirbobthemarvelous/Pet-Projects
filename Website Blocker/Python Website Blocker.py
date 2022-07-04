import time
from datetime import datetime as dt
  # https://www.geeksforgeeks.org/website-blocker-using-python/
# change hosts path according to your OS
hosts_path = "C:\Windows\System32\drivers\etc"
# localhost's IP
redirect = "127.0.0.1"
  
# websites That you want to block
website_list = ["www.facebook.com","facebook.com",
      "www.tumblr.com"]
  
while True:
  
    # time of your work
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
  
            # removing hostnmes from host file
            file.truncate()
  
        print("Fun hours...")
    time.sleep(5)

    """
    import time
from datetime import datetime as dt
hosts_path = r"C:\Windows\System32\drivers\etc"   # r is for raw string
hosts_temp = "hosts"
redirect = "127.0.0.1"
web_sites_list = ["www.facebook.com", "facebook.com"]    # users can modify the list of the websites they want to block
while True:
   if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22):
       print("Working hours")
       with open(hosts_path, "r+") as file:
           content = file.read()
           for website in web_sites_list:
               if website in content:
                   pass
               else:
                   file.write(redirect+" "+website+"\n")
   else:
       print("Fun time")
       with open(hosts_path, "r+") as file:
           content = file.readlines()
           file.seek(0)  # reset the pointer to the top of the text file
           for line in content:
               # here comes the tricky line, basically we overwrite the whole file
               if not any(website in line for website in web_sites_list):
                   file.write(line)
               # do nothing otherwise
           file.truncate() # this line is used to delete the trailing lines (that contain DNS)
    time.sleep(5)
    """
                