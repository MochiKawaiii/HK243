from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('OX Game 5x5')

# Khai báo các biến toàn cục
clicked = True
count = 0
win = False

# Hàm để bắt đầu hoặc chơi lại trò chơi
def start():
    # Khai báo các biến toàn cục sẽ được sử dụng và thay đổi
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, button21, button22, button23, button24, button25
    global clicked, count, win
    
    # Reset lại trạng thái trò chơi
    clicked = True
    count = 0
    win = False

    # Xây dựng các nút cho trò chơi
    button1 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button1))
    button2 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button2))
    button3 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button3))
    button4 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button4))
    button5 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button5))
    button6 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button6))
    button7 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button7))
    button8 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button8))
    button9 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button9))
    button10 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button10))
    button11 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button11))
    button12 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button12))
    button13 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button13))
    button14 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button14))
    button15 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button15))
    button16 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button16))
    button17 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button17))
    button18 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button18))
    button19 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button19))
    button20 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button20))
    button21 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button21))
    button22 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button22))
    button23 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button23))
    button24 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button24))
    button25 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: buttonClicked(button25))

    # Sắp xếp các nút trên màn hình cho trò chơi
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=0, column=4)
    button6.grid(row=1, column=0)
    button7.grid(row=1, column=1)
    button8.grid(row=1, column=2)
    button9.grid(row=1, column=3)
    button10.grid(row=1, column=4)
    button11.grid(row=2, column=0)
    button12.grid(row=2, column=1)
    button13.grid(row=2, column=2)
    button14.grid(row=2, column=3)
    button15.grid(row=2, column=4)
    button16.grid(row=3, column=0)
    button17.grid(row=3, column=1)
    button18.grid(row=3, column=2)
    button19.grid(row=3, column=3)
    button20.grid(row=3, column=4)
    button21.grid(row=4, column=0)
    button22.grid(row=4, column=1)
    button23.grid(row=4, column=2)
    button24.grid(row=4, column=3)
    button25.grid(row=4, column=4)

# Hàm vô hiệu hóa tất cả các nút khi game kết thúc
def disableButtons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    button10.config(state=DISABLED)
    button11.config(state=DISABLED)
    button12.config(state=DISABLED)
    button13.config(state=DISABLED)
    button14.config(state=DISABLED)
    button15.config(state=DISABLED)
    button16.config(state=DISABLED)
    button17.config(state=DISABLED)
    button18.config(state=DISABLED)
    button19.config(state=DISABLED)
    button20.config(state=DISABLED)
    button21.config(state=DISABLED)
    button22.config(state=DISABLED)
    button23.config(state=DISABLED)
    button24.config(state=DISABLED)
    button25.config(state=DISABLED)

# Hàm kiểm tra người chiến thắng
def checkWinner():
    global win

    # Các điều kiện mà người chơi 1 [X] chiến thắng
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" and button10["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button11["text"] == "X" and button12["text"] == "X" and button13["text"] == "X" and button14["text"] == "X" and button15["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button16["text"] == "X" and button17["text"] == "X" and button18["text"] == "X" and button19["text"] == "X" and button20["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button21["text"] == "X" and button22["text"] == "X" and button23["text"] == "X" and button24["text"] == "X" and button25["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button1["text"] == "X" and button6["text"] == "X" and button11["text"] == "X" and button16["text"] == "X" and button21["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button2["text"] == "X" and button7["text"] == "X" and button12["text"] == "X" and button17["text"] == "X" and button22["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button3["text"] == "X" and button8["text"] == "X" and button13["text"] == "X" and button18["text"] == "X" and button23["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button4["text"] == "X" and button9["text"] == "X" and button14["text"] == "X" and button19["text"] == "X" and button24["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button5["text"] == "X" and button10["text"] == "X" and button15["text"] == "X" and button20["text"] == "X" and button25["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button1["text"] == "X" and button7["text"] == "X" and button13["text"] == "X" and button19["text"] == "X" and button25["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
    elif button5["text"] == "X" and button9["text"] == "X" and button13["text"] == "X" and button17["text"] == "X" and button21["text"] == "X":
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()

    # Các điều kiện mà người chơi 2 [O] chiến thắng
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button6["text"] == "O" and button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" and button10["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button11["text"] == "O" and button12["text"] == "O" and button13["text"] == "O" and button14["text"] == "O" and button15["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button16["text"] == "O" and button17["text"] == "O" and button18["text"] == "O" and button19["text"] == "O" and button20["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button21["text"] == "O" and button22["text"] == "O" and button23["text"] == "O" and button24["text"] == "O" and button25["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button1["text"] == "O" and button6["text"] == "O" and button11["text"] == "O" and button16["text"] == "O" and button21["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button2["text"] == "O" and button7["text"] == "O" and button12["text"] == "O" and button17["text"] == "O" and button22["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button3["text"] == "O" and button8["text"] == "O" and button13["text"] == "O" and button18["text"] == "O" and button23["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button4["text"] == "O" and button9["text"] == "O" and button14["text"] == "O" and button19["text"] == "O" and button24["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button5["text"] == "O" and button10["text"] == "O" and button15["text"] == "O" and button20["text"] == "O" and button25["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button1["text"] == "O" and button7["text"] == "O" and button13["text"] == "O" and button19["text"] == "O" and button25["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
    elif button5["text"] == "O" and button9["text"] == "O" and button13["text"] == "O" and button17["text"] == "O" and button21["text"] == "O":
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()

# Hàm kiểm tra nếu hòa
def checkDraw():
    global count, win
    if count == 25 and win == False:
        messagebox.showerror("OX Game", "DRAW!!")
        disableButtons()

# Hàm xử lý khi một nút được nhấn
def buttonClicked(button):
    global clicked, count
    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkWinner()
        checkDraw()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("OX Game", "LỖI!! Vui lòng chọn lại ô khác.")

# --- Phần chính của chương trình ---

# Tạo menu trò chơi
gameMenu = Menu(root)
root.config(menu=gameMenu)

# Tạo menu tùy chọn "Options"
optionMenu = Menu(gameMenu, tearoff=False)
gameMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Restart Game", command=start)

# Bắt đầu trò chơi lần đầu tiên
start()

# Chạy vòng lặp chính của cửa sổ
root.mainloop()