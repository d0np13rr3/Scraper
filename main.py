import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
import os
import numpy as np
from os import path
from tkinter import messagebox
from datetime import date
from datetime import datetime
import random
import csv
import datetime
from datetime import timedelta
import tkinter.scrolledtext as tkst
from fpdf import FPDF
import shutil
import atexit
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from array import array


"""CD"""

exists = os.path.isfile('./CD.txt')
if exists:
    pass
else:
    fp=open("CD.txt", "w+")
    fp.close()

main = Tk()
main.title('Scraper')

"""Opmaak Tabs"""

# gives weight to the cells in the grid
rows = 0
while rows < 60:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=60, rowspan=49, sticky='NESW')

# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Info')

tkinter.Label(page1, text="SCRAPE THE NET",borderwidth=1 ).grid(row=1,column=1, )

editArea3 = tkst.ScrolledText(page1, width = 150, height = 60)
editArea3.grid(row = 5, column=1)

# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Set Up')

tkinter.Label(page2, text="Site",borderwidth=1 ).grid(row=1,column=1)
ABXD0 = tkinter.Entry(page2,borderwidth=1, width =100 )
ABXD0.grid(row=2,column=1)

tkinter.Label(page2, text="What kind of tag do you want? Without the '<' and '>'",borderwidth=1 ).grid(row=3,column=1)
ABXD1 = tkinter.Entry(page2,borderwidth=1, width =100 )
ABXD1.grid(row=4,column=1)

def tag():
    top = ttk.top = Toplevel()
    CIList = ""
    with open ('html.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter = ';')
        for row in reader:
            try:
                CIList = CIList + str(row[0]) + str(row[1]) +'\n'
            except:
                pass
    editArea31 = tkst.ScrolledText(top, width = 80, height = 20)
    editArea31.grid(row = 1, column=1)
    editArea31.insert('1.0', CIList)

def scrape():
    editArea3.delete('1.0', END)
    site = ABXD0.get()
    tag = ABXD1.get()

    """set up site and request"""
    url = str(site)
    response = requests.get(url)

    """parser"""
    soup = BeautifulSoup(response.text, "html.parser")

    atag = soup.findAll(str(tag))
    atagtxt = ""
    utf8counter = 0 

    fp=open("CD.txt", "a")

    for a in atag:
        try:
            atagtxt = atagtxt + str(a) + '\n'
            fp.write(str(atagtxt))
        except UnicodeError:
            utf8counter = utf8counter + 1
            print("no utf 8")

    fp.close()
    editArea3.insert('1.0', atagtxt)

    messagebox.showinfo("Scraped", "Site is scraped with chosen tag")

def scrapeTXT():
    editArea3.delete('1.0', END)
    site = ABXD0.get()
    tag = ABXD1.get()

    """set up site and request"""
    url = str(site)
    response = requests.get(url)

    """parser"""
    soup = BeautifulSoup(response.text, "html.parser")


    atag = soup.get_text()

    editArea3.insert('1.0', atag)
    messagebox.showinfo("Tags", "View info for text")

def scrapeTAGS():
    editArea3.delete('1.0', END)
    site = ABXD0.get()
    tags = ""
    tagsL = {}

    """set up site and request"""
    url = str(site)
    response = requests.get(url)

    """parser"""
    soup = BeautifulSoup(response.text, "html.parser")

    i = 0
    for tag in soup.find_all(True):
        tagsL[str(tag.name)] = i
        i = i + 1

    for t in tagsL:
        tags = tags + str(t) + '\n'        

    editArea3.insert('1.0', tags)
    messagebox.showinfo("Tags", "View info for all available tags on the site")

"""main menu"""
main_menu = Menu(main)
main.config(menu=main_menu)

"""submenu"""
text_menu = Menu(main_menu, tearoff=False)
"""submenu"""
text_menu.add_command(label='HTML tag',
              command=tag)

"""Naam menu"""
main_menu.add_cascade(label="Hints", menu=text_menu)

"""submenu"""
text_menu1 = Menu(main_menu, tearoff=False)
"""submenu"""
text_menu1.add_command(label='Scrape site with chosen tag',
              command=scrape)
text_menu1.add_command(label='Scrape me - text',
              command=scrapeTXT)
text_menu1.add_command(label='Scrape me - available tags',
              command=scrapeTAGS)

"""Naam menu"""
main_menu.add_cascade(label="Scrapers", menu=text_menu1)


