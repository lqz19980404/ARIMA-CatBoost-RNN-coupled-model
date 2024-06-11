import pandas as pd

# 读取Excel文件中的两个工作表数据
df_sample1 = pd.read_excel(r'D:\Carbon density\X_SOIL\BIAO\2010\TEXT\verify_1.xlsx', sheet_name='3')
df_sample2 = pd.read_excel(r'D:\Carbon density\X_SOIL\BIAO\2010\TEXT\TEXT1.XLSX', sheet_name='2')

# 打印第一个样本的数量
num_samples1 = len(df_sample1)
print("第一个样本中的样本数量：", num_samples1)

threshold = 0.05

# 定义相似行序号
similar_row_numbers = {}

# 遍历第一种样本中的每一行
for idx1, row1 in df_sample1.iterrows():
    # 打印当前进行到哪个样本的查找
    print("正在查找与第", idx1 + 1, "个样本相似的行...")

    # 将第二种样本中与当前行差值小于阈值的行加入结果列表
    similar_rows = df_sample2[
        (abs(df_sample2.iloc[:, 4] - row1.iloc[4]) < threshold) &
        (abs(df_sample2.iloc[:, 1] - row1.iloc[1]) < threshold) &
        (abs(df_sample2.iloc[:, 2] - row1.iloc[2]) < threshold) &
        (abs(df_sample2.iloc[:, 3] - row1.iloc[3]) < threshold)
        ].index.tolist()

    # 为相似行添加序号
    for similar_row in similar_rows:
        similar_row_numbers[similar_row] = idx1 + 1

# 提取第二种样本中与第一种样本相近的行
result = df_sample2.loc[similar_row_numbers.keys()]

# 添加第一个样本列表该行的第一列的数字到相似行后
result['序列号'] = [similar_row_numbers[index] for index in result.index]

# 保存相似行到D盘
result.to_excel(r'D:\Carbon density\X_SOIL\BIAO\2010\TEXT/duoyu_2.xlsx', index=False)

# 在第二个样本中删除相似行
df_sample2_cleaned = df_sample2.drop(result.index)

# 保存删除相似行后的第二个样本到E盘
df_sample2_cleaned.to_excel(r'D:\Carbon density\X_SOIL\BIAO\2010\TEXT/shaix_2.xlsx', index=False)

# 输出结果
print("提取出的相似行已保存到D盘")
print("删除相似行后的第二个样本已保存到E盘")
