import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import warnings

# 忽略潜在的警告信息
warnings.filterwarnings("ignore")

# 时间序列数据
data = []
time_series = pd.Series(data)

# 设定ARIMA模型参数的探索范围
p_range = range(1, 11)  # AR项的可能取值
q_range = range(1, 11)  # MA项的可能取值

# 创建空的 DataFrame 来存储每个 (p, q) 组合对应的 AIC 和 BIC 值
aic_matrix = pd.DataFrame(index=p_range, columns=q_range)
bic_matrix = pd.DataFrame(index=p_range, columns=q_range)

# 遍历 p 和 q 的所有组合
for p in p_range:
    for q in q_range:
        try:
            # 尝试使用当前的 p 和 q 参数创建并拟合ARIMA模型
            model = ARIMA(time_series, order=(p, 2, q))
            model_fit = model.fit()

            # 将拟合后模型的 AIC 和 BIC 值存储到对应的 DataFrame 中
            aic_matrix.loc[p, q] = model_fit.aic
            bic_matrix.loc[p, q] = model_fit.bic
        except Exception as e:
            # 如果当前 (p, q) 组合导致模型无法拟合，则存储 NaN
            aic_matrix.loc[p, q] = np.nan
            bic_matrix.loc[p, q] = np.nan

# 输出 AIC 和 BIC 表格
print("AIC 表格:")
print(aic_matrix)
print("\nBIC 表格:")
print(bic_matrix)

aic_matrix.to_csv(r'd:\Desktop\小论1文件文\小论文表图/aic_matrix.csv')
bic_matrix.to_csv(r'd:\Desktop\小论1文件文\小论文表图/bic_matrix.csv')

print("AIC 表格已保存为 r'd:\Desktop\小论1文件文\小论文表图/aic_matrix.csv'")
print("BIC 表格已保存为 r'd:\Desktop\小论1文件文\小论文表图/bic_matrix.csv'")
