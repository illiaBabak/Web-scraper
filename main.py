import requests
from bs4 import BeautifulSoup

url = input("Enter the URL to connect")

# https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/ // works
# https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html
# https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y

r = requests.get(url)
status = r.status_code
# Check status of the connection
if status != 200:
    print("Failed to connect website or wrong url")
else:
    print("Succesfully Connected")

# Connect BeautifulSoup html parser
soup = BeautifulSoup(r.content, "html.parser")

# Getting the title tag
print(soup.title)
# return the title and content of the article to the user.
