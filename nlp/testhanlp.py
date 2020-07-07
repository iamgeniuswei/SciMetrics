# coding:utf-8
from pyhanlp import *

content = '首先介绍了缓冲区溢出漏洞危害的严重性和广泛性,然后,从如何利用缓冲区溢出漏洞的角度,依次介绍了缓冲区溢出漏洞的定义、操作系统内存组织方式以及缓冲区溢出攻击方式.将缓冲区溢出分析技术分为3类:自动检测、自动修复以及运行时防护,并对每一类技术进行了介绍、分析和讨论.最后,对相关工作进行了总结,并讨论了缓冲区溢出分析领域未来可能的3个研究方向:(1)对二进制代码进行分析;(2)结合机器学习算法进行分析;(3)综合利用多种技术进行分析. '
print(HanLP.extractKeyword(content, 5))
seg_hanlp = HanLP.segment(content)
print("/".join([term.word for term in seg_hanlp]))