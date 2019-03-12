import requests
import re

# # scrape for nodes  version 0.1
# # Ross Mckechnie 22/11/2018

# used for testing
# theblacklistsite = open(r"D:\test.html")
# data=theblacklistsite.read()

# Please note that this can only scrape from the website every thirty mins as the website has a restriction

theblacklistsite = "https://www.dan.me.uk/tornodes"
data = requests.get(theblacklistsite).content



print("running scrape")
data = re.search(r'\<\!\-\-\ \_\_BEGIN\_TOR\_NODE\_LIST\_\_ \/\/\-\-\>(.*)\<\!\-\- \_\_',data, flags=re.DOTALL)
ipvFour = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\|\w+\|\d+\|\d+\|(\w+)', data.group(1))
ipvSix = re.findall(r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\|\w+\|\d+\|\d+\|(\w+)', data.group(1))

for item in ipvFour:
    if(re.match(r'E|X',item[1])):
        # is exit node
        fileout = open('exitnode.txt', 'a')
        fileout.write(item[0]+'\n')
        fileout.close()
    else:
        # not exit node
        fileout = open('othernode.txt', 'a')
        fileout.write(item[0]+'\n')
        fileout.close()
for item in ipvSix:
    if(re.match(r'E|X',item[-1])):
        # is exit node
        fileout = open('ipsix_exitnode.txt', 'a')
        fileout.write(item[0]+'\n')
        fileout.close()
    else:
        # not exit node
        fileout = open('ipsix_othernode.txt', 'a')
        fileout.write(item[0]+'\n')
        fileout.close()
print("Finished")
