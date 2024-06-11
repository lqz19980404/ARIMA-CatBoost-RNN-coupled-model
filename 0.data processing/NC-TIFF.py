#_*_coding:utf-8_*_
#nc转tif
import os
import arcpy

PE_path=r'D:\Impact factor data\SM\SMCI_1km_2020_100cm/'     #nc文件夹路径
tiff_path = r'D:\Impact factor data\SM\SMCI_1km_2020_100cm\tiff/'         #tif文件夹保存路径

item = "smci"
i=1

for root, dirs, files in os.walk(PE_path):
    for file in files:
       if file.endswith(".nc"):
            PE_file = PE_path + file

            time_dimension = "time"  # 例如："time"
            #time_values = range(1, 366)

            # PE = Dataset(PE_file)
            for k in range(365):
                print(i)
                band = str(k)              #注意起始索引值
                #RasterLayer = arcpy.MakeNetCDFRasterLayer_md(PE_file, "SMCI", "lon", "lat", item + "_Layer", dimension_values='time')

                RasterLayer = arcpy.MakeNetCDFRasterLayer_md(PE_file, "SMCI", "lon", "lat", item + "_Layer",
                                                             dimension_values=[[time_dimension, band]],
                                                             value_selection_method="BY_INDEX")
                band = str(k + 1)
                raster_dataset = arcpy.Raster(item + "_Layer")
                band = band.zfill(3)
                raster_dataset.save(tiff_path + file[0:-3] + "_" + band + ".tif")
                arcpy.Delete_management(item + "_Layer")
                i=i+1