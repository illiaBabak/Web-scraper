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


# Main function
def main():
    url = input("Enter the URL to connect: ")
    r = requests.get(url)
    status = r.status_code
    check_status(status, url)


# Function to check if the status code is 200
def check_status(status, url):
    if status != 200:
        print("Failed to connect website or wrong url")
    else:
        print("Succesfully Connected")
        get_content_from_page(url)


# Function to get content from page
def get_content_from_page(url):
    article = Article(url)
    article.download()
    article.parse()

    # Get the article text:
    print(article.text)
    # Save page content to file
    main_content = article.text
    save(main_content)


if __name__ == "__main__":
    main()
