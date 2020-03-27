import re

# re.match是⽤来进⾏正则匹配检查的⽅法，若字符串匹配正则表达式，则match⽅法返回匹配对象,group⽤来返回字符串的匹配部分
result = re.match("itcast", "itcast.cn").group()
print(result)

# 匹配0到9第⼆种写法:[]代表匹配[ ]中列举的字符
ret = re.match("[0-9]", "7Hello Python").group()
print(ret)

# Python中字符串前⾯加上r表示原⽣字符串
mm = "c:\\a\\b\\c"
ret1 = re.match(r"c:\\a", mm).group()
print(ret1)

# 题⽬1：匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
ret2 = re.match("[a-zA-Z0-9_]{4,20}@163.com", "56hello@163.com").group()
print(ret2)

# 需求：匹配出0-100之间的数字: | 代表匹配左右任意⼀个表达式
ret3 = re.match("[1-9]?\d$|100", "8").group()
print(ret3)

# 匹配出163、126、qq邮箱之间的数字,() 将括号中字符作为⼀个分组
ret4 = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com").group()
print(ret4)

# search、findall
ret5 = re.search(r"\d+", "阅读次数为 9999").group()
print(ret5)
ret6 = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret6)

# sub 将匹配到的数据进⾏替换
ret7 = re.sub(r"\d+", '998', "python = 997")
print(ret7)

# split 根据匹配进⾏切割字符串，并返回⼀个列表
# 切割字符串"info:xiaoZhang 33 shandong" 根据：和空格分割
ret8 = re.split(r":| ", "info:xiaoZhang 33 shandong")
print(ret8)

# group(1)代表第一个group的值
s = "This is a number 234-235-22-423"
r = re.match(".+(\d+-\d+-\d+-\d+)", s).group(1)
print(r)
