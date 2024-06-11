# ARIMA-CatBoost-RNN-coupled-model
Estimation of regional terrestrial ecosystem carbon density and carbon storage based on multi-model coupling

0.data processing
  This part is the data processing code before building the training and validation data sets, which mainly includes data preprocessing, classification, conditional screening, normalization and other steps.
  这部分为构建训练与验证数据集前的数据处理代码，主要包括数据预处理、分类、按条件筛选、归一化等步骤。

1.ARIMA
  This includes the parameter determination, construction and training of the ARIMA model, calling the trained model, etc.
  这里包括ARIMA模型的参数确定、构建与训练、调用训练好的模型等。
  
2.CatBoost
  This includes the construction, training, and calling code of the CatBoost model.
  这里包括CatBoost模型的构建与训练、调用方式代码。
  
3.RNN
  This includes the construction, training, and calling code of the RNN model.
  这里包括RNN模型的构建与训练、调用方式代码。

Note that you must configure the environment and download the corresponding code library when calling.
注意在调用时配置好环境，下载相应的代码库。
