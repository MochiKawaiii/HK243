# Áp Dụng Tích Chập Cho Ma Trận 6×6 (Số "0")

## 1. Công nghệ sử dụng

- **Python**: Ngôn ngữ lập trình chính.
- **PyTorch**: Thư viện học sâu để xây dựng và huấn luyện mô hình CNN.
- **NumPy**: Xử lý và thao tác ma trận đầu vào.
- **Matplotlib**: Trực quan hóa feature maps sau khi áp dụng lớp tích chập.

## 2. Cách hoạt động của code

1. **Khởi tạo ma trận 6×6**
   - Ma trận `matrix_0` đại diện cho chữ số "0" dưới dạng ảnh grayscale 1 kênh.
   - Chuyển ma trận thành tensor với shape `(batch_size=1, channels=1, height=6, width=6)`.

2. **Tạo Custom Dataset**
   - Lớp `Custom6x6Dataset` kế thừa từ `torch.utils.data.Dataset`.
   - Chứa dữ liệu ma trận và nhãn (số 0).
   - Trả về ảnh và nhãn để đưa vào DataLoader.

3. **Model CNN đơn giản (SmallCNN)**
   - Hai tầng tích chập (Conv2d):
     - `conv1`: input 1 kênh → output 4 kênh, kernel 3×3.
     - `conv2`: input 4 kênh → output 8 kênh, kernel 3×3.
   - Hàm kích hoạt ReLU giữa các tầng.
   - Lớp MaxPool2d giảm kích thước feature map.
   - Fully-connected (`fc1`) kết nối đầu ra feature map với 2 nhãn.

4. **Huấn luyện mô hình**
   - Sử dụng `CrossEntropyLoss` cho bài toán phân loại 2 lớp.
   - Optimizer: `SGD` với learning rate = 0.01.
   - Vòng lặp huấn luyện trong `num_epochs` epoch để cập nhật trọng số mô hình.

5. **Đánh giá kết quả**
   - Dự đoán nhãn cho ảnh đầu vào.
   - In ra logits và nhãn dự đoán so với nhãn thật.

6. **Trực quan hóa Feature Map**
   - Hàm `visualize_conv1_feature_map`:
     - Lấy output của `conv1` sau ReLU.
     - Hiển thị ảnh gốc và 4 kênh feature map bằng Matplotlib.

## 3. Cách chạy mã

1. **Cài đặt môi trường**

   ```bash
   pip install torch torchvision matplotlib numpy
   ```

2. **Chạy file Python**

   ```bash
   python CNN_so0.py
   ```

3. **Kiểm tra kết quả**
   - Quan sát kết quả in ra trên terminal: loss qua các epoch, logits và nhãn dự đoán.
   - Cửa sổ Matplotlib sẽ hiện ảnh gốc và các feature map của `conv1`.

4. **Tùy chỉnh**
   - Có thể thay đổi số epoch, learning rate hoặc kiến trúc mạng để quan sát sự khác biệt.
