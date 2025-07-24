from tkinter import *
from tkinter import messagebox

# --- CÁC THAM SỐ CỦA BÀN CỜ ---
BOARD_SIZE = 8
WIN_LENGTH = 5
TOTAL_CELLS = BOARD_SIZE * BOARD_SIZE
# ---------------------------------

root = Tk()
root.title(f'Game XO {BOARD_SIZE}x{BOARD_SIZE} ({WIN_LENGTH}-in-a-row to win)')

# Khai báo các biến toàn cục
buttons = []
clicked = True
count = 0
win = False

# Hàm để bắt đầu hoặc chơi lại trò chơi
def start():
    global buttons, clicked, count, win
    
    # Xóa các nút cũ nếu có
    for widget in root.winfo_children():
        if isinstance(widget, Button):
            widget.destroy()

    # Reset lại trạng thái trò chơi
    buttons = []
    clicked = True
    count = 0
    win = False

    # Xây dựng các nút cho trò chơi và đặt vào lưới
    for i in range(TOTAL_CELLS):
        button = Button(root, text=" ", font=("Helvetica", 10), height=2, width=4, bg="SystemButtonFace", command=lambda b=i: buttonClicked(b))
        button.grid(row=i//BOARD_SIZE, column=i%BOARD_SIZE)
        buttons.append(button)

# Hàm vô hiệu hóa tất cả các nút khi game kết thúc
def disableButtons():
    for button in buttons:
        button.config(state=DISABLED)

# Hàm kiểm tra người chiến thắng (5 ô liên tiếp)
def checkWinner():
    global win
    
    # Tạo danh sách tất cả các điều kiện thắng một cách tự động
    winning_conditions = []
    num_starts = BOARD_SIZE - WIN_LENGTH + 1 # Số vị trí bắt đầu có thể có trên 1 hàng/cột

    # 1. Hàng ngang
    for row in range(BOARD_SIZE):
        for col in range(num_starts):
            condition = [row * BOARD_SIZE + col + i for i in range(WIN_LENGTH)]
            winning_conditions.append(tuple(condition))

    # 2. Hàng dọc
    for col in range(BOARD_SIZE):
        for row in range(num_starts):
            condition = [(row + i) * BOARD_SIZE + col for i in range(WIN_LENGTH)]
            winning_conditions.append(tuple(condition))

    # 3. Đường chéo (từ trên trái xuống dưới phải)
    for row in range(num_starts):
        for col in range(num_starts):
            condition = [(row + i) * BOARD_SIZE + (col + i) for i in range(WIN_LENGTH)]
            winning_conditions.append(tuple(condition))
            
    # 4. Đường chéo (từ trên phải xuống dưới trái)
    for row in range(num_starts):
        for col in range(WIN_LENGTH - 1, BOARD_SIZE):
            condition = [(row + i) * BOARD_SIZE + (col - i) for i in range(WIN_LENGTH)]
            winning_conditions.append(tuple(condition))

    # Kiểm tra cho cả 'X' và 'O'
    for player in ["X", "O"]:
        for condition in winning_conditions:
            if all(buttons[i]["text"] == player for i in condition):
                win = True
                winner_name = "Player 1" if player == "X" else "Player 2"
                messagebox.showinfo("OX Game", f"{winner_name} WINNER!!")
                disableButtons()
                return # Thoát khỏi hàm ngay khi tìm thấy người thắng

# Hàm kiểm tra nếu hòa
def checkDraw():
    global count, win
    if count == TOTAL_CELLS and win == False:
        messagebox.showerror("OX Game", "DRAW!!")
        disableButtons()

# Hàm xử lý khi một nút được nhấn
def buttonClicked(button_index):
    global clicked, count
    
    button = buttons[button_index]
    
    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkWinner()
        if not win: # Chỉ kiểm tra hòa nếu chưa có ai thắng
            checkDraw()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkWinner()
        if not win: # Chỉ kiểm tra hòa nếu chưa có ai thắng
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