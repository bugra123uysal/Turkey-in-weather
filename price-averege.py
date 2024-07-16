import requests
from bs4 import BeautifulSoup
import tkinter as tk
def dd():
     alveri=ara.get()
     print(alveri)
     """ web scan """
     API_KEY='a3d8561f67014566b81204426241607'
     CITIY='Istanbul'
     link=f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={alveri}'

     al=requests.get(link)
     içerik=al.content
     ö=BeautifulSoup(içerik,"html.parser")
     
     tür=ö.find_all("span")
     
     for xx in tür:
         print(xx.text)
""" sayfa tkinter """
sayfaa=tk.Tk()
sayfaa.geometry("800x500")
def bır():
    print()

ara=tk.Entry(sayfaa)
ara.place(y=10, x=10)

""" aramadan kullanıcının yazdığı veriyi almak """



btnn=tk.Button(sayfaa, text="ara", command=dd)
btnn.place(x=150, y=10)
sayfaa.mainloop()


