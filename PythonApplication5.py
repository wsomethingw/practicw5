import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


def parse_website():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    if quotes:
        lbl_info["text"] = quotes[0].text

def show_creator_info():
    lbl_info["text"] = "Zhuravleva Tanya Andreevna 2ISPk-2"
    
root = tk.Tk()
root.title("Website Parser")
root.geometry("600x400")

lbl_title = tk.Label(root, text="Website Quotes")
lbl_title.pack()

lbl_info = tk.Label(root, text="")
lbl_info.pack()

btn_parse = tk.Button(root, text="Parse Website", command=parse_website)
btn_parse.pack()

btn_creator = tk.Button(root, text="Creator info", command=show_creator_info)
btn_creator.pack()

#путь к фотографии воставляется вами 
image = Image.open("C:/Users/titan/pr/photo_2024-05-12_16-06-04.jpg")
tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=tk_image)
image_label.pack()

root.mainloop()
