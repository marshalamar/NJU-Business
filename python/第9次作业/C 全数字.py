'''
题目描述
如果一个n（n<=9）位数刚好包含了1至n中所有数字各一次则称它们是全数字（pandigital）的，例如四位数1324就是1至4全数字的。从键盘上输入一组（不止一个）整数，输出其中的全数字，若找不到则输出“not found”。形如：

def pandigital(nums):
      ......
      return lst


输入格式:
多个数字串，中间用一个逗号隔开

输出格式：
满足条件的数字串，分行输出
输入
1243,322,321,1212,2354
输出
1243
321
提示
if __name__ == "__main__":

      lst = pandigital(eval(input()))

      调用函数根据结果输出
'''


def pandigital(nums:str):
    length=len(nums)
    if length>9:
        return 0
    for i in range(1,length+1):
        if nums.count(str(i))>1 or nums.count(str(i))==0:
            return 0
    return 1

if __name__=='__main__':
    lst=input().split(',')
    ans=[]
    for num in lst:
        if pandigital(num):
            ans.append(num)
    if len(ans)==0:
        print('not found')
    else:
        print(*ans,sep='\n')