import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt

# 1) Tạo ma trận 6x6 đại diện cho "số 0"
#    Mỗi phần tử 0 hoặc 1. Ta giả lập nó như ảnh "1 kênh" (grayscale).
import numpy as np

matrix_0 = np.array([
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1]
], dtype=np.float32)

# Thêm 1 chiều channel (1 kênh) và 1 chiều batch (1 ảnh)
# Kết quả shape = (1, 1, 6, 6)
matrix_0 = matrix_0[np.newaxis, np.newaxis, :, :]

# 2) Tạo lớp Custom Dataset
class Custom6x6Dataset(Dataset):
    def __init__(self):
        # Ở đây, ta coi "số 0" là nhãn 0
        # Nếu có thêm nhiều ma trận khác, bạn có thể mở rộng danh sách.
        self.data = torch.tensor(matrix_0)
        # Ví dụ coi nhãn = 0 (một lớp duy nhất). 
        # Để minh họa, ta giả sử ta vẫn “phân loại” 2 lớp: 0 hoặc 1
        self.labels = torch.tensor([0])

    def __len__(self):
        return 1  # Có 1 ảnh

    def __getitem__(self, idx):
        # Trả về (ảnh, nhãn)
        return self.data[idx], self.labels[idx]

# 3) Khởi tạo dataset và dataloader
dataset_6x6 = Custom6x6Dataset()
dataloader_6x6 = DataLoader(dataset_6x6, batch_size=1, shuffle=False)

# 4) Định nghĩa mô hình CNN (giống ví dụ MNIST, nhưng có thể đơn giản hơn)
class SmallCNN(nn.Module):
    def __init__(self):
        super(SmallCNN, self).__init__()
        # Vì ảnh đầu vào là 6x6, ta chọn filter 3x3, stride=1, padding=0
        # Để tránh output quá nhỏ, ta chia chỉ 2 tầng chập
        self.conv1 = nn.Conv2d(1, 4, kernel_size=3)  # 1->4 kênh
        self.conv2 = nn.Conv2d(4, 8, kernel_size=3)  # 4->8 kênh
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        # Sau 2 lần conv (không padding), 
        # 6x6 -> 4x4 (conv1) -> 2x2 (conv2) 
        # -> 1x1 với pool => flatten = 8 * 1 * 1 = 8
        self.fc1 = nn.Linear(8, 2)  # Ví dụ phân loại 2 nhãn

    def forward(self, x):
        # Conv1 -> ReLU -> Conv2 -> ReLU -> Pool -> Flatten -> FC
        x = torch.relu(self.conv1(x))  # Kết quả: (4, 4, 4)
        x = torch.relu(self.conv2(x))  # Kết quả: (8, 2, 2)
        x = self.pool(x)               # Kết quả: (8, 1, 1)
        x = x.view(-1, 8)              # Flatten
        x = self.fc1(x)                # Output 2 lớp
        return x

# 5) Khởi tạo mô hình, hàm mất mát, optimizer
model = SmallCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 6) Vòng lặp huấn luyện đơn giản (chạy vài epoch)
num_epochs = 5
for epoch in range(num_epochs):
    for images, labels in dataloader_6x6:
        optimizer.zero_grad()
        outputs = model(images)
        
        # Giả sử nhãn = 0 => CrossEntropy với 2 lớp (0,1)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 7) Kiểm tra kết quả dự đoán
with torch.no_grad():
    for images, labels in dataloader_6x6:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        print(f"Logits: {outputs.squeeze().tolist()}")
        print(f"Dự đoán: {predicted.item()} - Nhãn thật: {labels.item()}")

# 8) Trực quan hóa Feature Map tầng conv1
def visualize_conv1_feature_map(sample):
    """
    Vẽ ảnh gốc (6x6) và output của conv1 (4 kênh)
    """
    model.eval()
    with torch.no_grad():
        conv1_output = torch.relu(model.conv1(sample))
    # conv1_output shape: (1, 4, 4, 4)
    
    fig, axes = plt.subplots(1, 5, figsize=(10, 2))
    # Ảnh gốc
    axes[0].imshow(sample[0, 0].cpu().numpy(), cmap='gray')
    axes[0].set_title("Ảnh gốc")
    axes[0].axis('off')
    
    # 4 kênh feature map
    for i in range(4):
        axes[i+1].imshow(conv1_output[0, i].cpu().numpy(), cmap='gray')
        axes[i+1].set_title(f"Kênh {i+1}")
        axes[i+1].axis('off')

    plt.tight_layout()
    plt.show()

# Gọi hàm trực quan
sample_images, _ = next(iter(dataloader_6x6))
visualize_conv1_feature_map(sample_images)
