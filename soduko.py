from tkinter import *
from random import randint as random

class SodukoOptions():
    def __init__(self,name="Soudko",maxBoxLength=False,maxBoxWidth=False,maxBoardHeight=False,maxBoardWidth=False,overideErrors=False,debugMessages=False,onGameWin=False,onGameLoss=False):
        self.name=name;
        self.maxBoxLength=maxBoxLength;
        self.maxBoxWidth=maxBoxWidth;
        self.maxBoardHeight=maxBoardHeight;
        self.maxBoardWidth=maxBoardWidth;
        self.overideErrors=overideErrors;
        self.debugMessages=debugMessages;
        self.onGameWin=onGameWin;
        self.onGameLoss=onGameLoss;

# usage:
# 
# board is box_length*box_width+board_height*board_width
# Tk is Tk()
# options is SoudkoOptions()
# 
# Soudko(board,Tk[,options])


class Soduko():
    def __init__(self,board,Tk,options=False):
        self.root=Tk
        self.board=None;
        self.boxes=None;
        self.selected_slot=None;
        self.selected_number=None;
        self.name="Soduko"
        self.maxBoxLength=5;
        self.maxBoxWidth=5;
        self.maxBoardHeight=5;
        self.maxBoardWidth=4;
        self.overideErrors=False;
        self.debugMessages=False;
        self.error=False;
        if options:
            if options.name:
                self.name=options.name
            if options.maxBoxLength:
                self.maxBoxLength=options.maxBoxLength
            if options.maxBoxWidth:
                self.maxBoxWidth=options.maxBoxWidth
            if options.maxBoardHeight:
                self.maxBoardHeight=options.maxBoardHeight
            if options.maxBoardWidth:
                self.maxBoardWidth=options.maxBoardWidth
            if options.overideErrors:
                self.overideErrors=options.overideErrors
            if options.debugMessages:
                print("Options enabled")
                self.debugMessages=options.debugMessages;
            if options.onGameWin:
                self.onGameWin=options.onGameWin
            if options.onGameLoss:
                self.onGameLoss=options.onGameLoss
        def board_error(error="-1"):
            print("Soduko board error, runner disabled. ("+error+")")
            self.error=True

        if "+" in board and "*" in board or self.overideErrors:
            if ("*" in board.split("+")[0] and "*" in board.split("+")[1]) or self.overideErrors:
                if self.debugMessages:
                    print("Board has passed checks 1")
                all_numbers=True
                for item in board.split("+"):
                    for number in item.split("*"):
                        passed=True
                        try:
                            int(number)
                            passed=True
                        except:
                            passed=False
                        finally:
                            if not passed:
                                all_numbers=False
                if all_numbers or self.overideErrors:
                    if self.debugMessages:
                        print("Board has passed checks 2")
                    self.board=[[-1,-1],[-1,-1]]
                    for i in range(2):
                        for ii in range(2):
                            self.board[i][ii]=int(board.split("+")[i].split("*")[ii])
                    if self.debugMessages:
                        print("================================================================")
                    if (self.board[0][0]>0 and self.board[0][0]<=self.maxBoxLength) or self.overideErrors:
                        if self.debugMessages:
                            print("Box length is valid")
                    else:
                        self.board[0][0]=-1
                        board_error("board")
                    if (self.board[0][1]>0 and self.board[0][1]<=self.maxBoxWidth and not self.error) or self.overideErrors:
                        if self.debugMessages:
                            print("Box width is valid")
                    else:
                        self.board[0][1]=-1
                        board_error("board")
                    if (self.board[1][0]>0 and self.board[1][0]<=self.maxBoardHeight and not self.error) or self.overideErrors:
                        if self.debugMessages:
                            print("Board length is valid")
                    else:
                        self.board[1][0]=-1
                        board_error("board")
                    if (self.board[1][1]>0 and self.board[1][1]<=self.maxBoardWidth and not self.error) or self.overideErrors:
                        if self.debugMessages:
                            print("Board width is valid")
                    else:
                        self.board[1][1]=-1
                        board_error("board")
                    if self.debugMessages:
                        print("================================================================")
                    if self.debugMessages and not self.error:
                        print("Board passed checks 3")
                        print(">>> Board passed all checks")
                else:
                    board_error("board")
            else:
                board_error("board")
        else:
            board_error("board")

    # renders the board
    def render(self):
        if not self.error:
            self.root.title(self.name)
            for i in range(len(self.boxes)):
                for ii in range(len(self.boxes[i])):
                    box=self.boxes[i][ii]
                    box_grid_start_location=[
                        i*(self.board[0][0]+1),  #y-axis
                        ii*(self.board[0][1]+1), #x-axis
                    ]
                    for s_i in range(len(box)+1):
                        for s_ii in range(len(box[0])+1):
                            # border won't display for impossible
                            # boards, but I don't care because they
                            # aren't beatable
                            if s_i==len(box) and s_ii==len(box[0]):
                                Button(self.root,text="+").grid(row=box_grid_start_location[1]+s_i,column=box_grid_start_location[0]+s_ii)
                            elif s_i==len(box):
                                Button(self.root,text="—").grid(row=box_grid_start_location[1]+s_i,column=box_grid_start_location[0]+s_ii)
                            elif s_ii==len(box[0]):
                                Button(self.root,text="|").grid(row=box_grid_start_location[1]+s_i,column=box_grid_start_location[0]+s_ii)
                            else:
                                _dummy=box[s_i][s_ii]
                                if _dummy==-1:
                                    _dummy=""
                                elif _dummy==0:
                                    _dummy="!"
                                else:
                                    _dummy=int(_dummy)
                                if self.selected_slot==str(i)+","+str(ii)+","+str(s_i)+","+str(s_ii):
                                    _dummy="!"+str(_dummy)
                                _state=NORMAL
                                
                                if str(i)+","+str(ii)+","+str(s_i)+","+str(s_ii) in self.disabled:
                                    if _dummy=="" or _dummy=="!": self.disabled.remove(str(i)+","+str(ii)+","+str(s_i)+","+str(s_ii))
                                    else: _state=DISABLED

                                Button(text=_dummy,state=_state,command=lambda i=i,ii=ii,s_i=s_i,s_ii=s_ii:self.select_slot(i,ii,s_i,s_ii)).grid(row=box_grid_start_location[1]+s_i,column=box_grid_start_location[0]+s_ii)
            number_grid_y_start=(((self.board[0][0]+1)*self.board[1][0])+1)*5
            number_grid_x=0
            for i in range(self.board[0][0]*self.board[0][1]+1):
                if i==0:
                    Button(text=" ",command=lambda: self.select_number(-1)).grid(row=number_grid_y_start,column=number_grid_x)
                else:
                    addon_text=""
                    if i==self.selected_number:
                        addon_text="! "
                    Button(text=addon_text+str(i),command=lambda i=i: self.select_number(i)).grid(row=number_grid_y_start,column=number_grid_x)
                number_grid_x+=1
            self.root.mainloop()
        else:
            print("There was an error somewhere.")

    # sets up the game
    def start(self):
        if not self.error:
            self.boxes=[]
            for i in range(self.board[1][1]):
                self.boxes.append([])
                for ii in range(self.board[1][0]):
                    self.boxes[i].append([])
                    for iii in range(self.board[0][0]):
                        self.boxes[i][ii].append([])
                        for iiii in range(self.board[0][1]):
                            self.boxes[i][ii][iii].append(-1)
            self.shuffle()
            self.render()
        else:
            print("There was a error somewhere.")
    
    #shuffles the board
    def shuffle(self):
        if not self.error:
            self.disabled=[]
            __max=self.board[0][0]*self.board[0][1]
            _max=int(self.board[0][0]*self.board[0][1])
            _min=_max-random(3,4)
            if _min<0: _min=0
            for i in range(len(self.boxes)):
                for ii in range(len(self.boxes[0])):
                    r_left=random(_min, _max)
                    for _dummy in range(r_left):
                        if r_left>0:
                            r_1=random(0,self.board[0][0]-1)
                            r_2=random(0,self.board[0][1]-1)
                            self.boxes[i][ii][r_1][r_2]=random(1,__max)
                            if self.checkGameStatus(i,ii,r_1,r_2)!=False:
                                self.disabled.append(str(i)+","+str(ii)+","+str(r_1)+","+str(r_2))
                            else:
                                print(i,ii,r_1,r_2)
                                self.boxes[i][ii][r_1][r_2]=-1
                            r_left-=1
        else:
            print("There was an error somewhere.")

    # selectes a slot
    def select_slot(self,i,ii,iii,iiii):
        if not self.error:
            try:
                self.boxes[i][ii][iii][iiii]
            except:
                if not self.overideErrors:
                    self.error = True
                    print("Soduko input error, runner disabled.")
            if not self.error:
                if self.debugMessages:
                    print("An item at ",i,ii,iii,iiii," was selected.")
                if self.selected_slot==str(i)+","+str(ii)+","+str(iii)+","+str(iiii):
                    self.selected_slot=None
                else:
                    self.selected_slot=str(i)+","+str(ii)+","+str(iii)+","+str(iiii)
                    if self.selected_number != None:
                        self.play()
                for widget in self.root.winfo_children():
                    widget.destroy()
                self.render()
        else:
            print("There was a error somewhere.")

    # selectes a number
    def select_number(self,number):
        if not self.error:
            try:
                number=int(number)
            except:
                if not self.overideErrors:
                    self.error = True
                    print("Soduko input error, runner disabled.")
            if not self.error:
                if self.debugMessages:
                    print("Selecting number ",int(number))
                if self.selected_number==int(number):
                    self.selected_number=None
                else:
                    self.selected_number=int(number)
                    if self.selected_slot != None:
                        self.play()
                for widget in self.root.winfo_children():
                    widget.destroy()
                self.render()
        else:
            print("There was an error somewhere.")

    # sets a slot to a number,
    # and also checks for winning and loosing.
    def play(self):
        if not self.error:
            path_to=self.selected_slot.split(',')
            self.boxes[int(path_to[0])][int(path_to[1])][int(path_to[2])][int(path_to[3])]=self.selected_number
            self.selected_slot=None
            game_status=self.checkGameStatus(int(path_to[0]),int(path_to[1]),int(path_to[2]),int(path_to[3]))
            print(game_status)
            if game_status!="None":
                if game_status:
                    self.onGameWin()
                else:
                    self.onGameLoss()
            else:
                for widget in self.root.winfo_children():
                    widget.destroy()
                self.render()
        else:
            print("There was an error somewhere.")
    # checks if the game was won
    # or lost.
    def checkGameStatus(self,i,ii,iii,iiii):
        if not self.error:
            win="None"

            vertical_duplicates=False
            horizontal_duplicates=False
            box_duplicates=False

            vertical_data=[]
            horizontal_data=[]
            box_data=[]

            for box_row in self.boxes[i][ii]:
                for box_item in box_row:
                    if box_item!=-1:
                        if box_item in box_data:
                            box_duplicates=True
                        box_data.append(box_item)

            for vertical_box_row_box in self.boxes[i]:
                for v_i in range(len(vertical_box_row_box)):
                    for v_ii in range(len(vertical_box_row_box[v_i])):
                        if v_ii is iiii:
                            if vertical_box_row_box[v_i][v_ii]!=-1:
                                if vertical_box_row_box[v_i][v_ii] in vertical_data:
                                    vertical_duplicates=True
                                vertical_data.append(vertical_box_row_box[v_i][v_ii])

            for h_i in range(len(self.boxes)):
                for h_ii in range(len(self.boxes[h_i])):
                    if h_ii is ii:
                        for horizontal_box_row_item in self.boxes[h_i][h_ii][iii]:
                            if horizontal_box_row_item!=-1:
                                if horizontal_box_row_item in horizontal_data:
                                    horizontal_duplicates=True
                                horizontal_data.append(horizontal_box_row_item)

            if box_duplicates or horizontal_duplicates or vertical_duplicates:
                win=False
            
            negative_one_found=False
            for nof_i in self.boxes:
                for nof_ii in nof_i:
                    for nof_iii in nof_ii:
                        for nof_iiii in nof_iii:
                            if nof_iiii==-1:
                                negative_one_found=True
            
            if negative_one_found:
                return win
            elif win=="None":
                return True
            else:
                return False
        else:
            print("There was an error somewhere.")

    # default game events, this should
    # be changed.
    def onGameWin(self):
        self.root.destroy()
        _tk=Tk()
        _tk.title(" ")
        Label(_tk,text="You won").pack()
        Button(_tk,text="Close",command=lambda t=_tk:t.destroy()).pack()
        _tk.mainloop()
    def onGameLoss(self):
        self.root.destroy()
        _tk=Tk()
        _tk.title(" ")
        Label(_tk,text="You lost").pack()
        Button(_tk,text="Close",command=lambda t=_tk:t.destroy()).pack()
        _tk.mainloop()

# example usage:

soduko=Soduko("3*3+3*2",Tk(),SodukoOptions(debugMessages=True))
soduko.start()