#_*_coding:utf-8_*_
import arcpy
import os

# 设置工作环境
arcpy.env.workspace = r"D:\Impact factor data\X\gyh"

# 列出文件夹中的所有 TIFF 文件
tif_list = arcpy.ListRasters("*", "TIF")

# 获取 TIFF 文件的数量
total_tif_count = len(tif_list)
processed_count = 0

# 循环处理每个 TIFF 文件
for tif_file in tif_list:
    # 更新处理计数器
    processed_count += 1
    print "Processing %s (%d/%d)" % (tif_file, processed_count, total_tif_count)

    # 获取当前文件的最大值和最小值
    raster = arcpy.Raster(tif_file)
    tif_max = raster.maximum
    tif_min = raster.minimum
    print "  Max value: %s, Min value: %s" % (tif_max, tif_min)

    # 构建输出路径
    output_path = r"D:\Impact factor data\X\gyh/gyh"
    output_name = os.path.splitext(tif_file)[0] + "_normalized.tif"
    output_full_path = os.path.join(output_path, output_name)

    # 使用栅格计算器进行归一化
    expression = "Float(\"%s\" - %s) / (%s - %s)" % (tif_file, tif_min, tif_max, tif_min)
    arcpy.gp.RasterCalculator_sa(expression, output_full_path)

print "Processing completed."
