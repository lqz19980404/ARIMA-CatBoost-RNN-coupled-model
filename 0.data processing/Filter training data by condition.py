import pandas as pd

def extract_and_save(csv_file_path, target_value, output_file_path_all, output_file_path_extracted):
    # 读取CSV文件到DataFrame
    data = pd.read_csv(csv_file_path)

    # 转为大列表
    all_data_list = data.values.tolist()
    extracted_data_list = []

    for a in range(5100): #100可改，这是一共要提取的数据量与下面0.00005相关也与0-0.1的分级范围相关
        a = a+1
        target_value = target_value +3.333333333333333e-5
        # 提取第6列数据
        column_six_list = [row[5] for row in all_data_list]

        # 寻找与目标值差距最小的行的索引
        min_diff_index = min(range(len(column_six_list)), key=lambda i: abs(column_six_list[i] - target_value))

        # 提取与目标值差距最小的行
        extracted_row = all_data_list[min_diff_index]

        print('提取数量：', a, '目标值', target_value, '提取密度值', extracted_row[5], '差距值：', extracted_row[5]-target_value)
        # 删除大列表中该行
        all_data_list.pop(min_diff_index)
        extracted_data_list.append(extracted_row)


    # 将大列表和提取出的行列表转为DataFrame
    all_data_df = pd.DataFrame(all_data_list, columns=data.columns)
    extracted_data_df = pd.DataFrame(extracted_data_list, columns=data.columns)

    # 保存两个DataFrame为CSV文件
    all_data_df.to_csv(output_file_path_all, index=False)
    extracted_data_df.to_csv(output_file_path_extracted, index=False)

# 定义CSV文件路径和输出文件路径
csv_file_path = r'D:\Carbon density\vegetation\below\rnn\2010/TQ2.csv' # 替换为实际文件路径
output_file_path_all = r'D:\Carbon density\vegetation\below\rnn\2010/F2.csv'  # 保存所有数据的文件路径
output_file_path_extracted = r'D:\Carbon density\vegetation\below\rnn\2010\TQ_2.csv'  # 保存提取出的数据的文件路径

# 指定目标数值
target_value = 0.32 #初始提取值

# 运行程序
extract_and_save(csv_file_path, target_value, output_file_path_all, output_file_path_extracted)
