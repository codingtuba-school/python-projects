from tkinter import *
from random import randint as random
winning=[
    [[0,0],[0,1],[0,2]],
    [[1,0],[1,1],[1,2]],
    [[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],
    [[0,1],[1,1],[2,1]],
    [[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],
    [[0,2],[1,1],[2,0]],
]
danger=[
    # 3 move wins
    # ...
    # 2 move wins
    [[0,0],[0,1],[1,0]],
    [[0,2],[0,1],[1,2]],
    [[2,0],[1,0],[2,1]],
    [[2,2],[2,1],[1,2]],
    [[0,0],[0,2],[2,0]],
    [[2,0],[2,2],[0,2]],
    [[0,0],[0,2],[1,1]],
    [[2,0],[2,2],[1,1]],
    [[0,0],[2,0],[1,1]],
    [[0,2],[2,2],[1,1]],
    [[0,0],[1,0],[1,1]],
    [[2,0],[2,1],[1,1]],
    [[2,2],[1,2],[1,1]],
    [[0,2],[0,1],[1,1]],
    # 1 move wins
    [[0,0],[0,1],[0,2]],
    [[1,0],[1,1],[1,2]],
    [[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],
    [[0,1],[1,1],[2,1]],
    [[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],
    [[0,2],[1,1],[2,0]],
]
_w=winning
def play(b):
    root=Tk()
    buttons=b
    _buttons=[[0,0,0],[0,0,0],[0,0,0]]
    cacl_w=120
    largest=-1
    for _row in buttons:
        amount=0
        for _number in _row:
            if _number!=0:
                amount+=1
        if amount>largest:
            largest=amount
    cacl_w+=(4*largest)
    root.title("ttt")
    root.geometry(str(cacl_w)+"x90+0+0")
    def two_row():
        _return=[False,0,[-1,-1]]
        for _side in [2,1]:
            _way=winning
            if _side==2:
                _way=danger
            for _solution in _way:
                _enemy=_side+1
                if _enemy==3:
                    _enemy=1
                _occupied=0
                _slot=[-1,-1]
                for _place in _solution:
                    if buttons[_place[0]][_place[1]]==_enemy:
                        _occupied+=1
                    elif buttons[_place[0]][_place[1]]==0:
                        _slot=_place
                if _occupied==2 and _slot!=[-1,-1]:
                    _return=[True,_side,_slot]
        return _return
    def move():
        found0=False
        for _row in buttons:
            for _item in _row:
                if _item==0:
                    found0=True
        if found0:
            if two_row()[0]:
                _slot=two_row()[2]
                buttons[_slot[0]][_slot[1]]=2
            else:
                _ramnom=[random(0,2),random(0,2)]
                while buttons[_ramnom[0]][_ramnom[1]]!=0:
                    _ramnom=[random(0,2),random(0,2)]
                buttons[_ramnom[0]][_ramnom[1]]=2
    def winner():
        _return=[False,0]
        for _side in range(1,3):
            for _win in _w:
                if buttons[_win[0][0]][_win[0][1]]==_side and buttons[_win[1][0]][_win[1][1]]==_side and buttons[_win[2][0]][_win[2][1]]==_side and _return[0]==False:
                    _return=[True,_side]
        found0=False
        for _row in buttons:
            for _item in _row:
                if _item==0:
                    found0=True
        if found0==True or _return[0]==True:
            return _return
        else:
            return [True,3]
    def _set(r,i):
        if buttons[r][i]==0:
            buttons[r][i]=1
            move()
            if winner()[0]:
                root.destroy()
                
                _text=""
                if winner()[1]==1:
                    _text="you win, "
                elif winner()[1]==2:
                    _text="you lose, "
                else:
                    _text="you tied, "
                _root=Tk()
                _root.geometry("200x30+0+0")
                _root.title("tic tac toe")
                def new():
                    _root.destroy()
                    play([[0,0,0],[0,0,0],[0,0,0]])
                Button(_root,text=_text+"play again?",command=new).pack()
            else:
                root.destroy()
                play(buttons)
    for i in range(3):
        for _i in range(3):
            if buttons[i][_i]==0:
                _buttons[i][_i]=Button(text=" ",command=lambda: _set(0,0))
            if buttons[i][_i]==1:
                _buttons[i][_i]=Button(text="x",command=lambda: _set(0,0))
            if buttons[i][_i]==2:
                _buttons[i][_i]=Button(text="o",command=lambda: _set(0,0))
    _buttons[0][1].config(command=lambda: _set(0,1))
    _buttons[0][2].config(command=lambda: _set(0,2))
    _buttons[1][0].config(command=lambda: _set(1,0))
    _buttons[1][1].config(command=lambda: _set(1,1))
    _buttons[1][2].config(command=lambda: _set(1,2))
    _buttons[2][0].config(command=lambda: _set(2,0))
    _buttons[2][1].config(command=lambda: _set(2,1))
    _buttons[2][2].config(command=lambda: _set(2,2))
    for i in range(3):
        for _i in range(3):
            _buttons[i][_i].update()
            _buttons[i][_i].grid(row=i,column=_i)
    root.mainloop()
play([[0,0,0],[0,0,0],[0,0,0]])