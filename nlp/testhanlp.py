# coding:utf-8
from pyhanlp import *
import jieba
#content = '首先介绍了缓冲区溢出漏洞危害的严重性和广泛性,然后,从如何利用缓冲区溢出漏洞的角度,依次介绍了缓冲区溢出漏洞的定义、操作系统内存组织方式以及缓冲区溢出攻击方式.将缓冲区溢出分析技术分为3类:自动检测、自动修复以及运行时防护,并对每一类技术进行了介绍、分析和讨论.最后,对相关工作进行了总结,并讨论了缓冲区溢出分析领域未来可能的3个研究方向:(1)对二进制代码进行分析;(2)结合机器学习算法进行分析;(3)综合利用多种技术进行分析. '
#content = '随着技术的发展,信息物理融合系统(cyber-physical system,简称CPS)在生活中扮演着越来越重要的角色,例如电力系统、铁路系统.如果CPS遭到攻击,将对现实世界的正常运转造成巨大影响,甚至威胁生命安全.垂悬指针是指向的区域被释放后未被置为空的指针,它是一种会导致攻击的软件缺陷.由垂悬指针导致的use-after-free和double-free漏洞能够执行任意恶意代码.迄今为止,只有少量工作针对垂悬指针进行检测、防御.其中多数都会导致过高的额外运行时开销.提出Dang Done用于检测和防御垂悬指针.首先,通过静态分析检测潜在垂悬指针;然后,基于检测到的垂悬指针信息和一系列预定义的指针变换规则,依据指针传播信息变换指针,使得指针及其别名都指向同一个新引入的指针.基于该方法,实现了Dang Done的原型工具.基于11个开源项目和SPEC CPU benchmark的实验结果表明:DangDone的静态分析部分只有33%的误报率,指针变换部分只引入了1%左右的额外开销.同时,Dang Done成功防护了11个开源项目中的use-after-free和double-free漏洞.实验结果体现了Dang Done的高效率及有效性.'
content = '针对当前工业信息物理系统的安全风险评估模型极少考虑系统的动态进程对评估准确性的影响，本文给出一种工业信息物理系统安全风险动态表现分析量化评估模型。首先运用贝叶斯网络对攻击在网络层的入侵过程建模，计算网络攻击成功入侵的概率；其次，在攻击成功入侵的前提下，采用卡尔曼状态观测器实时观测被控对象的状态，研究系统的动态表现，定量分析系统的表现损失，从经济损失的角度量化攻击对系统造成的影响，并结合攻击成功入侵的概率，实现对系统安全风险的动态评估。最后通过Matlab对攻击下沸水发电厂模型的运行状态进行仿真。结果表明，该模型能有效地评估工业信息物理系统的风险。'
seg_hanlp = HanLP.segment(content)
print("/".join([term.word for term in seg_hanlp]))
print(HanLP.extractKeyword(content, 20))


from  jieba import analyse
seg_list = jieba.cut(content, cut_all=False)
print("/".join(seg_list))
tfidf = analyse.extract_tags
keywords =  jieba.analyse.textrank(content, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
print(keywords)