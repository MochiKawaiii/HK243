# README for Naive Bayes Tutorials

This README consolidates two tutorials demonstrating Naive Bayes models applied to different data types:

- **Part I**: Drug Classification using Gaussian Naive Bayes (using `drug.csv` dataset)
- **Part II**: Text Classification using Bernoulli Naive Bayes (using `Education.csv` dataset)

---

## Part I: exercise2.ipynb

### 1. Chuẩn bị thư viện

```python
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import seaborn as sns
from scipy.stats import skew
```

### 2. Đọc dữ liệu

```python
data = pd.read_csv('drug.csv')
print(data.head())
print(data[['Sex','BP','Cholesterol','Drug']].nunique())
```

### 3. Khám phá phân phối và tiền xử lý

```python
X = data.drop('Drug', axis=1)
y = data['Drug']
X = pd.get_dummies(X, columns=['Sex','BP','Cholesterol'], dtype=int)
label_map = {'drugA':1,'drugB':2,'drugC':3,'drugX':4,'DrugY':5}
y = y.map(label_map)
sns.histplot(X['Na_to_K'], kde=True)
print('Skewness:', skew(X['Na_to_K']))
```

### 4. Chia tập train/test

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)
```

### 5. Huấn luyện mô hình

```python
gaussian = GaussianNB()
gaussian.fit(X_train, y_train)
```

### 6. Dự đoán và xác suất

```python
y_pred = gaussian.predict(X_test)
y_pred_proba = gaussian.predict_proba(X_test)
```

### 7. Đánh giá hiệu năng

```python
print(classification_report(y_test, y_pred, target_names=list(label_map.keys())))
```

---

## Part II: exercise1.ipynb

### 1. Chuẩn bị thư viện

```python
import numpy as np
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
```

### 2. Tải dữ liệu

```python
data = pd.read_csv('Education.csv')
print(data[['Text','Label']].head())
```

### 3. Chia tập train và test

```python
def split_train_test(data, ratio_test):
    np.random.seed(0)
    idx = np.random.permutation(len(data))
    data_shuffled = data.iloc[idx]
    test_size = int(len(data)*ratio_test)
    train = data_shuffled.iloc[:-test_size].reset_index(drop=True)
    test  = data_shuffled.iloc[-test_size:].reset_index(drop=True)
    return train, test

train_set, test_set = split_train_test(data, 0.2)
```

### 4. Khám phá và mã hóa nhãn

```python
print(train_set['Label'].value_counts())
y_train = train_set['Label'].map({'positive':1, 'negative':0})
```

### 5. Trích xuất đặc trưng văn bản

```python
vectorizer = CountVectorizer(binary=True, stop_words='english')
X_train_feats = vectorizer.fit_transform(train_set['Text'])
```

### 6. Huấn luyện mô hình

```python
model = BernoulliNB()
model.fit(X_train_feats, y_train)
```

### 7. Dự đoán và đánh giá

```python
X_test_feats = vectorizer.transform(test_set['Text'])
y_pred = model.predict(X_test_feats)
print(confusion_matrix(test_set['Label'], np.where(y_pred==1,'positive','negative')))
print(classification_report(test_set['Label'], np.where(y_pred==1,'positive','negative')))
```
