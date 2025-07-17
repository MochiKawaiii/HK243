# CNN-LAB

## 1. Công nghệ sử dụng
- **Ngôn ngữ**: Python 3.x  
- **Thư viện chính**:  
  - [PyTorch](https://pytorch.org/) (torch, torch.nn, torch.optim)  
  - [Torchvision](https://pytorch.org/vision/) (torchvision, torchvision.transforms)  
  - [NumPy](https://numpy.org/)  
  - [Matplotlib](https://matplotlib.org/)  

## 2. Cách hoạt động của code
1. **Giải thích CNN**  
   - Bắt đầu với phần lý thuyết về Convolutional Neural Network (CNN) và cách hoạt động cơ bản của nó: lớp convolution, pooling, activation, và fully-connected.  
2. **Chuẩn bị dữ liệu**  
   - Sử dụng `torchvision.datasets.MNIST` để load bộ dữ liệu chữ viết tay MNIST.  
   - Áp dụng các phép biến đổi (`transforms.ToTensor()`, `transforms.Normalize()`) để tiền xử lý ảnh.  
3. **Xây dựng mô hình**  
   - Định nghĩa lớp `Net(nn.Module)` gồm hai khối convolution + ReLU + MaxPool, sau đó là hai lớp fully-connected.  
   - Chuyển mô hình lên thiết bị (CPU hoặc GPU nếu có).  
4. **Huấn luyện mô hình**  
   - Khởi tạo hàm mất mát `nn.CrossEntropyLoss()` và optimizer `optim.SGD` (hoặc `Adam`).  
   - Vòng lặp training qua nhiều epoch:  
     - Duyệt batch dữ liệu train, tính forward, backprop, cập nhật trọng số.  
     - In ra loss trung bình sau mỗi epoch để theo dõi.  
5. **Đánh giá & Hiển thị kết quả**  
   - Chuyển mô hình sang chế độ `eval()` và tính accuracy trên tập test.  
   - Hiển thị một số ảnh cùng với dự đoán để trực quan hóa hiệu quả model.  

## 3. Cách chạy mã
1. **Chuẩn bị môi trường**  
   ```bash
   # Tạo và kích hoạt virtual environment (tuỳ chọn)
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

   # Cài đặt các gói cần thiết
   pip install torch torchvision numpy matplotlib jupyter
   ```
2. **Chạy Jupyter Notebook**  
   ```bash
   jupyter notebook CNN-LAB.ipynb
   ```
   - Trong giao diện Jupyter, mở file `CNN-LAB.ipynb` và chọn **Run All** để thực thi toàn bộ các cell.
3. **Chạy dưới dạng script (tuỳ chọn)**  
   - Nếu bạn muốn chạy file dưới dạng script Python, có thể chuyển notebook thành `.py`:
     ```bash
     jupyter nbconvert --to script CNN-LAB.ipynb
     python CNN-LAB.py
     ```
