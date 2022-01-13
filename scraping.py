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

url="https://bbc.com"
select=".media__title"

def display_headlines():
    global mylist
    mylist.destroy()
    mylist=Listbox(root, yscrollcommand = scrollbar.set,width=50,height=50)
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
    for _,i in enumerate(BeautifulSoup(simple_get(url),'html.parser').select(select)): # media__title
        mylist.insert(END,i.text.replace("  ",""))
def options():
    tp=Toplevel()

    def o_save():
        global url,select

        url=ent1.get()
        select=ent2.get()
        tp.destroy()

    frms=[
        Frame(tp),
        Frame(tp),
        Frame(tp)
    ]
    for frm in frms:
        frm.pack(expand=True)

    Label(frms[0],text="url: ").grid(row=0,column=0)
    ent1=Entry(frms[0])
    ent1.grid(row=0,column=1)

    Label(frms[1],text="select: ").grid(row=0,column=0)
    ent2=Entry(frms[1])
    ent2.grid(row=0,column=1)

    Button(frms[2],text="save",command=o_save).grid(row=0,column=0)
    Button(frms[2],text="close",command=lambda tp=tp:tp.destroy()).grid(row=0,column=1)

    tp.mainloop()

root=Tk()
frame=Frame()
frame.pack(expand=True)
Button(frame,text="scrape",command=display_headlines).grid(row=0,column=0)
Button(frame,text="options",command=options).grid(row=0,column=1)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set,width=50,height=50)
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

root.mainloop()