'''
@Author: your name
@Date: 2020-07-08 11:29:57
@LastEditTime: 2020-07-08 15:42:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \SciMetrics\testlac.py
'''
# coding:gbk
from LAC import LAC
lac = LAC(mode='lac')
lac.load_customization('custom.txt', sep=None)
text = '准确评估路网脆弱性是道路规划的基础.为兼顾路段和交叉口拥堵的影响,引入瓶颈线路的概念,旨在识别因道路容量较小而难以抵御突发事件的通行线路.在此基础上,提出了基于谱分析的路网脆弱性分析方法,利用图谱分区中的最小分割理论定位瓶颈线路.为解决瓶颈线路拥堵所致的大面积切断式分割问题,采取了基于连通贡献量的路网完善措施,在新建和扩建等方面对路网保护措施提出改进建议.仿真结果表明,与其他方案相比,所提出的脆弱性识别机制对路网中的瓶颈线路定位更准确,且可避免产生路网切断式分割现象.'
lac_result = lac.run(text)
print(lac_result)