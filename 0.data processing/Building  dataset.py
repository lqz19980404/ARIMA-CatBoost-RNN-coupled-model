import os
import pandas as pd

# 源文件夹路径
source_folder = r'E:\PYcharm\pythonProject1\soil_data\2010'

# 提取前1/10行的数据
def extract_and_save_data(file_path):
    print(f"正在处理文件: {file_path}")

    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)
        print("文件读取成功。")

        # 提取前1/10行数据
        extracted_data = df.head(int(len(df) / 10))
        print(f"提取了{len(extracted_data)}行数据。")

        # 保存提取的数据为新的CSV文件
        extracted_file_path = os.path.join(r'E:\PYcharm\pythonProject1\soil_data/test', os.path.basename(file_path))
        extracted_data.to_csv(extracted_file_path, index=False)
        print(f"提取的数据已保存到: {extracted_file_path}")

        # 删除原CSV文件中被提取出的数据
        remaining_data = df.tail(len(df) - len(extracted_data))
        remaining_data.to_csv(file_path, index=False)
        print("原文件中被提取的数据已删除。")

    except Exception as e:
        print(f"处理文件时出现错误: {e}")

# 遍历文件夹中的CSV文件并提取数据
for filename in os.listdir(source_folder):
    if filename.endswith('soil2010_extra_bc.csv'):
        file_path = os.path.join(source_folder, filename)
        extract_and_save_data(file_path)

print("所有数据提取和保存操作已完成。")
