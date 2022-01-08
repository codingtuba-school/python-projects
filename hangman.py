from tkinter import *
import tkinter
from random_words import RandomWords

rw = RandomWords()
root=Tk()
root.title("Hangman")

word = rw.random_word()
blanks = "_" * len(word)
bodyParts = ['0', '/', '|', '\\', '/', '\\']
currentBodyParts = ['', '', '', '', '', '']

def guess():
    global blanks
    guess=entry_input.get()
    entry_input.delete(0,END)
    game = True
    if guess in word:
        broken_word=list(word)
        for i in range(len(broken_word)):
            if broken_word[i] == guess:
                blanks = blanks[:i] + guess + blanks[i+1:]
        if blanks.count("_") == 0:
            button.config(text="You win!")
    else:
        for part in currentBodyParts:
            if part == "":
                currentBodyParts[currentBodyParts.index("")]=bodyParts[currentBodyParts.index("")]
                break
        if currentBodyParts==bodyParts:
            button.config(text="You loose, the word was "+word,width=100)
            entry_input.destroy()
            game=False
    if game:
        button.config(text="""
|---------|
|         |
|         """+currentBodyParts[0]+"""
|        """+currentBodyParts[1]+""""""+currentBodyParts[2]+""""""+currentBodyParts[3]+"""
|        """+currentBodyParts[4]+""" """+currentBodyParts[5]+"""
|
|
|

"""+blanks+"""
    """)
    button.update()
button=Button(root,text="""
|---------|
|         |
|         """+currentBodyParts[0]+"""
|        """+currentBodyParts[1]+""""""+currentBodyParts[2]+""""""+currentBodyParts[3]+"""
|        """+currentBodyParts[4]+""" """+currentBodyParts[5]+"""
|
|
|

"""+blanks+"""
    """, justify='left', font='TkFixedFont',command=guess,width=30)
button.pack(anchor=tkinter.W)
entry_input=Entry(root,width=25)
entry_input.pack()

root.mainloop()