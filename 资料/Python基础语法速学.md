# Python 基础语法速学

> 面向零基础学生的 Python 入门指南，两小时掌握核心语法。
> 所有示例均可直接复制运行。

---

## 目录

- [1. 第一个程序 — print()](#1-第一个程序--print)
- [2. 变量与数据类型](#2-变量与数据类型)
- [3. input() 输入](#3-input-输入)
- [4. 类型转换](#4-类型转换)
- [5. 运算符](#5-运算符)
- [6. 字符串操作](#6-字符串操作)
- [7. 条件判断 if/elif/else](#7-条件判断-ifelifelse)
- [8. 循环 — for](#8-循环--for)
- [9. 循环 — while](#9-循环--while)
- [10. break 和 continue](#10-break-和-continue)
- [11. 列表 list](#11-列表-list)
- [12. 元组 tuple](#12-元组-tuple)
- [13. 字典 dict](#13-字典-dict)
- [14. 集合 set](#14-集合-set)
- [15. 函数 def](#15-函数-def)
- [16. 函数参数详解](#16-函数参数详解)
- [17. return 返回值](#17-return-返回值)
- [18. 模块与 import](#18-模块与-import)
- [19. 文件读写](#19-文件读写)
- [20. 异常处理 try/except](#20-异常处理-tryexcept)
- [21. 类与对象（入门）](#21-类与对象入门)
- [22. 常用内置函数速查](#22-常用内置函数速查)
- [附录：练习题](#附录练习题)

---

## 1. 第一个程序 — print()

`print()` 用于在屏幕上输出内容，是最基础的函数。

```python
print(值1, 值2, ..., sep=' ', end='\n')
```

| 参数 | 说明 |
|------|------|
| `值` | 要输出的内容，可以是多个，用逗号隔开 |
| `sep` | 多个值之间的分隔符，默认空格 |
| `end` | 输出末尾的字符，默认换行 `\n` |

```python
# 输出文字
print("Hello, World!")

# 输出多个值
print("我叫", "小明", "今年", 18, "岁")
# 输出: 我叫 小明 今年 18 岁

# 改变分隔符
print("2025", "01", "15", sep="-")
# 输出: 2025-01-15

# 不换行输出
print("Hello", end=" ")
print("World")
# 输出: Hello World
```

---

## 2. 变量与数据类型

变量就是给数据取一个名字，方便之后使用。**不需要声明类型**，直接赋值即可。

### 变量命名规则

- 只能包含字母、数字、下划线 `_`
- 不能以数字开头
- 区分大小写（`name` 和 `Name` 是不同的变量）
- 不能使用 Python 关键字（如 `if`, `for`, `class` 等）

### 四种基本数据类型

| 类型 | 说明 | 例子 |
|------|------|------|
| `int` | 整数 | `10`, `-3`, `0` |
| `float` | 小数（浮点数）| `3.14`, `-0.5`, `1.0` |
| `str` | 字符串（文字）| `"hello"`, `'你好'` |
| `bool` | 布尔值（真/假）| `True`, `False` |

```python
# 整数
age = 18
print(age)        # 18

# 小数
price = 9.99
print(price)      # 9.99

# 字符串（用单引号或双引号都可以）
name = "小明"
greeting = '你好'
print(name)       # 小明

# 布尔值
is_student = True
print(is_student) # True

# 查看变量的类型
print(type(age))       # <class 'int'>
print(type(price))     # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_student))# <class 'bool'>
```

### `type()` 函数

```python
type(对象)
```

| 参数 | 说明 |
|------|------|
| `对象` | 任何 Python 对象 |
| **返回值** | 该对象的类型 |

**场景：** 调试时检查变量类型。

---

## 3. input() 输入

`input()` 让程序等待用户输入，**返回值永远是字符串**。

```python
result = input(提示文字)
```

| 参数 | 说明 |
|------|------|
| `提示文字` | 显示给用户看的提示（可省略）|
| **返回值** | 用户输入的字符串 `str` |

```python
name = input("请输入你的名字：")
print("你好，" + name + "！")
```

```python
# 注意：input 返回的是字符串，不能直接做数学运算
age_str = input("请输入你的年龄：")
age = int(age_str)    # 转成整数才能计算
print("明年你", age + 1, "岁")
```

---

## 4. 类型转换

不同类型之间需要手动转换。

| 函数 | 说明 | 例子 |
|------|------|------|
| `int(x)` | 转为整数 | `int("10")` → `10` |
| `float(x)` | 转为小数 | `float("3.14")` → `3.14` |
| `str(x)` | 转为字符串 | `str(100)` → `"100"` |
| `bool(x)` | 转为布尔值 | `bool(0)` → `False` |
| `list(x)` | 转为列表 | `list("abc")` → `['a','b','c']` |

```python
# 字符串 → 整数
num = int("42")
print(num + 8)    # 50

# 整数 → 字符串
age = 18
message = "我今年" + str(age) + "岁"
print(message)    # 我今年18岁

# 字符串 → 小数
pi = float("3.14")
print(pi * 2)     # 6.28

# 布尔值转换规则：0、空字符串、空列表、None → False，其他 → True
print(bool(0))     # False
print(bool(1))     # True
print(bool(""))    # False
print(bool("hi"))  # True
```

---

## 5. 运算符

### 算术运算符

| 运算符 | 说明 | 例子 | 结果 |
|--------|------|------|------|
| `+` | 加 | `3 + 2` | `5` |
| `-` | 减 | `3 - 2` | `1` |
| `*` | 乘 | `3 * 2` | `6` |
| `/` | 除（结果为小数）| `7 / 2` | `3.5` |
| `//` | 整除（向下取整）| `7 // 2` | `3` |
| `%` | 取余数 | `7 % 2` | `1` |
| `**` | 幂（次方）| `2 ** 3` | `8` |

```python
print(10 + 3)    # 13
print(10 - 3)    # 7
print(10 * 3)    # 30
print(10 / 3)    # 3.3333...
print(10 // 3)   # 3
print(10 % 3)    # 1
print(2 ** 10)   # 1024
```

### 比较运算符（结果为 True 或 False）

| 运算符 | 说明 | 例子 | 结果 |
|--------|------|------|------|
| `==` | 等于 | `3 == 3` | `True` |
| `!=` | 不等于 | `3 != 5` | `True` |
| `>` | 大于 | `5 > 3` | `True` |
| `<` | 小于 | `3 < 5` | `True` |
| `>=` | 大于等于 | `5 >= 5` | `True` |
| `<=` | 小于等于 | `3 <= 5` | `True` |

```python
print(10 == 10)   # True
print(10 != 5)    # True
print(10 > 20)    # False
print(5 <= 5)     # True
```

### 逻辑运算符

| 运算符 | 说明 | 例子 |
|--------|------|------|
| `and` | 且，两个都为真才为真 | `True and False` → `False` |
| `or` | 或，一个为真就为真 | `True or False` → `True` |
| `not` | 取反 | `not True` → `False` |

```python
age = 20
# 判断年龄在 18 到 60 之间
print(age >= 18 and age <= 60)  # True

score = 85
# 判断是否及格或者有加分
print(score >= 60 or score >= 50)  # True

is_raining = False
print(not is_raining)  # True（没下雨）
```

### 赋值运算符

| 运算符 | 等价写法 | 例子 |
|--------|----------|------|
| `=` | 赋值 | `x = 10` |
| `+=` | `x = x + n` | `x += 3` |
| `-=` | `x = x - n` | `x -= 2` |
| `*=` | `x = x * n` | `x *= 4` |
| `/=` | `x = x / n` | `x /= 2` |
| `//=` | `x = x // n` | `x //= 3` |
| `%=` | `x = x % n` | `x %= 3` |

```python
score = 100
score += 10   # score 变成 110
score -= 20   # score 变成 90
score *= 2    # score 变成 180
print(score)  # 180
```

---

## 6. 字符串操作

字符串是最常用的数据类型之一。

### 创建字符串

```python
s1 = "双引号字符串"
s2 = '单引号字符串'
s3 = """
多行
字符串
"""
```

### 字符串拼接

```python
first = "Hello"
second = "World"

# 用 + 拼接
result = first + " " + second
print(result)  # Hello World

# 用 f-string 格式化（最推荐，Python 3.6+）
name = "小明"
age = 18
print(f"我叫{name}，今年{age}岁")
# 输出：我叫小明，今年18岁

# f-string 里可以写表达式
print(f"明年{age + 1}岁")
# 输出：明年19岁
```

### 字符串索引与切片

字符串中每个字符都有编号（索引），**从 0 开始**。

```python
s = "Hello"

# 索引（取单个字符）
print(s[0])    # H
print(s[1])    # e
print(s[-1])   # o（-1 表示最后一个）

# 切片（取一段）：s[开始:结束]，不含结束位置
print(s[0:3])  # Hel
print(s[1:4])  # ell
print(s[:3])   # Hel（从头开始可省略0）
print(s[2:])   # llo（到末尾可省略）
print(s[:])    # Hello（完整复制）

# 带步长：s[开始:结束:步长]
print(s[::2])  # Hlo（每隔一个取）
print(s[::-1]) # olleH（倒序）
```

### 常用字符串方法

| 方法 | 说明 | 例子 |
|------|------|------|
| `len(s)` | 字符串长度 | `len("abc")` → `3` |
| `s.upper()` | 转大写 | `"hello".upper()` → `"HELLO"` |
| `s.lower()` | 转小写 | `"HELLO".lower()` → `"hello"` |
| `s.strip()` | 去掉两端空白 | `" hi ".strip()` → `"hi"` |
| `s.lstrip()` | 去掉左端空白 | `" hi ".lstrip()` → `"hi "` |
| `s.rstrip()` | 去掉右端空白 | `" hi ".rstrip()` → `" hi"` |
| `s.replace(旧, 新)` | 替换 | `"abc".replace("a","x")` → `"xbc"` |
| `s.split(分隔符)` | 分割成列表 | `"a-b-c".split("-")` → `['a','b','c']` |
| `s.join(列表)` | 用 s 连接列表 | `"-".join(["a","b"])` → `"a-b"` |
| `s.find(子串)` | 查找位置（没找到返回-1）| `"hello".find("ll")` → `2` |
| `s.count(子串)` | 统计出现次数 | `"aaba".count("a")` → `3` |
| `s.startswith(前缀)` | 是否以指定开头 | `"hello".startswith("he")` → `True` |
| `s.endswith(后缀)` | 是否以指定结尾 | `"hello".endswith("lo")` → `True` |
| `s.isdigit()` | 是否全是数字 | `"123".isdigit()` → `True` |
| `s.isalpha()` | 是否全是字母 | `"abc".isalpha()` → `True` |
| `s.title()` | 每个单词首字母大写 | `"hello world".title()` → `"Hello World"` |

```python
# 综合示例
sentence = "  Hello, World!  "

print(len(sentence))              # 17
print(sentence.strip())           # "Hello, World!"
print(sentence.strip().lower())   # "hello, world!"
print(sentence.strip().replace("World", "Python"))  # "Hello, Python!"

# 分割与合并
fruits = "苹果,香蕉,橘子"
fruit_list = fruits.split(",")
print(fruit_list)                 # ['苹果', '香蕉', '橘子']

joined = " | ".join(fruit_list)
print(joined)                     # 苹果 | 香蕉 | 橘子

# 查找
email = "student@school.com"
print(email.find("@"))            # 7
print(email.endswith(".com"))     # True
```

### `in` 关键字（检查是否包含）

```python
print("he" in "hello")     # True
print("xyz" in "hello")    # False
print("a" not in "hello")  # True
```

---

## 7. 条件判断 if/elif/else

根据条件执行不同的代码。**注意缩进**，Python 用缩进（4个空格）表示代码块。

### 基本语法

```python
if 条件:
    # 条件为 True 时执行
    代码
elif 另一个条件:
    # 上面不满足，这个满足时执行
    代码
else:
    # 以上都不满足时执行
    代码
```

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
# 输出：良好
```

### 嵌套判断

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("可以入场")
    else:
        print("请先买票")
else:
    print("未满18岁不能入场")
```

### 组合条件

```python
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
    print("适合出去玩")

username = "admin"
if username == "admin" or username == "root":
    print("管理员你好")
```

### 完整示例：简易计算器

```python
num1 = float(input("输入第一个数："))
op = input("输入运算符(+, -, *, /)：")
num2 = float(input("输入第二个数："))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("错误：不能除以0")
        result = None
    else:
        result = num1 / num2
else:
    print("不支持的运算符")
    result = None

if result is not None:
    print(f"{num1} {op} {num2} = {result}")
```

---

## 8. 循环 — for

`for` 循环用于遍历序列（列表、字符串、范围等）。

### 基本语法

```python
for 变量 in 可迭代对象:
    代码
```

### 遍历字符串

```python
for char in "Hello":
    print(char)
# 输出：H e l l o（每行一个）
```

### 遍历列表

```python
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"我喜欢{fruit}")
```

### range() 函数

`range()` 生成一个数字序列，常配合 `for` 使用。

```python
range(结束)              # 从0到结束-1
range(开始, 结束)        # 从开始到结束-1
range(开始, 结束, 步长)  # 从开始到结束-1，每次加步长
```

| 参数 | 说明 |
|------|------|
| `结束` | 不包含此值 |
| `开始` | 起始值（默认0）|
| `步长` | 每次递增量（默认1）|

```python
# 打印 0 到 4
for i in range(5):
    print(i)    # 0 1 2 3 4

# 打印 1 到 10
for i in range(1, 11):
    print(i)    # 1 2 3 ... 10

# 偶数：0 2 4 6 8
for i in range(0, 10, 2):
    print(i)

# 倒数：5 4 3 2 1
for i in range(5, 0, -1):
    print(i)
```

### 带索引遍历：enumerate()

```python
enumerate(可迭代对象, start=0)
```

| 参数 | 说明 |
|------|------|
| `可迭代对象` | 列表、字符串等 |
| `start` | 编号起始值，默认0 |

```python
fruits = ["苹果", "香蕉", "橘子"]
for index, fruit in enumerate(fruits):
    print(f"第{index}个: {fruit}")
# 第0个: 苹果
# 第1个: 香蕉
# 第2个: 橘子

# 从1开始编号
for index, fruit in enumerate(fruits, start=1):
    print(f"第{index}个: {fruit}")
```

### for...else

```python
# else 在循环正常结束（没有 break）时执行
for i in range(5):
    if i == 10:
        print("找到了")
        break
else:
    print("没找到")
# 输出：没找到
```

### 完整示例：九九乘法表

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # 换行
```

---

## 9. 循环 — while

`while` 在条件为 `True` 时持续执行。

### 基本语法

```python
while 条件:
    代码
    # 记得更新条件，否则死循环！
```

```python
# 从1加到100
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"1到100的和 = {total}")
# 输出：1到100的和 = 5050
```

### 完整示例：猜数字游戏

```python
import random

answer = random.randint(1, 100)
count = 0

print("=== 猜数字游戏 ===")
print("我想了一个1到100之间的数")

while True:
    guess = int(input("你猜几？"))
    count += 1

    if guess < answer:
        print("太小了！")
    elif guess > answer:
        print("太大了！")
    else:
        print(f"恭喜！猜对了！用了{count}次")
        break
```

---

## 10. break 和 continue

| 关键字 | 作用 |
|--------|------|
| `break` | 立刻退出当前循环 |
| `continue` | 跳过本次循环的剩余部分，进入下一次 |

```python
# break 示例：找到第一个能被7整除的数
for i in range(1, 100):
    if i % 7 == 0:
        print(f"第一个能被7整除的是: {i}")
        break
# 输出：第一个能被7整除的是: 7

# continue 示例：跳过偶数，只打印奇数
for i in range(10):
    if i % 2 == 0:
        continue   # 跳过偶数
    print(i)
# 输出：1 3 5 7 9
```

---

## 11. 列表 list

列表是最常用的数据结构，可以存放**任意类型**的多个元素，**可以修改**。

### 创建列表

```python
# 空列表
empty = []
empty2 = list()

# 有初始值的列表
numbers = [1, 2, 3, 4, 5]
names = ["小明", "小红", "小刚"]
mixed = [1, "hello", True, 3.14]  # 可以混合类型
```

### 访问元素（索引和切片，与字符串相同）

```python
fruits = ["苹果", "香蕉", "橘子", "葡萄", "西瓜"]

print(fruits[0])     # 苹果
print(fruits[-1])    # 西瓜
print(fruits[1:3])   # ['香蕉', '橘子']

# 修改元素
fruits[0] = "草莓"
print(fruits)        # ['草莓', '香蕉', '橘子', '葡萄', '西瓜']
```

### 常用列表方法

| 方法 | 说明 | 例子 |
|------|------|------|
| `len(lst)` | 列表长度 | `len([1,2,3])` → `3` |
| `lst.append(x)` | 末尾添加元素 | `[1,2].append(3)` → `[1,2,3]` |
| `lst.insert(i, x)` | 在位置 i 插入 | `[1,3].insert(1, 2)` → `[1,2,3]` |
| `lst.extend(另一列表)` | 合并另一个列表 | `[1].extend([2,3])` → `[1,2,3]` |
| `lst.remove(x)` | 删除第一个值为 x 的 | `[1,2,3].remove(2)` → `[1,3]` |
| `lst.pop(i)` | 删除并返回位置 i 的元素 | `[1,2,3].pop(1)` → 返回`2` |
| `lst.pop()` | 删除并返回最后一个 | `[1,2,3].pop()` → 返回`3` |
| `lst.clear()` | 清空列表 | |
| `lst.index(x)` | 查找 x 的位置 | `[1,2,3].index(2)` → `1` |
| `lst.count(x)` | 统计 x 出现次数 | `[1,1,2].count(1)` → `2` |
| `lst.sort()` | 排序（改变原列表）| `[3,1,2].sort()` → `[1,2,3]` |
| `lst.sort(reverse=True)` | 降序排序 | `[3,1,2].sort(reverse=True)` → `[3,2,1]` |
| `sorted(lst)` | 排序（返回新列表）| `sorted([3,1,2])` → `[1,2,3]` |
| `lst.reverse()` | 反转列表 | `[1,2,3].reverse()` → `[3,2,1]` |
| `lst.copy()` | 浅拷贝 | |
| `x in lst` | 判断是否在列表中 | `2 in [1,2,3]` → `True` |

```python
# 综合示例：管理购物清单
shopping = []

# 添加商品
shopping.append("牛奶")
shopping.append("面包")
shopping.append("鸡蛋")
shopping.append("牛奶")  # 可以重复
print(shopping)   # ['牛奶', '面包', '鸡蛋', '牛奶']

# 在指定位置插入
shopping.insert(1, "黄油")
print(shopping)   # ['牛奶', '黄油', '面包', '鸡蛋', '牛奶']

# 删除
shopping.remove("牛奶")   # 只删除第一个
print(shopping)   # ['黄油', '面包', '鸡蛋', '牛奶']

# 弹出最后一个
last = shopping.pop()
print(f"取出: {last}")    # 取出: 牛奶
print(shopping)           # ['黄油', '面包', '鸡蛋']

# 排序
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print(numbers)   # [1, 2, 3, 5, 8, 9]

# 检查元素是否存在
print("面包" in shopping)  # True
print("苹果" in shopping)  # False

# 列表长度
print(len(shopping))  # 3
```

### 遍历列表

```python
colors = ["红", "绿", "蓝"]

# 方式一：直接遍历
for color in colors:
    print(color)

# 方式二：用索引遍历
for i in range(len(colors)):
    print(f"第{i}个颜色是{colors[i]}")

# 方式三：enumerate
for i, color in enumerate(colors):
    print(f"索引{i}: {color}")
```

---

## 12. 元组 tuple

元组和列表类似，但**创建后不能修改**（不可变）。

### 创建元组

```python
# 用小括号
point = (3, 5)
colors = ("红", "绿", "蓝")

# 只有一个元素时必须加逗号
single = (42,)

# 其实不加括号也行
coords = 10, 20
```

### 使用元组

```python
point = (3, 5)

# 访问（和列表一样）
print(point[0])   # 3
print(point[1])   # 5

# 不能修改！以下会报错：
# point[0] = 10   # TypeError!

# 解包（把元组的值分别赋给多个变量）
x, y = point
print(x)  # 3
print(y)  # 5

# 常用方法
colors = ("红", "绿", "蓝", "红")
print(len(colors))        # 4
print(colors.count("红"))  # 2
print(colors.index("蓝"))  # 2
```

**什么时候用元组？**
- 数据不应该被修改时（如坐标点、RGB颜色值）
- 函数返回多个值时
- 字典的键（列表不能做键，元组可以）

```python
# 函数返回多个值（其实就是返回元组）
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([3, 1, 5, 2, 4])
print(result)      # (1, 5)

smallest, largest = get_min_max([3, 1, 5, 2, 4])
print(smallest)    # 1
print(largest)     # 5
```

---

## 13. 字典 dict

字典存储**键值对（key: value）**，用键来快速查找值。

### 创建字典

```python
# 空字典
empty = {}
empty2 = dict()

# 有初始值
student = {
    "name": "小明",
    "age": 18,
    "grade": "高三"
}
```

### 基本操作

```python
student = {"name": "小明", "age": 18, "grade": "高三"}

# 获取值
print(student["name"])       # 小明
print(student.get("age"))    # 18

# get() 可以设置默认值（键不存在时返回默认值，不会报错）
print(student.get("phone", "未设置"))  # 未设置

# 修改 / 新增
student["age"] = 19          # 修改已有的
student["phone"] = "12345"   # 新增
print(student)
# {'name': '小明', 'age': 19, 'grade': '高三', 'phone': '12345'}

# 删除
del student["phone"]
# 或者
removed = student.pop("grade")   # 删除并返回值
print(removed)  # 高三

# 检查键是否存在
print("name" in student)    # True
print("email" in student)   # False
```

### 常用字典方法

| 方法 | 说明 |
|------|------|
| `d[key]` | 获取值（键不存在会报错）|
| `d.get(key, default)` | 获取值（安全，不存在返回 default）|
| `d[key] = value` | 设置/修改值 |
| `del d[key]` | 删除键值对 |
| `d.pop(key, default)` | 删除并返回值 |
| `d.keys()` | 所有键 |
| `d.values()` | 所有值 |
| `d.items()` | 所有键值对 |
| `d.update(other_dict)` | 合并另一个字典 |
| `len(d)` | 键值对数量 |
| `key in d` | 判断键是否存在 |
| `d.clear()` | 清空 |
| `d.copy()` | 浅拷贝 |
| `d.setdefault(key, default)` | 键不存在时设置默认值并返回 |

### 遍历字典

```python
student = {"name": "小明", "age": 18, "score": 95}

# 遍历键
for key in student:
    print(key)
# name  age  score

# 遍历值
for value in student.values():
    print(value)
# 小明  18  95

# 遍历键和值
for key, value in student.items():
    print(f"{key}: {value}")
# name: 小明
# age: 18
# score: 95
```

### 完整示例：词频统计

```python
text = "the cat sat on the mat the cat"
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# 找出出现最多的词
max_word = ""
max_count = 0
for word, count in word_count.items():
    if count > max_count:
        max_count = count
        max_word = word

print(f"出现最多的词: '{max_word}', 共{max_count}次")
```

---

## 14. 集合 set

集合中的元素**不重复**、**无序**。

### 创建集合

```python
# 用花括号（注意：空花括号 {} 是字典，不是集合）
fruits = {"苹果", "香蕉", "橘子", "苹果"}
print(fruits)  # {'香蕉', '苹果', '橘子'}（自动去重，顺序不固定）

# 空集合必须用 set()
empty = set()

# 从列表去重
numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)
print(unique)  # {1, 2, 3}
```

### 常用操作

| 方法 | 说明 |
|------|------|
| `s.add(x)` | 添加元素 |
| `s.remove(x)` | 删除（不存在会报错）|
| `s.discard(x)` | 删除（不存在不报错）|
| `s.pop()` | 随机删除一个 |
| `s.clear()` | 清空 |
| `len(s)` | 元素个数 |
| `x in s` | 是否在集合中 |

### 集合运算

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 交集（两个都有的）
print(a & b)       # {3, 4}
print(a.intersection(b))

# 并集（合在一起）
print(a | b)       # {1, 2, 3, 4, 5, 6}
print(a.union(b))

# 差集（a 有 b 没有的）
print(a - b)       # {1, 2}
print(a.difference(b))

# 对称差集（只在一个中出现的）
print(a ^ b)       # {1, 2, 5, 6}
```

**场景：** 去重、成员检测（比列表快得多）、集合运算。

```python
# 实用：列表去重并保持原顺序
names = ["小明", "小红", "小明", "小刚", "小红"]
seen = set()
unique_names = []
for name in names:
    if name not in seen:
        seen.add(name)
        unique_names.append(name)
print(unique_names)  # ['小明', '小红', '小刚']
```

---

## 15. 函数 def

函数是一段可以重复使用的代码块。

### 基本语法

```python
def 函数名(参数1, 参数2, ...):
    """函数说明文档（可选）"""
    代码
    return 返回值    # 可选
```

```python
# 定义函数
def greet(name):
    """打招呼函数"""
    print(f"你好，{name}！")

# 调用函数
greet("小明")   # 你好，小明！
greet("小红")   # 你好，小红！
```

```python
# 带计算的函数
def add(a, b):
    result = a + b
    return result

total = add(3, 5)
print(total)   # 8
```

### 无参数函数

```python
def say_hello():
    print("Hello!")

say_hello()  # Hello!
```

### 无返回值函数

```python
def print_line():
    print("-" * 30)

print_line()  # ------------------------------
```

---

## 16. 函数参数详解

### 位置参数（最基本的参数）

```python
def power(base, exponent):
    return base ** exponent

print(power(2, 3))   # 8
```

### 默认参数

```python
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}！")

greet("小明")            # 你好，小明！
greet("小明", "早上好")  # 早上好，小明！
```

### 关键字参数（按名字传参）

```python
def create_student(name, age, grade):
    print(f"姓名:{name}, 年龄:{age}, 年级:{grade}")

# 可以打乱顺序
create_student(age=18, grade="高三", name="小明")
```

### 多个返回值

```python
def divide(a, b):
    quotient = a // b   # 商
    remainder = a % b   # 余数
    return quotient, remainder

q, r = divide(17, 5)
print(f"商: {q}, 余数: {r}")  # 商: 3, 余数: 2
```

### 完整示例

```python
def calculate_bmi(weight, height):
    """
    计算 BMI 指数
    weight: 体重(kg)
    height: 身高(m)
    """
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        status = "偏瘦"
    elif bmi < 24:
        status = "正常"
    elif bmi < 28:
        status = "偏胖"
    else:
        status = "肥胖"

    return bmi, status

bmi_value, bmi_status = calculate_bmi(65, 1.75)
print(f"BMI: {bmi_value:.1f}, 状态: {bmi_status}")
# BMI: 21.2, 状态: 正常
```

---

## 17. return 返回值

- `return` 结束函数并返回值
- 没有 `return` 或只写 `return`，函数返回 `None`
- 可以返回任何类型

```python
def is_even(n):
    """判断是否是偶数"""
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False

# 用在条件判断中
if is_even(10):
    print("10是偶数")
```

```python
def find_first_negative(numbers):
    """找到第一个负数，没有则返回 None"""
    for n in numbers:
        if n < 0:
            return n    # 找到就立即返回，函数结束
    return None         # 没找到

result = find_first_negative([3, 5, -2, 8, -1])
print(result)  # -2

result = find_first_negative([3, 5, 8])
print(result)  # None
```

---

## 18. 模块与 import

模块就是一个 `.py` 文件，可以导入里面的函数和变量来使用。

### 导入方式

```python
# 方式一：导入整个模块
import math
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.141592653589793

# 方式二：导入模块中的特定内容
from math import sqrt, pi
print(sqrt(16))          # 4.0
print(pi)                # 3.14...

# 方式三：给模块取别名
import random as rd
print(rd.randint(1, 10))
```

### 常用标准库模块

#### math — 数学函数

| 函数 | 说明 | 例子 |
|------|------|------|
| `math.sqrt(x)` | 平方根 | `math.sqrt(25)` → `5.0` |
| `math.pow(x, y)` | x 的 y 次方 | `math.pow(2, 3)` → `8.0` |
| `math.ceil(x)` | 向上取整 | `math.ceil(3.2)` → `4` |
| `math.floor(x)` | 向下取整 | `math.floor(3.8)` → `3` |
| `math.fabs(x)` | 绝对值 | `math.fabs(-5)` → `5.0` |
| `math.pi` | 圆周率 | `3.141592...` |
| `math.e` | 自然常数 | `2.718281...` |
| `math.sin/cos/tan(x)` | 三角函数（弧度）| |
| `math.radians(度)` | 角度转弧度 | `math.radians(180)` → `π` |
| `math.degrees(弧度)` | 弧度转角度 | `math.degrees(math.pi)` → `180` |
| `math.log(x)` | 自然对数 | |
| `math.log10(x)` | 以10为底的对数 | |
| `math.gcd(a, b)` | 最大公约数 | `math.gcd(12, 8)` → `4` |

```python
import math

# 计算圆的面积
radius = 5
area = math.pi * radius ** 2
print(f"半径{radius}的圆面积 = {area:.2f}")  # 78.54

# 取整
print(math.ceil(3.1))   # 4
print(math.floor(3.9))  # 3

# 三角函数
angle = math.radians(60)
print(f"sin(60°) = {math.sin(angle):.4f}")  # 0.8660
```

#### random — 随机数

| 函数 | 说明 | 例子 |
|------|------|------|
| `random.randint(a, b)` | 随机整数 [a, b] | `random.randint(1, 6)` |
| `random.random()` | 随机小数 [0, 1) | `random.random()` |
| `random.uniform(a, b)` | 随机小数 [a, b] | `random.uniform(1.5, 3.5)` |
| `random.choice(seq)` | 随机选一个 | `random.choice(["a","b","c"])` |
| `random.choices(seq, k=n)` | 随机选多个（可重复）| |
| `random.sample(seq, k=n)` | 随机选多个（不重复）| |
| `random.shuffle(lst)` | 打乱列表顺序 | |
| `random.seed(n)` | 设置随机种子（可复现）| |

```python
import random

# 掷骰子
dice = random.randint(1, 6)
print(f"骰子: {dice}")

# 随机选人
students = ["小明", "小红", "小刚", "小华"]
chosen = random.choice(students)
print(f"被选中: {chosen}")

# 随机打乱
cards = list(range(1, 14))
random.shuffle(cards)
print(f"洗牌: {cards}")

# 随机抽3个不重复的
lucky = random.sample(range(1, 100), 3)
print(f"幸运数字: {lucky}")
```

#### os — 操作系统交互

| 函数 | 说明 |
|------|------|
| `os.getcwd()` | 获取当前工作目录 |
| `os.listdir(path)` | 列出目录中的文件 |
| `os.path.exists(path)` | 路径是否存在 |
| `os.path.join(a, b)` | 拼接路径 |
| `os.path.basename(path)` | 获取文件名 |
| `os.path.dirname(path)` | 获取目录名 |
| `os.makedirs(path)` | 创建多级目录 |
| `os.path.isfile(path)` | 是否为文件 |
| `os.path.isdir(path)` | 是否为目录 |

```python
import os

print(os.getcwd())                        # 当前目录
print(os.path.exists("test.py"))          # 文件是否存在
print(os.path.join("folder", "file.txt")) # folder/file.txt 或 folder\file.txt
```

#### datetime — 日期时间

```python
from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()
print(now)                    # 2026-02-23 14:30:00.123456
print(now.year)               # 2026
print(now.month)              # 2
print(now.day)                # 23
print(now.hour)               # 14
print(now.minute)             # 30

# 格式化输出
print(now.strftime("%Y年%m月%d日 %H:%M:%S"))
# 2026年02月23日 14:30:00

# 时间计算
tomorrow = now + timedelta(days=1)
print(f"明天: {tomorrow.strftime('%Y-%m-%d')}")

last_week = now - timedelta(weeks=1)
print(f"上周: {last_week.strftime('%Y-%m-%d')}")
```

#### json — JSON 数据处理

```python
import json

# Python 字典 → JSON 字符串
data = {"name": "小明", "age": 18, "scores": [90, 85, 92]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

# JSON 字符串 → Python 字典
text = '{"name": "小红", "age": 17}'
obj = json.loads(text)
print(obj["name"])  # 小红
```

---

## 19. 文件读写

### 打开文件

```python
file = open(文件路径, 模式, encoding="utf-8")
```

| 模式 | 说明 |
|------|------|
| `"r"` | 读取（默认，文件不存在报错）|
| `"w"` | 写入（覆盖，文件不存在则创建）|
| `"a"` | 追加（在末尾添加）|
| `"r+"` | 读写 |

### 推荐用 with 语句（自动关闭文件）

```python
# 写文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

# 读取全部内容
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 逐行读取
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip() 去掉换行符

# 读取所有行到列表
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)  # ['第一行\n', '第二行\n', '第三行\n']

# 追加内容
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("第四行\n")
```

### 常用文件方法

| 方法 | 说明 |
|------|------|
| `f.read()` | 读取全部内容为字符串 |
| `f.read(n)` | 读取 n 个字符 |
| `f.readline()` | 读取一行 |
| `f.readlines()` | 读取所有行到列表 |
| `f.write(str)` | 写入字符串 |
| `f.writelines(list)` | 写入字符串列表 |
| `f.close()` | 关闭文件 |

### 完整示例：成绩管理

```python
# 写入成绩数据
students = [
    {"name": "小明", "score": 92},
    {"name": "小红", "score": 88},
    {"name": "小刚", "score": 75},
]

with open("scores.txt", "w", encoding="utf-8") as f:
    for s in students:
        f.write(f"{s['name']},{s['score']}\n")

print("成绩已保存！")

# 读取并统计
total = 0
count = 0

with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            name, score = line.split(",")
            score = int(score)
            total += score
            count += 1
            print(f"{name}: {score}分")

print(f"平均分: {total / count:.1f}")
```

---

## 20. 异常处理 try/except

当程序可能出错时，用 try/except 来让程序不会崩溃。

### 基本语法

```python
try:
    可能出错的代码
except 错误类型:
    出错时执行的代码
```

### 常见错误类型

| 错误 | 说明 | 常见原因 |
|------|------|----------|
| `ValueError` | 值错误 | `int("abc")` |
| `TypeError` | 类型错误 | `"2" + 3` |
| `ZeroDivisionError` | 除以零 | `10 / 0` |
| `IndexError` | 索引越界 | `[1,2][5]` |
| `KeyError` | 键不存在 | `dict["xxx"]` |
| `FileNotFoundError` | 文件不存在 | `open("不存在.txt")` |
| `NameError` | 变量未定义 | 使用未定义的变量 |
| `AttributeError` | 属性不存在 | 调用不存在的方法 |

```python
# 基本用法
try:
    num = int(input("输入一个数字："))
    print(f"你输入了: {num}")
except ValueError:
    print("输入的不是有效数字！")

# 捕获多种错误
try:
    x = int(input("输入被除数："))
    y = int(input("输入除数："))
    result = x / y
    print(f"结果：{result}")
except ValueError:
    print("请输入有效数字！")
except ZeroDivisionError:
    print("不能除以0！")

# 捕获所有错误
try:
    result = 10 / 0
except Exception as e:
    print(f"出错了：{e}")
    # 出错了：division by zero
```

### try/except/else/finally

```python
try:
    num = int(input("输入数字："))
except ValueError:
    print("不是数字！")
else:
    # 没有出错时执行
    print(f"数字是 {num}")
finally:
    # 无论是否出错都会执行
    print("程序结束")
```

### 完整示例：安全的用户输入

```python
def get_positive_integer(prompt):
    """安全地获取一个正整数"""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("请输入正整数！")
                continue
            return value
        except ValueError:
            print("输入无效，请输入数字！")

age = get_positive_integer("请输入年龄：")
print(f"你的年龄是 {age}")
```

---

## 21. 类与对象（入门）

类是创建对象的模板。就像"学生"是一个概念（类），"小明"是一个具体的学生（对象）。

### 基本语法

```python
class 类名:
    def __init__(self, 参数...):
        """初始化方法，创建对象时自动调用"""
        self.属性 = 值

    def 方法名(self, 参数...):
        """普通方法"""
        代码
```

- `self` 代表对象自己，每个方法的第一个参数必须是 `self`
- `__init__` 是初始化方法，创建对象时自动执行

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = []

    def add_score(self, score):
        """添加成绩"""
        self.scores.append(score)

    def get_average(self):
        """计算平均分"""
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def introduce(self):
        """自我介绍"""
        avg = self.get_average()
        print(f"我叫{self.name}，{self.age}岁，平均分{avg:.1f}")


# 创建对象
s1 = Student("小明", 18)
s1.add_score(90)
s1.add_score(85)
s1.add_score(92)
s1.introduce()
# 我叫小明，18岁，平均分89.0

s2 = Student("小红", 17)
s2.add_score(95)
s2.add_score(88)
s2.introduce()
# 我叫小红，17岁，平均分91.5
```

### 继承

子类可以继承父类的属性和方法，还可以添加自己的。

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}在叫")


class Dog(Animal):
    def speak(self):
        print(f"{self.name}: 汪汪汪！")

    def fetch(self):
        print(f"{self.name}去捡球了")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: 喵喵喵！")


# 使用
dog = Dog("旺财")
cat = Cat("小花")

dog.speak()   # 旺财: 汪汪汪！
dog.fetch()   # 旺财去捡球了
cat.speak()   # 小花: 喵喵喵！
```

### 完整示例：银行账户

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            print("存款金额必须大于0")
            return
        self.balance += amount
        print(f"存入 {amount} 元，余额 {self.balance} 元")

    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            print("取款金额必须大于0")
            return
        if amount > self.balance:
            print(f"余额不足！当前余额 {self.balance} 元")
            return
        self.balance -= amount
        print(f"取出 {amount} 元，余额 {self.balance} 元")

    def show_balance(self):
        """查询余额"""
        print(f"{self.owner}的账户余额：{self.balance} 元")


# 使用
account = BankAccount("小明", 1000)
account.show_balance()    # 小明的账户余额：1000 元
account.deposit(500)      # 存入 500 元，余额 1500 元
account.withdraw(200)     # 取出 200 元，余额 1300 元
account.withdraw(2000)    # 余额不足！当前余额 1300 元
```

---

## 22. 常用内置函数速查

Python自带的函数，不需要 import。

### 数学类

| 函数 | 说明 | 例子 |
|------|------|------|
| `abs(x)` | 绝对值 | `abs(-5)` → `5` |
| `max(...)` | 最大值 | `max(1, 5, 3)` → `5` |
| `min(...)` | 最小值 | `min(1, 5, 3)` → `1` |
| `sum(iterable)` | 求和 | `sum([1, 2, 3])` → `6` |
| `round(x, n)` | 四舍五入到 n 位 | `round(3.14159, 2)` → `3.14` |
| `pow(x, y)` | x 的 y 次方 | `pow(2, 3)` → `8` |
| `divmod(a, b)` | 同时求商和余数 | `divmod(7, 3)` → `(2, 1)` |

```python
numbers = [4, 2, 7, 1, 9, 3]
print(max(numbers))     # 9
print(min(numbers))     # 1
print(sum(numbers))     # 26
print(round(3.14159, 2))  # 3.14
print(abs(-42))         # 42
```

### 类型判断

| 函数 | 说明 | 例子 |
|------|------|------|
| `type(x)` | 获取类型 | `type(42)` → `<class 'int'>` |
| `isinstance(x, type)` | 判断类型 | `isinstance(42, int)` → `True` |

```python
print(isinstance(42, int))       # True
print(isinstance("hi", str))     # True
print(isinstance([1,2], list))   # True
print(isinstance(3.14, (int, float)))  # True（多个类型用元组）
```

### 序列操作

| 函数 | 说明 | 例子 |
|------|------|------|
| `len(x)` | 长度 | `len([1,2,3])` → `3` |
| `range(n)` | 生成数字序列 | 见第8节 |
| `enumerate(seq)` | 带索引遍历 | 见第8节 |
| `sorted(seq)` | 排序（返回新列表）| `sorted([3,1,2])` → `[1,2,3]` |
| `reversed(seq)` | 反转迭代器 | `list(reversed([1,2,3]))` → `[3,2,1]` |
| `zip(a, b)` | 配对组合 | 见下方 |

```python
# zip：把两个列表配对
names = ["小明", "小红", "小刚"]
scores = [90, 85, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}分")
# 小明: 90分
# 小红: 85分
# 小刚: 78分

# sorted 排序
words = ["banana", "apple", "cherry"]
print(sorted(words))                     # 按字母排序
print(sorted(words, key=len))            # 按长度排序
print(sorted(words, reverse=True))       # 降序

# 对字典列表排序
students = [
    {"name": "小明", "score": 92},
    {"name": "小红", "score": 88},
    {"name": "小刚", "score": 95},
]
result = sorted(students, key=lambda s: s["score"], reverse=True)
for s in result:
    print(f"{s['name']}: {s['score']}")
# 小刚: 95
# 小明: 92
# 小红: 88
```

### 输入输出

| 函数 | 说明 |
|------|------|
| `print(...)` | 输出 |
| `input(提示)` | 输入 |
| `open(文件, 模式)` | 打开文件 |

### 其他常用

| 函数 | 说明 | 例子 |
|------|------|------|
| `id(x)` | 对象的内存地址 | `id(42)` |
| `help(x)` | 查看帮助文档 | `help(print)` |
| `dir(x)` | 查看对象的所有属性和方法 | `dir("")` |

```python
# help 查看函数用法
# help(print)

# dir 查看字符串有哪些方法
methods = dir("")
# 过滤出不以_开头的方法（公开方法）
public_methods = [m for m in methods if not m.startswith("_")]
print(public_methods)
```

---

## 附录：练习题

学完以上内容，试试以下练习来巩固知识。

### 练习 1：温度转换器

编写程序，将摄氏度转为华氏度（公式：F = C × 9/5 + 32）。

```python
# 参考答案
celsius = float(input("请输入摄氏温度："))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

### 练习 2：判断闰年

编写函数判断一个年份是否为闰年。
规则：能被4整除但不能被100整除，或者能被400整除。

```python
# 参考答案
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("请输入年份："))
if is_leap_year(year):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")
```

### 练习 3：列表去重排序

将列表中的重复元素去除，并按从大到小排序。

```python
# 参考答案
numbers = [5, 3, 8, 1, 3, 5, 8, 2, 9, 1]
unique_sorted = sorted(set(numbers), reverse=True)
print(unique_sorted)
# [9, 8, 5, 3, 2, 1]
```

### 练习 4：统计字符串

统计一个句子中每个字母出现的次数（不区分大小写，忽略空格和标点）。

```python
# 参考答案
text = "Hello World, Hello Python!"
text = text.lower()

char_count = {}
for char in text:
    if char.isalpha():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

for char, count in sorted(char_count.items()):
    print(f"'{char}': {count}次")
```

### 练习 5：简易通讯录

用字典存储联系人（姓名→电话），实现增删查功能。

```python
# 参考答案
contacts = {}

while True:
    print("\n=== 通讯录 ===")
    print("1. 添加联系人")
    print("2. 查找联系人")
    print("3. 删除联系人")
    print("4. 显示所有")
    print("5. 退出")

    choice = input("请选择操作：")

    if choice == "1":
        name = input("姓名：")
        phone = input("电话：")
        contacts[name] = phone
        print(f"已添加 {name}")

    elif choice == "2":
        name = input("查找姓名：")
        phone = contacts.get(name)
        if phone:
            print(f"{name}: {phone}")
        else:
            print("未找到该联系人")

    elif choice == "3":
        name = input("删除姓名：")
        if name in contacts:
            del contacts[name]
            print(f"已删除 {name}")
        else:
            print("未找到该联系人")

    elif choice == "4":
        if contacts:
            for name, phone in contacts.items():
                print(f"  {name}: {phone}")
        else:
            print("通讯录为空")

    elif choice == "5":
        print("再见！")
        break

    else:
        print("无效选择，请重试")
```

---

## 速查表：Python 关键字

| 关键字 | 用途 | 关键字 | 用途 |
|--------|------|--------|------|
| `if` | 条件判断 | `elif` | 否则如果 |
| `else` | 否则 | `for` | 循环 |
| `while` | 条件循环 | `break` | 跳出循环 |
| `continue` | 跳过本次 | `def` | 定义函数 |
| `return` | 返回值 | `class` | 定义类 |
| `import` | 导入模块 | `from` | 从...导入 |
| `as` | 别名 | `try` | 尝试 |
| `except` | 捕获异常 | `finally` | 最终执行 |
| `raise` | 抛出异常 | `with` | 上下文管理 |
| `pass` | 占位符（什么都不做）| `None` | 空值 |
| `True` | 真 | `False` | 假 |
| `and` | 且 | `or` | 或 |
| `not` | 非 | `in` | 属于 |
| `is` | 是（同一对象）| `del` | 删除 |
| `global` | 全局变量 | `lambda` | 匿名函数 |

---

> 学完这份指南，你已经掌握了 Python 最核心的语法！
> 接下来可以开始学习 Pygame 来制作游戏了 🎮
