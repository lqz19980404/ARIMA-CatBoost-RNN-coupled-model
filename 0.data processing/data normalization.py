import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 读取CSV文件
file_path = r'E:\xuzhou\biao\tcl00.csv'
df = pd.read_csv(file_path)

# 剔除除第一列以外，所有列中大于10000或小于0的数据
df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda x: x.clip(0.00001, 10000))

# 保存原始数据列名
original_columns = df.columns.tolist()

# 提取除第一列以外的所有数据
data_to_normalize = df.iloc[:, 1:]

# 显示每列的最大值和最小值
column_stats = data_to_normalize.describe().loc[['min', 'max']]
print("每列的最小值和最大值:")
print(column_stats)

# 使用MinMaxScaler进行归一化
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data_to_normalize)

# 将归一化后的数据添加到DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=data_to_normalize.columns)

# 将原始数据的第一列和归一化后的数据合并
final_df = pd.concat([df.iloc[:, 0], normalized_df], axis=1)

# 保存归一化后的数据到D盘
output_file_path = r'E:\xuzhou\biao\tcl00_gyh.csv'
final_df.to_csv(output_file_path, index=False)

# 输出归一化公式
normalization_formula = f"归一化公式: {original_columns[1:]} -> (x - min) / (max - min)"
print(normalization_formula)
