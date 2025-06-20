# README – Bài toán N-Queens (TH_2.ipynb)

## 🛠️ Công nghệ sử dụng

| Thành phần | Mục đích |
|------------|----------|
| **Python ≥ 3.8** | Ngôn ngữ lập trình chính |
| **Jupyter Notebook** | Môi trường tương tác để mô tả lý thuyết & chạy thử mã |
| **NumPy** | Biểu diễn bàn cờ dưới dạng ma trận, hỗ trợ thao tác mảng |
| (✔️) Thư viện chuẩn `typing`, `itertools`, … | Xử lý logic, không cần cài thêm |

> *Cài đặt nhanh*: `pip install numpy notebook`

---

## ⚙️ Cấu trúc chính notebook

| Cell | Vai trò chính |
|------|---------------|
| `is_valid_state(state, n)` | Kiểm tra trạng thái hiện tại đã đặt đủ **n** quân hậu hợp lệ hay chưa |
| `get_candidates(state, n)` | Sinh danh sách cột **an toàn** cho quân hậu kế tiếp |
| `search(state, solutions, n)` | Thuật toán **Backtracking** duyệt toàn bộ không gian tìm kiếm |
| `solve(n)` | Bao hàm, khởi tạo & trả về toàn bộ lời giải |
| Block **main** | Cho phép chạy notebook như script `.py`, in 2 lời giải ngẫu nhiên & hiển thị bàn cờ |

---

## 🚀 Cách hoạt động của code

1. **Biểu diễn trạng thái**  
   - `state` là *list* độ dài `r`, trong đó `state[i] = c` nghĩa là đặt quân Hậu ở hàng *i*, cột *c*.
2. **Sinh "ứng viên" (generate candidates)**  `get_candidates` so khớp các cột chưa bị khống chế theo 3 điều kiện:  
   - trùng cột  
   - trùng đường chéo chính  
   - trùng đường chéo phụ
3. **Đệ quy Backtracking**  
   - Thêm từng ứng viên vào `state`, gọi lại `search`.  
   - Khi `len(state) == n` → thêm vào `solutions` rồi *backtrack* (pop).
4. **Kết quả**  
   - Trả về `solutions` (danh sách danh sách), mỗi lời giải chứa vị trí cột của  *n* quân Hậu.

### Độ phức tạp

- **Thời gian (worst-case)**: O(N!) – giảm đáng kể nhờ cắt tỉa sớm.
- **Không gian**: O(N) cho ngăn xếp đệ quy, O(S × N) để lưu **S** lời giải.

---

## ▶️ Hướng dẫn chạy thử

```bash
# 1. Cài thư viện (nếu chưa có)
pip install numpy notebook

# 2. Mở notebook
jupyter notebook TH_2.ipynb
```

- Thay đổi giá trị `n` (ví dụ 4 hoặc 8) trong hàm `solve(n)` hoặc ô nhập `input()` để kiểm thử.
- Có thể **export** thành file Python:  
  `jupyter nbconvert --to script TH_2.ipynb`

---
