# Game XO

Kho lưu trữ này chứa nhiều triển khai trò chơi Tic-Tac-Toe (XO) và biến thể Gomoku trên các kích thước bàn khác nhau (4×4, 5×5, 6×6, 8×8). Với mỗi kích thước, có hai phiên bản:

- **Phiên bản gốc**: script Tkinter đơn giản với các điều kiện thắng được mã hóa cứng.
- **Phiên bản refactor** (`*_lamlai`): triển khai hướng đối tượng, kiểm tra động, logic có thể tái sử dụng.

---

## Nội dung

| Tệp                                  | Mô tả                                                 |
|--------------------------------------|-------------------------------------------------------|
| `Game_XOXO_4x4.py`                   | Tic-Tac-Toe 4×4, thắng 4 ô (mã cứng)                  |
| `Game_XOXO_4x4_lamlai.py`            | Tic-Tac-Toe 4×4, refactor OOP, kiểm tra động           |
| `Game_XOXO_5x5.py`                   | Tic-Tac-Toe 5×5, thắng 5 ô (mã cứng)                  |
| `Game_XOXO_5x5_lamlai.py`            | Tic-Tac-Toe 5×5, refactor OOP, kiểm tra động           |
| `Game_XOXO_6x6.py`                   | Gomoku 6×6, thắng 5 ô (vòng lặp logic cứng)           |
| `Game_XOXO_6x6_lamlai.py`            | Gomoku 6×6, refactor OOP, tham số hóa độ dài chiến thắng |
| `Game_XOXO_8x8.py`                   | Gomoku 8×8, thắng 5 ô (sinh tự động điều kiện)         |
| `Game_XOXO_8x8_lamlai.py`            | Gomoku 8×8, refactor OOP, tham số hóa cơ chế           |

---

## Đánh giá tính đúng đắn

### 1. `Game_XOXO_4x4.py` (Phiên bản gốc)
- **Điều kiện thắng**: Tất cả các hàng ngang, cột dọc và hai đường chéo chính (4 ô) được liệt kê rõ ràng.
- **Kiểm tra hòa**: Đếm số nước đi và thông báo hòa sau 16 nước đi nếu không có ai thắng.
- **Trường hợp biên**: Không cho phép ghi đè ô; hiển thị thông báo lỗi khi bấm ô không hợp lệ.

**Kết luận**: ✅ Đúng và hoạt động, nhưng lặp mã nhiều và khó mở rộng cho các kích thước khác.

### 2. `Game_XOXO_4x4_lamlai.py` (Phiên bản refactor)
- **Cấu trúc**: Lớp `TicTacToeGame` đóng gói trạng thái bàn, giao diện và logic.
- **Logic thắng**: Kiểm tra hàng, cột và chéo dựa trên kích thước bàn một cách động.
- **Linh hoạt**: Dễ thay đổi hằng số `BOARD_SIZE` để mở rộng.

**Kết luận**: ✅ Đúng, dễ bảo trì, ít dòng mã, có thể dùng lại cho các kích thước khác.

### 3. `Game_XOXO_5x5.py` (Phiên bản gốc)
- **Điều kiện thắng**: Tất cả 5 hàng, 5 cột và hai đường chéo chính được mã hóa thủ công.
- **Kiểm tra hòa**: Hòa khi đủ 25 nước đi mà không có người thắng.
- **Trường hợp biên**: Tương tự phiên bản 4×4.

**Kết luận**: ✅ Đúng cho 5×5, nhưng vẫn lặp mã và khó mở rộng.

### 4. `Game_XOXO_5x5_lamlai.py` (Phiên bản refactor)
- **Cấu trúc**: Lớp OOP với `BOARD_SIZE = 5`.
- **Logic thắng**: Dùng vòng lặp và `all()` để kiểm tra hàng, cột, chéo.
- **Linh hoạt**: Chỉ cần chỉnh `BOARD_SIZE` là dùng lại.

**Kết luận**: ✅ Đúng, mã sạch, sẵn sàng mở rộng.

### 5. `Game_XOXO_6x6.py` (Phiên bản gốc)
- **Loại trò chơi**: Gomoku trên lưới 6×6, thắng 5 ô liền.
- **Logic thắng**: Duyệt 4 hướng để kiểm tra 5 dấu liên tiếp.
- **Tham số**: `board_size` và `win_length` là tham số, nhưng giao diện vẫn dùng kích thước nút cố định.

**Kết luận**: ✅ Logic đúng cho 6×6, giao diện có thể cần điều chỉnh cho kích thước khác.

### 6. `Game_XOXO_6x6_lamlai.py` (Phiên bản refactor)
- **Cấu trúc**: Lớp `GomokuGame` tham số hóa theo `board_size` và `win_length`.
- **Logic thắng**: Kiểm tra trên ma trận `board` thay vì trực tiếp trên nút.
- **Tách biệt**: Phân tách rõ ràng giữa logic và giao diện.

**Kết luận**: ✅ Đúng và cấu trúc tốt, dễ mở rộng.

### 7. `Game_XOXO_8x8.py` (Phiên bản gốc)
- **Loại trò chơi**: Gomoku 8×8, thắng 5 ô.
- **Logic thắng**: Sinh tự động tập hợp các bộ chỉ số thắng cho hàng, cột và chéo.
- **Kiểm tra hòa**: Hòa sau 64 nước đi.

**Kết luận**: ✅ Đúng và năng động; sinh điều kiện thắng vững chắc cho mọi cặp `(BOARD_SIZE, WIN_LENGTH)`.

### 8. `Game_XOXO_8x8_lamlai.py` (Phiên bản refactor)
- **Cấu trúc**: Lớp `GomokuGame` tham số `(board_size=8, win_length=5)`.
- **Logic thắng**: Dùng phương pháp đếm tương tự như bản 6×6.
- **Dễ bảo trì**: Mã ngắn gọn, phân tách rõ ràng.

**Kết luận**: ✅ Đúng, dễ bảo trì, hoàn toàn tham số hóa.

---

## So sánh giữa bản gốc và bản refactor

| Yếu tố            | Phiên bản gốc                             | Phiên bản refactor                        |
|-------------------|-------------------------------------------|-------------------------------------------|
| Trùng lặp mã      | Cao (mã điều kiện thắng thủ công)         | Thấp (vòng lặp và tham số hóa)            |
| Khả năng mở rộng  | Kém (phải viết lại cho từng kích thước)   | Rất tốt (chỉnh hằng số là đủ)             |
| Khả năng đọc      | Trung bình (mã lặp nhiều)                 | Cao (cấu trúc lớp và phương thức rõ ràng) |
| Dễ bảo trì        | Khó (logic cứng khớp khắp nơi)            | Dễ (đường logic duy nhất cho mọi kích thước)|
| Tính đúng đắn     | ✅                                        | ✅                                        |

*Tất cả các triển khai đã được kiểm tra để phát hiện đúng thắng và hòa theo quy tắc quy định.*