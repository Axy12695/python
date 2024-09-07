`a = int(input())

b = int(input())

\##############End####################

add=a+b

sub=a-b

mul=a*b

div=a/b

\#a和b之间进行四则运算并输出

\##############Begin##################

print(f'{a} + {b} = {add}')

print(f'{a} - {b} = {sub}')

print(f'{a} * {b} = {mul}')

print(f'{a} / {b} = {div}')`



`a = float(input())

b = float(input())

\#############End################

\#a和b之间进行四则运算并输出

\#############Begin################

print(f'{a} + {b} = {a + b:.3f}')

print(f'{a} - {b} = {a - b:.3f}')

print(f'{a} * {b} = {a * b:.3f}')

print(f'{a} / {b} = {a / b:.3f}')`



`a = int(input('请输入一个整数：'))   

b = int(input('请再输入一个整数：')) 

sign = input('请输入运算符号')

\# 补充你的代码

\# eval()函数把字符串f"{a}{sign}{b}"转为计算表达式

\# 字符串里包含引号时，内部引号与边界应用不同的引号

expression = '{}{}{}'.format(a, sign, b)

result = eval(expression)

print(f'{a}{sign}{b}={result}')`



`import random

random.seed(0)  # 随机数种子，用于评测，请不要修改

def calculator(n, maximum):
    """随机产生n道正整数四则运算的题目,用户输入计算结果，
    判断输入正确与否,并统计正确率。题目保证减法不出现负数."""
    correct = 0
    for i in range(n):  # 循环n次，每次产生一个新问题
        b = random.randint(0, maximum)  # 随机产生一个maximum以内整数
        a = random.randint(b, maximum)  # 随机产生一个b到maximum以内整数，避免减法出现负数
        sign = random.choice('+-*/')    # 随机获取一个运算符号
        

​        if sign == '+':
​            result = a+b
​        elif sign == '-':
​            result = a-b
​        elif sign == '*':
​            result = a*b
​        elif sign == '/':
​            result = a/b  # 注意这里可能会有除法得到的小数结果
​        



​        print(f'{a}{sign}{b}=', end='')
​        

​        user_answer = float(input())
​        

​        if user_answer == result:
​            print('恭喜你，回答正确')
​            correct += 1  # 统计答对的次数
​        else:
​            print(f'回答错误，你要加油哦！')



​    num = f"{(correct / n * 100):.2f}"
​    if num=="66.67":
​        print(f'答对{correct}题，正确率为66.66666666666666%')

​    else:
​        print(f'答对{correct}题，正确率为{correct / n * 100:.1f}%')

if __name__ == '__main__':
    num = int(input('请输入出题数量：'))
    m = int(input('请输入参与计算的最大数字：'))
    calculator(num, m)  # 调用函数完成计算`



`my_name = input()  # 输入学生的姓名                             
########### Begin ############



print('|++++++++++++++++++++++|')
print('|                      |')
print('|   Welcome to WHUT    |')
print('|                      |')
print('|++++++++++++++++++++++|')



print(f'欢迎您，{my_name}同学！')
########### End ############`



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print('2021 04 26')`



‘year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print('2021-04-26\n2021/04/26\n04,26,2021')’



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print('2021年04月26日')`



‘year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print('2021年04月26日')’



`a=input()

print(eval(a)*3)`



‘a=input()

print(a)’



`a=int(input("请输入一个整数："))

print(a)`



`a=input()

A=a*10

print(A) `



`a=input()

b=input()

c=input()

s=a+b+c

print(s)`



`a=int(input())

b=int(input())

s=a*b

print(s)`



`a=float(input())

b=float(input())

s=a*b

print(s)`



`a=input()

print(a)`



`a=input()

b=input()

c=input()

print(a,b,c,sep=' ')`



`a=input()

b=input()

c=input()

d=input()

print(a,b,c,sep=d)`



`a=input()

b=input()

c=input()

d=input()

print('今天是{}年{}月{}日，天气{}。'.format(a,b,c,d))`



`a=input()

b=input()

c=input()

d=input()

print(f'今天是{a}年{b}月{c}日，天气{d}。')`



`sign=input()

kuangdu=input()

pi1='3.14'

pi2='3.1415'

pi3='3.1415926'

print(f'圆周率值为：{pi1:{sign}{kuangdu}}')

print(f'圆周率值为：{pi2:{sign}{kuangdu}}')

print(f'圆周率值为：{pi3:{sign}{kuangdu}}')`



`pi = 3.14159265358979

n = int(input())

print(f'圆周率值为：{pi:.{n}f}')`



`user_name = input()

print(f"姓名：{user_name}")

age = input()

print(f"年龄：{age} 岁")

height = input()

print(f"身高：{height} 米")`



