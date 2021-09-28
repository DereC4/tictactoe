from tkinter import * 
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
#root.iconbitmap('')

clicked = True
count = 0

def disableAllButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkWin(word):
    global winner
    winner = False
    if (b1["text"]== word and b2['text']== word and b3["text"]==word):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Congrats!", word+" wins!")
        disableAllButtons()
    elif (b4["text"]== word and b5['text']== word and b6["text"]==word):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Congrats!", word+" wins!")
        disableAllButtons()
    elif (b7["text"]== word and b8['text']== word and b9["text"]==word):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Congrats!", word+" wins!")
        disableAllButtons()
    elif (b1["text"]== word and b5['text']== word and b9["text"]==word):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Congrats!", word+" wins!")
        disableAllButtons()
    elif (b2["text"]== word and b5['text']== word and b8["text"]==word):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Congrats!", word+" wins!")
        disableAllButtons()
    elif (b1["text"]== word and b4['text']== word and b7["text"]==word):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Congrats!", word+" wins!")
        disableAllButtons()
    elif (b3["text"]== word and b6['text']== word and b9["text"]==word):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Congrats!", word+" wins!")
        disableAllButtons()
    elif (b3["text"]== word and b5['text']== word and b7["text"]==word):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Congrats!", word+" wins!")
        disableAllButtons()
    if (count == 9 and winner == False):
        messagebox.showinfo("It's a tie!", "Tie! Try to restart the round!")
        disableAllButtons()

def click(b):
    global clicked, count
    if(b["text"]== " " and clicked == True):
        b['text'] = "X"
        clicked = False
        count += 1
        checkWin("X")
    elif(b["text"] == " " and clicked == False):
        b['text'] = "O"
        clicked = True
        count += 1
        checkWin("O")
    else:
        messagebox.showerror("Uh oh!","You can't select that box!\nPick another one!")
        
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    # Buttons
    b1 = Button(root, text = " ", font=("Helvetica",20), height=3, width = 6, bg = "SystemButtonFace", command = lambda: click(b1))
    b2 = Button(root, text = " ", font=("Helvetica",20), height=3, width = 6, bg = "SystemButtonFace", command = lambda: click(b2))
    b3 = Button(root, text = " ", font=("Helvetica",20), height=3, width = 6, bg = "SystemButtonFace", command = lambda: click(b3))
    b4 = Button(root, text = " ", font=("Helvetica",20), height=3, width = 6, bg = "SystemButtonFace", command = lambda: click(b4))
    b5 = Button(root, text = " ", font=("Helvetica",20), height=3, width = 6, bg = "SystemButtonFace", command = lambda: click(b5))
    b6 = Button(root, text = " ", font=("Helvetica",20), height=3, width = 6, bg = "SystemButtonFace", command = lambda: click(b6))
    b7 = Button(root, text = " ", font=("Helvetica",20), height=3, width = 6, bg = "SystemButtonFace", command = lambda: click(b7))
    b8 = Button(root, text = " ", font=("Helvetica",20), height=3, width = 6, bg = "SystemButtonFace", command = lambda: click(b8))
    b9 = Button(root, text = " ", font=("Helvetica",20), height=3, width = 6, bg = "SystemButtonFace", command = lambda: click(b9))
    # Grid
    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)
    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)
    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

def exit():
    root.destroy()

mainMenu = Menu(root)
root.config(menu=mainMenu)
optionsMenu = Menu(mainMenu, tearoff= False)
mainMenu.add_cascade(label="Options", menu = optionsMenu)
optionsMenu.add_command(label="Restart Round", command = reset)
optionsMenu.add_command(label="Quit Game", command = exit)

reset()
root.mainloop()