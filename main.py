import requests
import os
import shutil
from bs4 import BeautifulSoup
from newspaper import Article

FILE_NAME = "data.txt"
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
DESTINATION_PATH = os.path.join(DOWNLOAD_PATH, FILE_NAME)

# A counter that count the number of saved files
counter = 1


# A function that will save data to txt file
def save(data_to_save):
    global DESTINATION_PATH, counter

    if os.path.exists(DESTINATION_PATH):
        file_name, file_extension = os.path.splitext(DESTINATION_PATH)
        file_name_with_counter = f"{file_name}({counter}){file_extension}"
        DESTINATION_PATH = os.path.join(DOWNLOAD_PATH, file_name_with_counter)
        counter += 1

    with open(FILE_NAME, "w") as file:
        file.write(data_to_save)

    shutil.move(FILE_NAME, DESTINATION_PATH)
    print(f"File saved in {DESTINATION_PATH}")


url = input("Enter the URL to connect: ")

# https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/ // works
# https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html
# https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y

# Gets the status code to see if the website is up
r = requests.get(url)
content = r.content
status = r.status_code


# Function to check if the status code is 200
def check_status():
    global status
    # Check status of the connection
    if status != 200:
        print("Failed to connect website or wrong url")
    else:
        print("Succesfully Connected")
        div_to_text()


# Connect BeautifulSoup html parser
soup = BeautifulSoup(r.content, "html.parser")

# Getting the title tag
print(soup.title)


def div_to_text():
    article = Article(url)
    article.download()
    article.parse()

    # Get the article text:
    print(article.text)
    # mozhna zapisat article.text і прокінуть в save()


check_status()
