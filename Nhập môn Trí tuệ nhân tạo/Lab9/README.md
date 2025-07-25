# Thực hành 20–24: Tìm kiếm và Học tăng cường

## 1. Công nghệ sử dụng
- **Ngôn ngữ**: Python 3  
- **Thư viện**:
  - `numpy`: Xử lý mảng, ma trận và tính toán số học.  
  - `random`: Sinh số ngẫu nhiên cho việc khởi tạo trạng thái và chính sách ε-greedy.  
  - `collections.deque`: Cấu trúc hàng đợi để triển khai thuật toán BFS (First-In-First-Out).  

## 2. Tổng quan hoạt động

### Thực hành 20: Mê cung 6x6 với DFS
- **Mô tả bài toán**: Tìm đường đi từ vị trí bắt đầu `(0,0)` đến đích `(0,5)` trong mê cung kích thước 6x6, với ô chặn (1) và ô trống (0).  
- **Thuật toán**: **Depth-First Search (DFS)**  
  - Khởi tạo ma trận mê cung và danh sách `obstacles` chứa các ô chặn.  
  - Dùng hàm `is_valid(cell)` để kiểm tra ô hợp lệ (trong giới hạn và không bị chặn).  
  - Sử dụng đệ quy `dfs(cell)`:
    1. Nếu `cell == goal`, thêm vào đường đi và trả về True.  
    2. Đánh dấu `cell` đã thăm (set `visited`).  
    3. Thử lần lượt các bước di chuyển: lên, xuống, trái, phải.  
    4. Nếu một hướng dẫn đến đích, thêm `cell` vào `path` khi quay lui.  
  - Cuối cùng, nếu tìm được đường đi, đảo ngược danh sách `path` để in theo thứ tự từ start đến goal.  
- **Ưu điểm**: 
  - Cài đặt đơn giản, sử dụng ít bộ nhớ (đệ quy hoặc ngăn xếp).  
- **Nhược điểm**: 
  - Không đảm bảo tìm đường ngắn nhất; có thể lạc sâu vào nhánh không dẫn đến đích.

### Thực hành 21: Mê cung 6x6 với BFS
- **Mô tả bài toán**: Tương tự Thực hành 20, nhưng tìm đường ngắn nhất.  
- **Thuật toán**: **Breadth-First Search (BFS)**  
  - Sử dụng `deque` làm hàng đợi FIFO.  
  - Mỗi mục trong hàng đợi lưu cặp `(cell, path)` - ô hiện tại và đường đi tới đây.  
  - Lấy phần tử đầu hàng đợi, nếu `cell == goal`, trả về `path`.  
  - Với mỗi ô láng giềng hợp lệ chưa thăm, thêm vào hàng đợi và mark `visited`.  
  - Quá trình tiếp tục cho đến khi tìm ra đường đi.  
- **Ưu điểm**: 
  - Đảm bảo tìm **đường đi ngắn nhất** (số bước ít nhất).  
- **Nhược điểm**: 
  - Tốn bộ nhớ do phải lưu nhiều trạng thái trung gian (toàn bộ cấp độ hiện tại).

### Thực hành 22: FSSP_BFS trên lưới 5x5
- **Mô tả bài toán**: Lưới 5x5, ô chặn tại các vị trí nhất định, tìm đường đi ngắn nhất từ góc trên trái `(0,0)` sang góc dưới phải `(4,4)`.  
- **Kỹ thuật**: **Forward State Space Planning (FSSP)** kết hợp BFS  
  - Mỗi ô trong lưới là một trạng thái.  
  - Khởi tạo hàng đợi với `start` và thuật toán BFS để mở rộng trạng thái theo mức.  
  - Dùng `visited` để tránh lặp.  
  - Thêm cha–con để truy vết đường đi khi đạt `goal`.  
- **Kết quả**: Đường đi ngắn nhất trên lưới 5x5.

### Thực hành 23: FSSP_BFS trên đồ thị tổng quát
- **Mô tả bài toán**: Đồ thị tổng quát cho trước với danh sách kề, tìm đường đi ngắn nhất từ đỉnh `A` đến `F`.  
- **Kỹ thuật**: BFS trên đồ thị  
  - Sử dụng hàng đợi lưu `(node, path)`.  
  - Thăm lần lượt đỉnh kề, mark `visited`.  
  - Khi gặp `goal`, trả về chuỗi đỉnh đi qua.  
- **Ứng dụng**: Bài toán tìm đường trên mạng lưới, mạng xã hội, biểu đồ phụ thuộc,...

### Thực hành 24: Q-Learning trong môi trường tuyến tính 6 trạng thái
- **Mô tả bài toán**: Môi trường gồm 6 trạng thái tuyến tính (0→5), trạng thái 5 là đích.  
- **Thuật toán**: **Q-Learning (off-policy)**  
  - **Q-table**: Ma trận kích thước (số trạng thái)×(số hành động) khởi tạo bằng 0.  
  - **Hàm chuyển trạng thái** `next_state(state, action)`: 0=trái, 1=phải.  
  - **Hàm thưởng** `reward(...)`: chỉ thưởng 1 khi đến đích, 0 còn lại.  
  - **Chính sách ε-greedy**: với xác suất ε chọn ngẫu nhiên (exploration), còn lại chọn hành động tốt nhất theo Q-table (exploitation).  
  - **Cập nhật Q**:
    ```
    Q[s,a] += α * (r + γ * max_a' Q[s',a'] - Q[s,a])
    ```
    với α: learning rate, γ: discount factor.  
  - **Huấn luyện** qua nhiều tập (episodes) cho đến khi Q hội tụ.  
- **Kết quả**: Bảng Q cuối cùng cho thấy giá trị Q cao ở các trạng thái gần mục tiêu, ngụ ý hành động hướng đến đích có kỳ vọng phần thưởng cao.

## 3. So sánh kết quả

| Thuật toán    | Đầu ra                     | Ưu điểm                                   | Nhược điểm                                    | Ứng dụng chính                                 |
|---------------|----------------------------|-------------------------------------------|-----------------------------------------------|-------------------------------------------------|
| **DFS**       | Đường đi (list ô)          | - Cài đặt đơn giản<br>- Ít bộ nhớ         | - Không đảm bảo đường ngắn nhất<br>- Có thể lặp sâu | Tìm lời giải bất kỳ, không cần tối ưu           |
| **BFS**       | Đường đi (list ô)          | - Đảm bảo đường ngắn nhất                 | - Tốn bộ nhớ nếu không gian lớn               | Tìm đường ngắn nhất trên lưới/đồ thị            |
| **FSSP_BFS**  | Đường đi trên lưới/đồ thị   | - Tương tự BFS<br>- Dễ mở rộng bài toán    | - Tương tự BFS                                 | Lập kế hoạch trạng thái tiến, tìm đường tối ưu  |
| **Q-Learning**| Bảng Q (ma trận giá trị)   | - Học chính sách tối ưu từ tương tác<br>- Không cần mô hình | - Cần nhiều vòng lặp để hội tụ<br>- Phụ thuộc tham số | Học tăng cường, robot, game có phần thưởng     |

---

