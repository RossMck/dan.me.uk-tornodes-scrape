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
data = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\|(\w+)', data.group(1))

for item in data:
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
print("Finished")