import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 加载数据
data_path = r'D:\Carbon density\vegetation\below\rnn\2010/test2.csv'  # 请替换为实际的数据路径
data = pd.read_csv(data_path)

#print(data.dtypes)

# 提取自变量和因变量
X = data.iloc[:, 1:5].values  # 假设自变量在第2到5列
# print(X)
y = data.iloc[:, -1].values  # 假设因变量在最后一列
X = X.reshape(-1, 1, 4)
# 归一化数据（可选）
# 这里使用了简单的归一化，具体归一化方式可以根据实际情况调整
# X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
# y = (y - np.mean(y)) / np.std(y)

# 转化为 PyTorch 张量
X = torch.FloatTensor(X)
print(X.shape)
y = torch.FloatTensor(y).view(-1, 1)


# 定义 RNN 模型
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size,num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])  # 取最后一个时间步的输出
        out = torch.relu(out)
        return out


# 定义训练函数
def train_rnn(model, X_train, y_train, num_epochs=100, batch_size=500, learning_rate=0.001):
    criterion = nn.L1Loss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    losses = []

    for epoch in range(num_epochs):
        for i in range(0, len(X_train), batch_size):
            inputs = X_train[i:i + batch_size]
            targets = y_train[i:i + batch_size]

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            #if (epoch + 1) % 20 == 0 :
             #   x=outputs.detach()
              #  y=targets.detach()
               # plt.scatter(x.numpy(),y.numpy())
                #plt.show()

            loss.backward()
            optimizer.step()

        losses.append(loss.item())
        #if (epoch + 1) % 5 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    return losses


# 定义函数用于制作 LOSS 值、预测值和真实值的差与 epoch 的函数图像
def plot_loss_and_predictions(losses, predictions, targets):
    plt.plot(losses, label='Loss')
    plt.legend()
    plt.xlabel('Epoch')
    plt.ylabel('Value')
    plt.show()


    plt.scatter(range(len(targets)),targets,c='g',label='targets')
    plt.scatter(range(len(predictions)),predictions,c='r',label='predictions')
    plt.xlabel('Epoch')
    plt.ylabel('predictions and targets')
    plt.show()


# 划分训练集和验证集
train_size = int(0.8 * len(X))
X_train, X_val = X[:train_size], X[train_size:]
y_train, y_val = y[:train_size], y[train_size:]


# 调用训练函数
input_size = X.shape[2]  # 自变量的特征数提取的是（n,1,4）中的4
hidden_size = 512
output_size = 1
num_layers = 5
model = SimpleRNN(input_size, hidden_size, output_size,num_layers)
losses = train_rnn(model, X_train, y_train)


# 模型评估
model.eval()
with torch.no_grad():
    val_predictions = model(X_val)
    mse = nn.L1Loss()(val_predictions, y_val)
    print(f'Validation MSE: {mse.item():.4f}')

# # 显示模型参数
# def print_model_parameters(model):
#     for name, param in model.named_parameters():
#         if param.requires_grad:
#             print(name, param.data)
#
# print_model_parameters(model)

# 制作 LOSS 值、预测值和真实值的差与 epoch 的函数图像
val_predictions = val_predictions.numpy()
y_val = y_val.numpy()
plot_loss_and_predictions(losses, val_predictions, y_val)


# 保存训练好的模型
torch.save(model.state_dict(), 'out_mod/be/2.pth')
