import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        """
        Hàm khởi tạo, thiết lập các thành phần chính của game.
        """
        self.root = root
        self.root.title("Game XO 5x5 (Refactored)")
        
        # Hằng số cho bàn cờ
        self.BOARD_SIZE = 5
        
        # Biến trạng thái của game
        self.current_player = "X"
        self.moves_made = 0
        self.game_over = False
        
        # Mảng 2 chiều để lưu trạng thái logic và các nút
        self.board = [["" for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.buttons = [[None for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        
        self.create_menu()
        self.create_board_widgets()

    def create_menu(self):
        """Tạo menu bar với tùy chọn chơi lại."""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        options_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Restart Game", command=self.reset_game)

    def create_board_widgets(self):
        """Tạo và sắp xếp các nút trên bàn cờ."""
        frame = tk.Frame(self.root)
        frame.pack()
        
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                # Sử dụng lambda để truyền đúng tọa độ (hàng, cột) cho mỗi nút
                button = tk.Button(
                    frame, 
                    text=" ", 
                    font=("Helvetica", 20), 
                    height=2, 
                    width=5,
                    command=lambda r=row, c=col: self.on_button_click(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        """Xử lý sự kiện khi một ô trên bàn cờ được nhấn."""
        # Chỉ cho phép đi khi ô còn trống và game chưa kết thúc
        if self.board[row][col] == "" and not self.game_over:
            # Cập nhật trạng thái logic và giao diện
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.moves_made += 1
            
            # Kiểm tra kết quả sau nước đi
            if self.check_winner(row, col):
                self.end_game(f"Player {self.current_player} wins!")
            elif self.moves_made == self.BOARD_SIZE * self.BOARD_SIZE:
                self.end_game("It's a draw!")
            else:
                # Đổi lượt cho người chơi tiếp theo
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        """Kiểm tra xem người chơi hiện tại có thắng sau nước đi ở (row, col) không."""
        player = self.current_player
        
        # 1. Kiểm tra hàng (check the entire row)
        if all(self.board[row][c] == player for c in range(self.BOARD_SIZE)):
            return True
            
        # 2. Kiểm tra cột (check the entire column)
        if all(self.board[r][col] == player for r in range(self.BOARD_SIZE)):
            return True
            
        # 3. Kiểm tra đường chéo chính (chỉ khi ô nằm trên đường chéo này)
        if row == col:
            if all(self.board[i][i] == player for i in range(self.BOARD_SIZE)):
                return True
                
        # 4. Kiểm tra đường chéo phụ (chỉ khi ô nằm trên đường chéo này)
        if row + col == self.BOARD_SIZE - 1:
            if all(self.board[i][self.BOARD_SIZE - 1 - i] == player for i in range(self.BOARD_SIZE)):
                return True
                
        return False

    def end_game(self, message):
        """Kết thúc game, hiển thị thông báo và vô hiệu hóa bàn cờ."""
        self.game_over = True
        messagebox.showinfo("Game Over", message)
        self.disable_buttons()

    def disable_buttons(self):
        """Vô hiệu hóa tất cả các nút trên bàn cờ."""
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                self.buttons[row][col].config(state=tk.DISABLED)

    def reset_game(self):
        """Thiết lập lại bàn cờ để chơi ván mới."""
        self.current_player = "X"
        self.moves_made = 0
        self.game_over = False
        
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                self.board[row][col] = ""
                self.buttons[row][col].config(text=" ", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()