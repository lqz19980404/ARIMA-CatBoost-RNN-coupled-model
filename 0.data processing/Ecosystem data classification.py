import os
import pandas as pd
from tqdm import tqdm

# 定义输入文件夹路径
input_folder = r"D:\stxt\XIFEN\BIAO/f2"

# 获取文件夹中所有的XLSX文件路径
xlsx_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.xlsx')]

# 打印需要处理的表格数量
print(f"需要处理 {len(xlsx_files)} 个表格")

# 存储所有结果的列表
all_results = []

# 遍历每个XLSX文件并进行处理
for idx, input_excel in enumerate(xlsx_files, start=1):
    print(f"正在处理第 {idx} 个表格: {input_excel}")

    # 读取Excel文件
    df = pd.read_excel(input_excel)

    # 删除小于 0 的行
    df = df[(df.iloc[:, 1:6] >= 0).all(axis=1)]

    # 根据第7列的唯一值对第2到第6列进行分类，计算每个类别的总和
    unique_values = df.iloc[:, 6].unique()
    result_data = []

    for value in unique_values:
        sub_df = df[df.iloc[:, 6] == value]
        sum_values = sub_df.iloc[:, 1:6].sum().tolist()
        result_data.append([value] + sum_values)

    # 构建结果 DataFrame
    result_df = pd.DataFrame(result_data, columns=['Category'] + ['Sum_column_' + str(i) for i in range(2, 7)])

    # 获取文件名作为表名
    table_name = os.path.splitext(os.path.basename(input_excel))[0]

    # 添加表名作为一行数据
    result_df.loc[-1] = [table_name] + [''] * 5
    result_df.index = result_df.index + 1
    result_df = result_df.sort_index()

    # 将结果添加到列表中
    all_results.append(result_df)

# 合并所有结果表
merged_result = pd.concat(all_results, ignore_index=True)

# 构建保存结果的文件路径
output_excel = os.path.join(input_folder, "Merged_Result.xlsx")

# 保存合并后的结果到新的Excel文件
merged_result.to_excel(output_excel, index=False)

print("合并后的结果已保存到:", output_excel)