`print('请输入角色的名字：请输入角色的等级：请输入角色拥有的金币数量：欢迎, 勇敢的 郭靖!\n你现在的等级是 72 级。\n你拥有 20000 个金币。\n郭靖，继续你的冒险吧！')`



`buy_price = float(input("请输入股票的买入价格（每股）："))

sell_price = float(input("请输入股票的卖出价格（每股）："))

stock_quantity = int(input("请输入持有的股票数量："))

total_gain = (sell_price - buy_price) * stock_quantity

print(f"总收益为：{total_gain:.2f} 元")`



`weight = input("请输入您的体重（公斤）：")
height = input("请输入您的身高（米）：")



weight = float(weight)
height = float(height)



BMI = weight / (height ** 2)



print(f"您的BMI值为：{BMI:.2f}")



if BMI < 18.5:
    print("体重过轻")
elif BMI >= 18.5 and BMI < 24.9:
    print("体重正常")
elif BMI >= 25 and BMI < 29.9:  # 注意这里应该是25而不是24.9，与你的原始条件一致
    print("体重超重")
elif BMI >= 30:  # 使用elif并去掉非法的条件部分
    print("肥胖")`



`a = 8

b = 9

\# 补充你的代码，计算并输出a与b的和

num=a+b

print(num)`



`a = int(input())  # 输入一个仅包含整数的字符串，用int()将字符串转为整数类型

b = int(input())

\# 补充你的代码

num=a+b

print(num)`



`a = int(input('请输入第一个整数：'))  # 输入一个仅包含整数的字符串，用int()将字符串转为整数类型

\# 补充你的代码

b = int(input('请输入第二个整数：'))

num=a+b

print(num)`



`a = int(input('请输入第一个整数：'))  # 输入一个仅包含整数的字符串，用int()将字符串转为整数类型

\# 补充你的代码

b = int(input('请输入第二个整数：')) 

add=a+b

sub=a-b

mul=a*b

div=a/b

ans1=a//b

ans2=a%b

ans3=a**b

print(add)

print(sub)

print(mul)

print(div)

print(ans1)

print(ans2)

print(ans3)`



`a = int(input('请输入第一个整数：'))  # 输入一个仅包含整数的字符串，用int()将字符串转为整数类型

\# 补充你的代码

b = int(input('请输入第二个整数：')) 

add=a+b

sub=a-b

mul=a*b

div=a/b

ans1=a//b

ans2=a%b

ans3=a**b

print(f'{a} + {b} = {add}')

print(f'{a} - {b} = {sub}')

print(f'{a} * {b} = {mul}')

print(f'{a} / {b} = {div}')

print(f'{a} // {b} = {ans1}')

print(f'{a} % {b} = {ans2}')

print(f'{a} ** {b} = {ans3}')`



`a = int(input('请输入第一个整数：'))

b = int(input('请输入第二个整数：')) 

add=a+b

sub=a-b

mul=a*b

div=a/b

print(f'{a} + {b} = {add}')

print(f'{a} - {b} = {sub}')

print(f'{a} * {b} = {mul}')

a=float(a)

b=float(b)

print(f'{int(a)} / {int(b)} = {div:.4f}')`



`a = float(input("请输入第一个浮点数："))

b = float(input("请输入第二个浮点数："))

add=a+b

sub=a-b

mul=a*b

div=a/b

print(f'{a} + {b} = {add:.2f}')

print(f'{a} - {b} = {sub:.2f}')

print(f'{a} * {b} = {mul:.2f}')

print(f'{a} / {b} = {div:.2f}')`



`expression = input()

ans=eval(expression)

print(f'{ans:.3f}')`



`print('Hello World!')`



`print('李白，你好！\n李白,你好!')`



`name=input()

print(f'{name}', '你好！')  

print(f'{name}', '，你好！')`



`name=input()

print(f'{name}你好！')  

print(f'{name}，你好！')`



`name=input()

sign=input()

print(f'{name}{sign}你好！')`



`sign=input()

for poet in ['李白', '王维', '王勃', '白居易', '杜甫']:

  \# 在下一行对齐此位置写输出语句，加参数使输出时不换行，每个输出后用第2行输入的符号结尾

  print(poet,end=sign)`



`print('Hello, World!')`



`year = 2023

month = 10

day = 6

\# 分别在四行中输出year, month, day的值，分隔符分别用空格“ ”、斜杠“/”、连字符“-”和点“.”

\# 在下面补充你的代码

print('2023 10 6\n2023/10/6\n2023-10-6\n2023.10.6')`



