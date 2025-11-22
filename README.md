# My-Python-Learning-Journey

##项目简介
该项目展现了我的 Python 学习之旅，这个仓库记录了我学习 Python 编程过程中的成长足迹。
我会在这里保存学习过程中编写的比较满意的代码，从基础语法到小型项目，以便随时回顾。

##项目特点
-**学习导向**：以基础知识和核心概念为主
-**Python语言**：所记录的均为Python语言的代码
-**循循渐进**：代码从简单到复杂，展现学习路径

##当前所记录代码及说明

###python电子教室登陆系统
一个简单的学生登录和注册的界面

####功能介绍

#####操作主界面
提供给用户“注册”、“登陆”、“退出”等选择
```
print("===python电子教室登陆系统===")
    user_acc = []
    while True:
        print("==登陆(1)==\n==注册(2)==\n==退出(3)==")
        ch1=input("请输入数字执行对应功能")
```

#####注册账户
使用规定邮箱进行注册
```
        elif ch1 == "2":
            print("==注册==\n按q键返回上一界面")
            while True:
                b1=input("请输入您的电子邮箱")
                fen = b1.split("@")
                emn = fen[0]
                em="@email.szu.edu.cn"
                rb = False
                rb2 = False
                if b1 == "q":
                    break
                if em in b1:
                    if len(emn) < 4 or len(emn) > 18:
                        print("账号格式错误")
                        continue
                    elif not emn.isdigit():
                        print("账号格式错误")
                        continue
                    elif b1 in [u1['ub1'] for u1 in user_acc]:
                        print("账号已存在")
                        continue
                    else:
                        print("账号输入成功")
                        rb = True
                else:
                    print("账号格式错误")
                    continue
                while True:
                    b2 = input("请输入您的密码\n按q键返回上一界面")
                    if b2 == "q":
                        break
                    if len(b2) < 8 or len(b2) > 16:
                        print("密码长度需要在8-16之间")
                    else:
                        da = False
                        xi = False
                        nu = False
                        for i2 in b2:
                            if i2.isupper():
                                da = True
                            if i2.islower():
                                xi = True
                            if i2.isdigit():
                                nu = True
                        if not da or not xi or not nu:
                            print("密码至少存在一个大写字母、小写字母和数字")
                        else:
                            kong = ' ' in b2
                            if kong:
                                print("密码中不得包含空格")
                            else:
                                print("密码设置成功")
                                while True:
                                    bb2 = input("请再次输入密码以确认\n按q返回上一界面")
                                    if bb2 == 'q':
                                        print("重新设置密码，返回密码输入界面")
                                        break
                                    elif bb2 == b2:
                                        rb2 = True
                                        print("密码设置成功，注册完成")
                                        user_acc.append({
                                            'ub1': b1,
                                            'ub2': b2
                                        })
                                        break
                                    else:
                                        print("密码确认失败，请重新输入")
                                        continue
                                if bb2 == 'q':
                                    continue
                    if rb2:
                        break
                if rb and rb2:
                    break
```

#####登陆账户
验证已注册的账户进行登陆
```
        in1 = False
        if ch1 == "1":
            print("==登陆==\n按q键返回上一界面")
            while True:
                a1=input("请输入账号")
                if a1 == "q" :
                   break
                a2=input("请输入密码")
                if a2 == "q" :
                   break
                in2 = False
                for u2 in user_acc:
                    if a1 == u2['ub1'] and a2 == u2['ub2']:
                        print("登陆成功！\n"+a1+"欢迎回来！")
                        in1 = True
                        in2 = True
                        break
                if in2:
                    break
                if not in2:
                    print("账号或密码有误，请重新输入")
        elif in1:
            break
```

#####退出程序
```
        elif ch1 == "3":
            break
        else :
            print("无效命令，请重新尝试")
```

####运行方法
1. 确保已安装 Python 3.6 或更高版本
2. 下载 `student_login_system.py` 文件
3. 在命令行中运行：
```
   bash
   python student_login_system.py
```

##学习心得与规划

###11月20日

####心得
即使是命令行程序，也需要考虑操作便利性和提示清晰度，GitHub上其他Python公开项目就让人一目了然
此外，变量命名和注释也需要尽可能让人能够清楚理解，这样才能使代码更易于理解和维护
在将自己的代码放置在GitHub的仓库里并编写readme，让我感到了一种更加专业、正式的感觉，在这个过程中，我感到对代码的应用属性有了
更深刻的理解，不只是理论书面上的编写，而是要拿来实际使用的工具，通过浏览其他公开项目，我感觉有了更多的学习热情。

####规划
目前我想要借助GitHub这一平台记录自己写的各种代码，并尝试去复刻社区里他人公开的代码用于学习
