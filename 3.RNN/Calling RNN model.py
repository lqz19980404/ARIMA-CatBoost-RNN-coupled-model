import torch
import torch.nn as nn
import pandas as pd
import numpy as np

# 加载数据
data_path = r'E:\xuzhou\biao/tcl00_gyh.csv'  # 请替换为实际的数据路径
new_data = pd.read_csv(data_path)

# 提取自变量
X_new = new_data.iloc[:, 1:5].values  # 假设自变量在第2到5列
X_new = X_new.reshape(-1, 1, 4)
#print(X_new)
# 转化为 PyTorch 张量
print('完成数据传入')
X_new = torch.FloatTensor(X_new)

# 定义 RNN 模型
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])  # 取最后一个时间步的输出
        out = torch.relu(out)
        return out

# 初始化模型并加载训练好的参数
input_size = 4  # 自变量的特征数
hidden_size = 512
output_size = 1
num_layers = 5
model = SimpleRNN(input_size, hidden_size, output_size, num_layers)
model.load_state_dict(torch.load(r'E:\PYcharm\pythonProject1\out_mod\be\2.pth'))

# 将模型设置为评估模式
model.eval()

# 使用模型进行预测
with torch.no_grad():
    predictions = model(X_new)

# 将预测结果保存到 D 盘
predictions = predictions.numpy().flatten()
new_data['PreCD'] = predictions
new_data.to_csv(r'E:\xuzhou\biao/T2000_be.csv', index=False)
print("Predictions saved to predictions.csv.")