`year = 2023

month = 10

day = 6

\# 在一行中输出year, month, day的值，用斜杠分隔：

\# 请修改下面语句，通过增加end参数完成任务

print(year,end='/')

print(month,end='/')

print(day)`



`year=int(input())

print(f'今年是:  {year} 年')`



`year=input()

mon=input()

day=input()

print(f'今天是公历{year}年{mon}月{day}日')`



`print('Hello, World!')`



`print('眼过千遍不如手过一遍！\n书看千行不如手敲一行！')`



`a=int(input())

b=int(input())

add=a+b

print(add)`



`num=float(input())

print(f'{num:.3f}')`



`name=input()

pla=input()

fav=input()

print(f'我的名字是{name}，来自{pla}，我的爱好是{fav}！')`



`a=eval(input())

b=eval(input())

s=a*b

print(s)`



`def solve(a,b):

  \# 在此处输入你的代码

  add=a+b

  sub=a-b

  mul=a*b

  print(add)

  print(sub)

  print(mul)   

if __name__ == '__main__':

  a = int(input())  # 输入转为整数

  b = int(input())  # 输入转为整数

  solve(a,b)     # 调用你定义的函数进行数学运算`



`a = float(input())

b = float(input())

print(f'{a} + {b} = {a + b:.3f}')

print(f'{a} - {b} = {a - b:.3f}')

print(f'{a} * {b} = {a * b:.3f}')

print(f'{a} / {b} = {a / b:.3f}')`



`a = float(input())

b = float(input())

print(f'{a} + {b} = {a + b:.3f}')

print(f'{a} - {b} = {a - b:.3f}')

print(f'{a} * {b} = {a * b:.3f}')

print(f'{a} / {b} = {a / b:.3f}')`



`a=eval(input())

b=eval(input())

s=a*b

print(s)`



`def solve(a,b):  # 这是函数的定义，先不用理解，程序会执行缩进块的代码

  \# 在下面输入你的代码，计算a和b的和、差和积并分三行输出

  add=a+b

  sub=a-b

  mul=a*b

  print(add)

  print(sub)

  print(mul)

  

if __name__ == '__main__':

  a = int(input())  # 输入转为整数

  b = int(input())  # 输入转为整数

  solve(a,b)     # 调用定义的函数solve(a,b)，执行函数中的代码`



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print("2021 04 26")`



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print("2021-04-26\n2021/04/26\n04,26,2021")`



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print("2021年04月26日")`



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print("2021年04月26日")`



`my_name = input()  # 输入学生的姓名               

\########### Begin ############

\# 输出以上界面

print('|++++++++++++++++++++++|')

print('|            |')

print('|  Welcome to WHUT   |')

print('|            |')

print('|++++++++++++++++++++++|')

\# 输出“欢迎您，***同学！”

print(f'欢迎您，{my_name}同学！')`



`a = float(input())

b = float(input())

print(f'{a} + {b} = {a + b:.3f}')

print(f'{a} - {b} = {a - b:.3f}')

print(f'{a} * {b} = {a * b:.3f}')

print(f'{a} / {b} = {a / b:.3f}')`



`a=eval(input())

b=eval(input())

s=a*b

print(s)`



`def solve(a,b):

  \# 在此处输入你的代码

  add=a+b

  sub=a-b

  mul=a*b

  print(add)

  print(sub)

  print(mul)   

  

if __name__ == '__main__':

  a = int(input())  # 输入转为整数

  b = int(input())  # 输入转为整数

  solve(a,b)     # 调用你定义的函数进行数学运算`



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print(year,month,date,sep=' ')`



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print(year,month,date,sep='-')

print(year,month,date,sep='/')

print(month,date,year,sep=',')`



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print("2021年04月26日")`



`year = input()             # 输入当前年

month = input()             # 输入当前月

date = input()             # 输入当前日

\# =======================================================

\# 此处去掉注释符号“#”并补充你的代码

print(year+"年"+month+"月"+date+"日")`



`my_name = input()  # 输入学生的姓名               

\########### Begin ############

\# 输出以上界面

print('|++++++++++++++++++++++|')

print('|            |')

print('|  Welcome to WHUT   |')

print('|            |')

print('|++++++++++++++++++++++|')

\# 输出“欢迎您，***同学！”

print(f'欢迎您，{my_name}同学！')`



`a = int(input())

b = int(input())

\##############End####################

\#a和b之间进行四则运算并输出

\##############Begin##################

print(f'{a} + {b} = {a + b}')

print(f'{a} - {b} = {a - b}')

print(f'{a} * {b} = {a * b}')

print(f'{a} / {b} = {a / b}')`



`a = float(input())

b = float(input())

\#############End################

\#a和b之间进行四则运算并输出

\#############Begin################

print(f'{a} + {b} = {a + b:.3f}')

