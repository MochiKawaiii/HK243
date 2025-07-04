# Lab 3 – Genetic Algorithm

## Công nghệ sử dụng

- **Python ≥ 3.9**
- **numpy** – thao tác vector/quần thể
- **matplotlib** – vẽ biểu đồ quá trình hội tụ
- **Jupyter Lab/Notebook** – thực thi tương tác

---

## Cấu trúc chính notebook (`lab3.ipynb`)

1. **Khởi tạo & Tham số GA** – tạo quần thể, thiết lập `population_size`, `mutation_rate`, số thế hệ.
2. **Hàm fitness** – hai ví dụ có sẵn (1 biến và 2 biến).
3. **Vòng lặp GA** – chu kỳ Chọn lọc → Lai ghép → Đột biến → Cập nhật quần thể.
4. **Trực quan hoá** – đồ thị fitness theo thế hệ.
5. **Bài tập** – cell chứa TODO để bạn:
   - Thay hàm fitness mới.
   - Chỉnh tham số GA.
   - Trực quan hoá thêm (2‑D/3‑D).

---

## Cách hoạt động của code (phần Bài tập)

1. Mở cell **Bài tập** ở cuối notebook.
2. Thay đổi hàm `objective()` hoặc thêm biến tuỳ nhu cầu.
3. Điều chỉnh tham số ở ô thiết lập ban đầu.
4. Chạy lại các cell GA.
5. Quan sát biểu đồ fitness để đánh giá tác động của thay đổi.

---

## Hướng dẫn chạy thử

```bash
# Tạo môi trường ảo
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Cài đặt phụ thuộc
pip install numpy matplotlib jupyter

# Mở notebook
jupyter lab lab3.ipynb   # hoặc: jupyter notebook lab3.ipynb
```

Sau khi notebook mở, nhấn **Run All** hoặc chạy từng cell, hoàn thành phần Bài tập và lưu kết quả.
