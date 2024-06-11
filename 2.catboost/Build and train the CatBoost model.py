import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report

# 读取Excel文件
df = pd.read_excel(r'D:\Carbon density\X_SOIL\BIAO\2010\TEXT\TEXT3.xlsx')

# 假设要使用的特征是第2列到第5列
X = df.iloc[:, 1:5]  # 修改索引以匹配您的数据
y = df['CLASS']     # 假设目标变量在名为'target'的列中

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建CatBoost分类器实例
model = CatBoostClassifier(
    iterations=1500,
    depth=8,
    learning_rate=0.1,
    loss_function='MultiClass',
    task_type='GPU',
    verbose=True
)

# 训练模型
model.fit(X_train, y_train)

# 进行预测
y_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# 显示不同类型的预测精度
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)

# 保存模型
model.save_model('FL_MOD/soil/1.cbm', format='cbm')