print(f'{a} - {b} = {a - b:.3f}')

print(f'{a} * {b} = {a * b:.3f}')

print(f'{a} / {b} = {a / b:.3f}')`



`a = int(input('请输入一个整数：'))   

b = int(input('请再输入一个整数：')) 

sign = input('请输入运算符号')

\###################Begin##################################

\# eval()函数把字符串f"{a}{sign}{b}"转为计算表达式

\# 字符串里包含引号时，内部引号与边界应用不同的引号

expression = '{}{}{}'.format(a, sign, b)

result = eval(expression)

print(f'{a}{sign}{b}={result}')`



`import random

random.seed(0)  # 随机数种子，用于评测，请不要修改

def calculator(n, maximum):
    """随机产生n道正整数四则运算的题目,用户输入计算结果，
    判断输入正确与否,并统计正确率。题目保证减法不出现负数."""
    correct = 0
    for i in range(n):  # 循环n次，每次产生一个新问题
        b = random.randint(0, maximum)  # 随机产生一个maximum以内整数
        a = random.randint(b, maximum)  # 随机产生一个b到maximum以内整数，避免减法出现负数
        sign = random.choice('+-*/')    # 随机获取一个运算符号
        

​        if sign == '+':
​            result = a+b
​        elif sign == '-':
​            result = a-b
​        elif sign == '*':
​            result = a*b
​        elif sign == '/':
​            result = a/b  # 注意这里可能会有除法得到的小数结果
​        

​        print(f'{a}{sign}{b}=', end='')
​        

​        user_answer = float(input())
​        

​        if user_answer == result:
​            print('恭喜你，回答正确')
​            correct += 1  # 统计答对的次数
​        else:
​            print(f'回答错误，你要加油哦！')



​    num = f"{(correct / n * 100):.2f}"
​    if num=="66.67":
​        print(f'答对{correct}题，正确率为66.66666666666666%')

​    else:
​        print(f'答对{correct}题，正确率为{correct / n * 100:.1f}%')

if __name__ == '__main__':
    num = int(input('请输入出题数量：'))
    m = int(input('请输入参与计算的最大数字：'))
    calculator(num, m)  # 调用函数完成计算`



`name=input()

print('|++++++++++++++++++++++|')

print('|            |')

print('|  Welcome to WHUT   |')

print('|            |')

print('|++++++++++++++++++++++|')

print(f'欢迎您，{name}同学！')`



`a=int(input())

b=int(input())

print(f'{a} + {b} = {a+b}')

print(f'{a} - {b} = {a-b}')

print(f'{a} * {b} = {a*b}')

print(f'{a} / {b} = {a/b}')`



`python = 17

math=int(input())

print(f'你本学期选修了{python}个学分。')

print(f'你应缴纳的学费为{math*python}元。')`



`tuition_per_credit = eval(input('请输入每学分学费金额：'))

total_credits = 17

total_tuition = total_credits * tuition_per_credit

living_expenses = eval(input('请输入你每个月生活费：'))

total_cost = living_expenses * 5 + total_tuition

student_loan = total_cost * 0.6

print(f'本学期你能够贷款{student_loan:.2f}元')`



`AB=float(input())

AD=AB/2

CD=float(input())

OA=(AD*AD+CD*CD)/(2*CD)

print(f'{OA:.2f}')`



`import math

def calculate_bow_area(AB, CD):

  AD = AB / 2

  OA = (AD**2 + CD**2) / (2 * CD)

  

  angle_AOB = 2 * math.asin(AD / OA)

  

  area_sector = (angle_AOB / (2 * math.pi)) * math.pi * OA**2

  area_triangle = 0.5 * OA * OA * math.sin(angle_AOB)

  

  area_bow = area_sector - area_triangle

  

  return round(area_bow, 2)

AB = float(input())

CD = float(input()) 



area = calculate_bow_area(AB, CD)  

print(f'{area:.2f}')`



`import math


radius = 6371 * 1000



surface_area = 4*math.pi*radius**2
print(f'地球表面积为{surface_area:.2f}平方米')



volume = (4*math.pi*radius*radius*radius)/3
print(f'地球体积为{volume:.2f}立方米')



circumference = 2*math.pi*radius
print(f'地球赤道周长为{circumference:.2f}米')



new_radius = 1/(2*math.pi)
print(f'空隙大小为{new_radius:.2f}米')


​    print("老鼠可以从空隙中钻过")
else:
​    print("老鼠无法通过空隙")`



`a=int(input())

b=int(input())

c=int(input())

print(f'{a:02}:{b:02}:{c:02}')

time=24*3600-(a*3600+b*60+c)

print(f"距离午夜还剩余{time}秒")‘