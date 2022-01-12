from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from tkinter import *

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    print(e)

def display_headlines():
    global mylist
    mylist.destroy()
    mylist=Listbox(root, yscrollcommand = scrollbar.set,width=50,height=50)
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
    for _,i in enumerate(BeautifulSoup(simple_get('https://bbc.com'),'html.parser').select('.media__title')): # media__title
        mylist.insert(END,i.text.replace("  ",""))

root=Tk()
Button(text="scrape",command=display_headlines).pack()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set,width=50,height=50)
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

root.mainloop()