'''
题目描述

BMI是世界公认的⼀一种评定肥胖程度的分级方法，世界卫生组织(WHO)也以BMI来对肥胖或超重进⾏定义。它的定义如下:
体质指数(BMI)=体重(kg)÷身⾼(m)^2
当BMI大于等于18.5小于等于23.9时属正常。请输⼊入你或同伴的体重和身高计算BMI值，并输出胖瘦判断的结果。大于23.9输出fat，小于等于23.9大于等于18.5输出normal，小于18.5输出slim


输入
70 1.75
输出
normal

样例输入
70 1.75
样例输出
normal
'''
weight,height=eval(input().replace(' ',','))
BMI=weight/height/height
if 18.5<=BMI<=23.9:
    print('normal')
elif BMI>23.9:
    print('fat')
elif 18.5>=BMI:
    print('slim')