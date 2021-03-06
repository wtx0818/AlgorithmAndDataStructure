# -*- coding:utf-8 -*-
'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
复制

+2147483647
    1a33
+123
size=4
i=1
1*10^2
size-i-1
123
size=3
i=0
1*10^2
size-0-1

输出
复制
2147483647
    0
'''


class Solution:
    def StrToInt(self, s):
        # write code here
        if s=="":
            return 0
        listS = list(s)
        flag = 0
        index = 0
        standard = 1
        sum = 0
        CharList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        if listS[0] == '-':
            index += 1
            standard = -1
        if listS[0] == '+':
            index += 1

        size = len(listS)

        for i in range(index, size):
            if flag != 0:
                return 0

            if listS[i] >= '0' and listS[i] <= '9':
                cur = size - i - 1
                sum = sum + (int(listS[i]) - 0) * pow(10, cur)

            else:
                flag = 1

        return standard * sum


s = Solution()
print s.StrToInt("123")
