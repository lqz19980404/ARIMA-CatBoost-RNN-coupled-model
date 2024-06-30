import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# 忽略潜在的警告信息
warnings.filterwarnings("ignore")

# 时间序列数据
data = []
time_series = pd.Series(data)

# 构建并拟合ARIMA模型
model = ARIMA(time_series, order=(5, 1, 2))
model_fit = model.fit()

# 使用模型进行预测
forecast = model_fit.forecast(steps=6)
last_five = time_series[-6:]
loss = mean_squared_error(last_five, forecast)

# 输出预测结果
# 使用iloc[0]或者tolist()[0]来获取第一个预测值
print("预测的5期值为:", forecast)
print("损失（LOSS）值:", loss)
# 或者
# print("预测的下一期值为:", forecast.tolist()[0])



# import pandas as pd
# from statsmodels.tsa.arima.model import ARIMA
# import warnings
#
# # 忽略潜在的警告信息
# warnings.filterwarnings("ignore")
#
# # 时间序列数据
# data = [4.82, 4.39, 6.68, 7.59, 7.45, 6.87, 5.88, 5.87, 6.91, 6.31, 7.49, 7.43, 7.83, 8.38, 8.18]
# time_series = pd.Series(data)
#
# # 构建并拟合ARIMA模型
# model = ARIMA(time_series, order=(5, 2, 5))
# model_fit = model.fit()
#
# # 使用模型进行预测，预测未来5年
# forecast = model_fit.forecast(steps=5)
#
# # 输出预测结果
# print("未来5年的预测值为:", forecast)
