'''
题目描述
输入两个整数，判断它们是否互质。
输入
输入两个整数a，b，每行一个。
输出
输出它们是否互质，如果互质的话，则输出：a and b are coprime，否则输出: a and b are not coprime。
样例输入
2
3
样例输出
2 and 3 are coprime
'''
a=int(input())
b=int(input())
c=min(a,b)
d=max(a,b)
factors=[c]
for i in range(2,int(c/2)+1):
    if c%i==0:
        factors.append(i)
flag=True
for factor in factors:
    if d%factor==0:
        flag=False
        break
if flag:
    print("{} and {} are coprime".format(a,b),end='')
else:
    print("{} and {} are not coprime".format(a,b),end='')