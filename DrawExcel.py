#! /usr/bin/env python3

import xlrd
import numpy as np
from pyecharts.charts import Bar

#柱形图方法
def ColumnChart():
    #获取总行数
    nrows = table.nrows

    #获取总列数
    ncols = table.ncols
    #数据是行还是列
    print('''
          绘图数据是行还是列
          1、行
          2、列
          ''')
    dataFromExcel = int(input())
    if dataFromExcel == 1:
        #获取x轴数据
        print('一共 '+ str(nrows) +' ,X轴数据是第几行')
        x = int(input())
        #获取y轴数据
        print('一共 '+ str(nrows) +' ,Y轴数据是第几行')
        y = int(input())
    else:
        #获取x轴数据
        print('一共 '+ str(ncols) +' ,X轴数据是第几行')
        x = int(input())
        dataX = table.col_values(x-1)
        #获取y轴数据
        print('一共 '+ str(ncols) +' ,Y轴数据是第几行')
        y = int(input())
        dataY = table.col_values(y-1)


 
    bar.add_xaxis(dataX[1:])
    bar.add_yaxis('cmp',dataY[1:])
    
    return bar

#条形图方法
def BargraphChart():
    return True


#折线图方法
def LineChart():
    return True

#获取一列的数值，例如第2列
    return True

#南丁格尔图方法
def NightingaleRoseChart():
    return True

#雷达图
def RadarChart():
    return True

#饼图
def PieChart():
    return True

#散点图
def ScatterplotChart():
    return True

#读取excel数据
#输入需要读取Excel表格的路径
print('请输入文件路径，如：\'/Users/mac/Documents/test.xls\'')
path = input()
data = xlrd.open_workbook(path)
table = data.sheet_by_index(0)
bar = Bar()

#选择方法
while True:
    #选择所要绘制的图形
    print('''
    请选择要绘制的图形：
    1、柱形图
    2、条形图
    3、折线图
    4、南丁格尔-玫瑰图
    5、雷达图
    6、饼图
    7、散点图
    ''')
    tableNumber = int(input())
    if tableNumber == 1:
        ColumnChart()
        break
    if tableNumber == 2:
        BargraphChart()
        break
    if tableNumber == 3:
        LineChart()
        break
    if tableNumber == 4:
        NightingaleRoseChart()
        break
    if tableNumber == 5:
        RadarChart()
        break
    if tableNumber == 6:
        PieChart()
        break
    if tableNumber == 7:
        ScatterplotChart()
        break
    else:
        continue
    
#绘图输出路径
print('请输入文件输出路径与文件名，如：\'/Users/mac/Documents/testExcel.html\'')
OutputPath=input()
bar.render(OutputPath)
    
