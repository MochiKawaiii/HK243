import tkinter as tk
from tkinter import messagebox

class GomokuGame:
    def __init__(self, root, board_size=8, win_length=5):
        """
        Hàm khởi tạo, thiết lập các thành phần chính của game.
        """
        self.root = root
        self.board_size = board_size
        self.win_length = win_length
        self.root.title(f'Game XO {board_size}x{board_size} ({win_length}-in-a-row to win) - Refactored')
        
        # Biến trạng thái của game
        self.current_player = "X"
        self.moves_made = 0
        self.game_over = False
        
        # Mảng 2 chiều để lưu các nút
        self.buttons = [[None for _ in range(board_size)] for _ in range(board_size)]
        
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
        
        for row in range(self.board_size):
            for col in range(self.board_size):
                button = tk.Button(
                    frame, 
                    text=" ", 
                    font=("Helvetica", 10), 
                    height=2, 
                    width=4,
                    command=lambda r=row, c=col: self.on_button_click(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        """Xử lý sự kiện khi một ô trên bàn cờ được nhấn."""
        if self.buttons[row][col]['text'] == " " and not self.game_over:
            # Cập nhật giao diện
            self.buttons[row][col].config(text=self.current_player)
            self.moves_made += 1
            
            # Kiểm tra kết quả sau nước đi
            if self.check_winner(row, col):
                self.end_game(f"Player {self.current_player} wins!")
            elif self.moves_made == self.board_size * self.board_size:
                self.end_game("It's a draw!")
            else:
                # Đổi lượt cho người chơi tiếp theo
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        """
        Kiểm tra xem người chơi hiện tại có thắng không bằng cách kiểm tra 4 hướng
        (ngang, dọc, chéo chính, chéo phụ) từ ô vừa đánh.
        """
        player = self.current_player
        
        # Các hướng để kiểm tra: (delta_row, delta_col)
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)] # Ngang, Dọc, Chéo \, Chéo /
        
        for dr, dc in directions:
            count = 1 # Bắt đầu đếm từ ô vừa đánh
            
            # Đếm về phía trước
            for i in range(1, self.win_length):
                r, c = row + i * dr, col + i * dc
                if 0 <= r < self.board_size and 0 <= c < self.board_size and self.buttons[r][c]['text'] == player:
                    count += 1
                else:
                    break
            
            # Đếm về phía sau
            for i in range(1, self.win_length):
                r, c = row - i * dr, col - i * dc
                if 0 <= r < self.board_size and 0 <= c < self.board_size and self.buttons[r][c]['text'] == player:
                    count += 1
                else:
                    break
            
            # Nếu đủ số ô liên tiếp thì thắng
            if count >= self.win_length:
                return True
                
        return False

    def end_game(self, message):
        """Kết thúc game, hiển thị thông báo và vô hiệu hóa bàn cờ."""
        self.game_over = True
        messagebox.showinfo("Game Over", message)
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def reset_game(self):
        """Thiết lập lại bàn cờ để chơi ván mới."""
        self.current_player = "X"
        self.moves_made = 0
        self.game_over = False
        
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].config(text=" ", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    # Khởi tạo game với bàn cờ 8x8 và luật thắng 5 ô
    game = GomokuGame(root, board_size=8, win_length=5)
    root.mainloop()