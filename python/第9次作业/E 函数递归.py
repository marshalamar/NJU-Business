'''
按如下递归公式求函数值。
x=1时 f(x)=10；x>1时 f(x)=f(x-1)+2
输入
整形变量x
输出
f(x)
样例输入
10
样例输出
28
'''

def f(x):
    if x==1:
        return 10
    if  x>1:
        return f(x-1)+2

print(f(int(input())))