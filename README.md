# Python
## 知识点
### 命名规则
- 以字母下划线开头，后跟字母、下划线和数字；不准以数字开头
### 关键字（保留字）
- 是指在编程语言内部定义并保留使用的标识符，python3.x有35个保留字，分别为：
```python
#引入模块：
import keyword

k= keyword.kwlist
#查看保留字个数
print("python保留字个数:"+str(len(k))+"个")
#列出保留字
print(k)

# 打印出：
"""
python保留字个数: 35个

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 
'with', 'yield']
"""

```
### 源文件扩展名
- python一般常用扩展名(后缀名)为.py
### 程序设计IPO模式
- I:Input输入，程序的输入
- P:Process处理，程序的主要逻辑
- O:Option输出，程序的主要输出
### 字符串比较规则
- 从第一个字符串开始，位置一一对应比较编码的大小，从字符串左边开始，依次比较每个字符，直接出现差异、或者其中一个串结束为止
### 注释
- #后面的为注释内容
```python
# 普通注释
print("hellow world") # 人生的第一个代码

"""
这是一个多行注释,
这种文档字符串不仅提高了代码的可读性，还便于其他开发人员理解你的代码。
"""
def python_one(text):
    """
    返回传入的文本。

    :param text: 需要返回的文本。
    :return: 传入的文本。
    """
    return text

```
### 数据类型
#### 浮点数
- 浮点数是带有小数的数字，它在Python中使用IEEE 754标准进行存储，存在范围限制（通常在-10^308到10^308之间），如果计算结果超出这个范围，会产生溢出错误。
### 字典
- "键"可以是整数或字符串，也可以是函数、元组、类等不可变类型