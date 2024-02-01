import requests
import os
import shutil
from newspaper import Article
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.geometry("400x200")
window.title("Python Web Scraper")

# Styling

# Import the tcl file
window.tk.call("source", "forest-dark.tcl")
# Set the theme with the theme_use method
ttk.Style().theme_use("forest-dark")

enter_url_text = ttk.Label(window, text="Enter the URL to connect: ")
enter_url_text.pack(pady=5)

url_entry = ttk.Entry(window, justify="center")
url_entry.pack(pady=5)

status_label = ttk.Label(window, text="")
status_label.pack(pady=10)

FILE_NAME = "data.txt"
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
DESTINATION_PATH = os.path.join(DOWNLOAD_PATH, FILE_NAME)

# A counter that count the number of saved files
counter = 1


def show_alert(msg):
    messagebox.showinfo("Alert", msg)


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

    status_label.config(text="")
    url_entry.delete(0, END)
    window.update()

    shutil.move(FILE_NAME, DESTINATION_PATH)
    window.after(
        0, show_alert, f"Succesfully Connected\nFile saved in {DESTINATION_PATH}"
    )


# Function that executes a page request
def request_to_page(url):
    try:
        r = requests.get(url)
        status = r.status_code
        check_status(status, url)
    except:
        show_alert("Failed to connect website or wrong url")
        status_label.config(text="")
        return


# Function that receives the url
def get_url():
    url = url_entry.get()

    if not url:
        show_alert("Enter valid URL")
        return

    status_label.config(text="Connecting...")
    window.update()

    window.after(0, request_to_page, url)


# Function to check if the status code is 200
def check_status(status, url):
    if status != 200:
        status_label.config(text="")
        show_alert("Failed to connect website or wrong url")
    else:
        get_content_from_page(url)


# Function to get content from page
def get_content_from_page(url):
    article = Article(url)
    article.download()
    article.parse()

    # Save page content to file
    main_content = article.text
    save(main_content)


# , bg="black", fg="white",
btn = ttk.Button(window, text="Get data", command=get_url)

btn.pack(pady=20)
status_label.pack(side="top", pady=10)

window.mainloop()
