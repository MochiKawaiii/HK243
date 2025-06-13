
# Thuật toán BFS, DFS và Các Biến Thể – README

## 1. Công nghệ sử dụng
- **Python 3**: Ngôn ngữ lập trình chính.
- **Collections** (`deque`, `defaultdict`): triển khai hàng đợi BFS, ngăn xếp và biểu diễn đồ thị.
- **Heapq**: hàng đợi ưu tiên cho thuật toán Dijkstra.
- **Time** & **Statistics**: đo và thống kê thời gian chạy thuật toán.
- **Typing**: chú thích kiểu dữ liệu (giúp code rõ ràng hơn).
- **Jupyter Notebook**: môi trường thực thi tương tác (Google Colab/VS Code Notebooks đều phù hợp).

## 2. Tổng quan cách hoạt động

### 2.1 BFS – Breadth‑First Search
- Duyệt đồ thị **theo tầng**, dùng hàng đợi FIFO.
- Trả về **đường đi có *số bước* ít nhất** trên đồ thị *không trọng số*.
- Tránh lặp vô hạn nhờ tập `visited`.

```python
from collections import deque
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None
```

### 2.2 DFS – Depth‑First Search
- Duyệt **theo chiều sâu**, dùng đệ quy hoặc ngăn xếp LIFO.
- Trả về **một** đường đi (không đảm bảo ngắn nhất).
- Bộ nhớ tiết kiệm hơn BFS vì chỉ lưu đường hiện tại.

### 2.3 Biến thể & mở rộng
| Biến thể | Mục tiêu | Ý tưởng chính |
|----------|----------|---------------|
| **BFS đếm số đỉnh** | Thống kê số nút đã duyệt | Đếm kích thước `visited` sau khi BFS kết thúc. |
| **BFS/DFS liệt kê *mọi* đường đi** | In tất cả đường từ `start` tới `goal` | Không dừng ngay khi gặp đích, tiếp tục duyệt và lưu toàn bộ đường. |
| **Dijkstra** | Đường đi **nhẹ nhất** trên đồ thị trọng số | Mở rộng nút có chi phí tạm thời nhỏ nhất trước (hàng đợi ưu tiên). |

### 2.4 Đồ thị mẫu
- **Mẫu 1**: đồ thị nhỏ, không chu trình.
- **Mẫu 2**: đồ thị có chu trình.
- **Mẫu 4**: đồ thị lưới, kiểm tra BFS đếm đỉnh.
- **Mẫu 5**: đồ thị trọng số nhỏ, minh họa hạn chế BFS/DFS.
- **Mẫu 6**: trọng số và nhiều đường alternatif, so sánh BFS, DFS, Dijkstra.
- **Mẫu 7**: không trọng số, mật độ cao, BFS liệt kê nhiều đường ngắn nhất.
- **Đồ thị 10 đỉnh**: tự thiết kế, 19 cạnh, dùng cho thử nghiệm tổng quan.

## 3. Cách chạy mã
1. **Mở Notebook** `BFS-DFS.ipynb` trên Jupyter/Colab.
2. Chạy tuần tự từng ô:
   * Thiết lập & lý thuyết.
   * Hàm BFS/DFS/Dijkstra.
   * Đồ thị mẫu + in kết quả.
3. Hoặc copy các hàm vào file `.py` rồi chạy từ CLI:

```bash
python bfs_demo.py
```

## 4. So sánh kết quả
- **BFS**: ít bước nhất, không tối ưu trọng số.  
- **DFS**: đường tuỳ theo thứ tự duyệt, không đảm bảo tối ưu.  
- **Dijkstra**: trọng số nhỏ nhất, có thể dài bước hơn BFS.

| Thuật toán | Số bước (ví dụ) | Tổng trọng số |
|------------|-----------------|---------------|
| BFS        | 3               | 20            |
| DFS        | 5               | 14            |
| Dijkstra   | 4               | **14 (tối ưu)** |

## 5. Hiệu suất
- Đo 10 000 lần trên Đồ thị 6 & 7:  
  *BFS thường nhanh hơn DFS* (đặc biệt đồ thị rậm).  
- Bộ nhớ:  
  *DFS* tiết kiệm hơn (duyệt một nhánh), *BFS* cần lưu nhiều đường tạm.

## 6. Mục đích & ứng dụng
- **Giáo dục**: minh họa tìm kiếm mù trong AI, luyện triển khai Python.
- **Ứng dụng thực tế**  
  - BFS: tìm đường ngắn nhất trong mê cung, mức quan hệ mạng xã hội.  
  - DFS: backtracking (Sudoku, tô màu đồ thị), kiểm tra chu trình.  
  - Dijkstra: GPS, mạng máy tính, tối ưu hoá chi phí đường đi.
