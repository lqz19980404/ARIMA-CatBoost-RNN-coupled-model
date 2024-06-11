import pandas as pd
from catboost import CatBoostClassifier

# 加载保存的模型
model = CatBoostClassifier()
model.load_model('FL_MOD/catboost_model18.cbm')

# 假设您有一个新的数据集，您想用这个模型来做预测
# 首先，读取数据（确保这个数据集的格式与训练模型时使用的数据集格式一致）
new_data = pd.read_excel(r'D:\Carbon density\vegetation\ad\biao\ab_15_2.xlsx')

# 使用模型进行预测
# 假设我们使用的特征是第2列到第5列
X_new = new_data.iloc[:, 1:5]  # 修改索引以匹配您的数据
predictions = model.predict(X_new)

# 将预测结果保存在新的列中
new_data['Predictions'] = predictions

# 将包含预测结果的数据集保存到新的 Excel 文件中
output_file_path = r'D:\Carbon density\vegetation\ad\yc/flab_15_2.xlsx'
new_data.to_excel(output_file_path, index=False)

# 输出包含预测结果的数据集路径
print(f"Predictions saved to: {output_file_path}")
