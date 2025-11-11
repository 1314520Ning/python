你的 Python 知识点整理非常全面！以下是对内容的**结构化梳理 + 补充建议**，便于学习、复习或教学使用：

---

# 🐍 Python 核心知识点汇总（结构优化版）

## 1. **命名规则**
- 必须以 **字母（a–z, A–Z）或下划线 `_`** 开头。
- 后续字符可为：字母、数字（0–9）、下划线。
- ❌ 禁止以数字开头（如 `1var` 非法）。
- 区分大小写：`name` ≠ `Name`。
- 建议使用 **小写字母+下划线**（snake_case）命名变量和函数。

> ✅ 合法示例：`user_name`, `_temp`, `count2`  
> ❌ 非法示例：`2name`, `my-variable`, `class`（保留字）

---

## 2. **关键字（保留字）**
Python 3.x 共 **35 个保留字**，不可用作标识符。

```python
import keyword
print("保留字个数:", len(keyword.kwlist))
print(keyword.kwlist)
```

输出：
```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
 'with', 'yield']
```

> 💡 记忆技巧：控制流（if/for/while）、函数（def/return）、异常（try/except）、作用域（global/nonlocal）等。

---

## 3. **源文件扩展名**
- 标准扩展名：`.py`
- 字节码缓存：`.pyc`（自动生成，无需手动创建）
- 模块包目录：需包含 `__init__.py`

---

## 4. **程序设计 IPO 模式**
| 阶段 | 说明 |
|------|------|
| **I (Input)** | 获取数据（用户输入、文件、网络等） |
| **P (Process)** | 核心逻辑处理（计算、判断、循环等） |
| **O (Output)** | 输出结果（打印、写文件、返回值等） |

> 示例：  
> ```python
> name = input("请输入姓名: ")          # I
> greeting = f"你好, {name}!"         # P
> print(greeting)                     # O
> ```

---

## 5. **字符串比较规则**
- **逐字符比较 Unicode 编码值**（从左到右）。
- 一旦某位字符不同，立即得出结果。
- 若一个字符串是另一个的前缀，则**短的小于长的**。

```python
"apple" < "banana"   # True（'a' < 'b'）
"abc" < "abcd"       # True（前缀关系）
"Zoo" < "apple"      # True（'Z'=90, 'a'=97 → 大写字母编码更小！）
```

> ⚠️ 注意：大小写敏感！建议比较前统一 `.lower()`。

---

## 6. **注释**
- **单行注释**：`# 这是注释`
- **多行注释 / 文档字符串**：用 `"""..."""` 或 `'''...'''`
  - 函数/类开头的文档字符串可通过 `help(func)` 查看。

```python
def add(a, b):
    """返回两个数的和"""
    return a + b
```

---

## 7. **基本数据类型**
| 类型 | 说明 |
|------|------|
| `int` | 整数（无限精度） |
| `float` | 浮点数（IEEE 754 双精度，范围 ≈ ±1.8e308） |
| `str` | 字符串（Unicode） |
| `bool` | 布尔值（`True` / `False`） |
| `list` | 有序可变序列 |
| `tuple` | 有序不可变序列 |
| `dict` | 键值对映射（key 必须为**不可变类型**） |
| `set` | 无序不重复集合 |

> 🔑 字典的 key 要求：**不可变（immutable）**  
> ✅ 合法 key：`str`, `int`, `tuple`（元素也需不可变）  
> ❌ 非法 key：`list`, `dict`, `set`

---

## 8. **Python 语言特点**
- ✅ **开源免费**（PSF 协议）
- ✅ **跨平台**（Windows/macOS/Linux）
- ✅ **解释型脚本语言**（无需编译，逐行解释执行）
- ✅ **动态类型**（变量无需声明类型）
- ✅ **自动内存管理**（垃圾回收机制）
- ✅ **丰富的标准库 & 第三方生态**

---

## 9. **循环控制**
| 关键字 | 作用 |
|--------|------|
| `break` | **立即退出整个循环** |
| `continue` | **跳过本次循环剩余代码，进入下一次迭代** |

```python
for i in range(5):
    if i == 2:
        continue  # 跳过 i=2
    if i == 4:
        break     # 在 i=4 时终止循环
    print(i)      # 输出: 0, 1, 3
```

---

## 10. **运算符速查表**

### 🔢 算术运算符
| 符号 | 说明 |
|------|------|
| `+` | 加 |
| `-` | 减 / 取负 |
| `*` | 乘 / 字符串重复 |
| `/` | 浮点除 |
| `//` | 整除（向下取整） |
| `%` | 取模（余数） |
| `**` | 幂运算 |

### 🔍 比较运算符
`==`, `!=`, `>`, `<`, `>=`, `<=`

### 🔄 赋值运算符
`=`, `+=`, `-=`, `*=`, `/=`, `%=`, `//=`, `**=`

### 🧠 逻辑运算符
`and`, `or`, `not`  
> 短路求值：`False and ...` 不计算后面；`True or ...` 不计算后面

### 🧩 其他符号
| 符号 | 用途 |
|------|------|
| `#` | 单行注释 |
| `"""` / `'''` | 多行字符串 / 注释 |
| `()` | 函数调用、元组、优先级 |
| `[]` | 列表、索引 |
| `{}` | 字典、集合 |
| `@` | 装饰器（如 `@staticmethod`） |
| `:` | 代码块开始（if/for/def/class 后） |
| `->` | 函数返回类型提示（如 `def f() -> int:`） |
| `>>>` | Python 交互式提示符 |

---

## ✅ 补充建议（进阶）

1. **类型提示（Type Hints）**（Python 3.5+）
   ```python
   def greet(name: str) -> str:
       return f"Hello, {name}"
   ```

2. **f-string 格式化**（Python 3.6+）
   ```python
   name = "Alice"
   print(f"Hello, {name.upper()}!")  # Hello, ALICE!
   ```

3. **虚拟环境管理**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Linux/macOS
   myenv\Scripts\activate     # Windows
   ```

---

这份整理既适合初学者建立知识框架，也方便老手快速查阅。你可以将其保存为 Markdown 或 PDF 作为学习手册！需要我帮你生成 **思维导图大纲** 或 **练习题** 吗？
