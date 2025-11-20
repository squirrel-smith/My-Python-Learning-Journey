def system_log():
    '''
    功能说明：打开程序界面
    '''
    print("===python电子教室登陆系统===")
    #先建立一个空列表，方便处理里面的数据
    user_acc = []
    #以下功能均建立在开启登陆系统的基础上，因此均需要缩进到与function body同一级别
    #由于这个程序是要用户无限尝试，只在希望退出时退出，因此用while true构建一个无限循环的框架
    while True:
        #显示主界面信息
        print("==登陆(1)==\n==注册(2)==\n==退出(3)==")
        ch1=input("请输入数字执行对应功能")
        #设置初始布尔值，防止其使用时没有被赋值
        in1 = False
        if ch1 == "1":
            print("==登陆==\n按q键返回上一界面")
            #同样是无限循环按键退出，while true
            while True:
                #用户输入信息
                a1=input("请输入账号")
                #之前将其防止下面的elif中，不知为何无法生效，只能将其单独提出进行判断
                if a1 == "q" :
                   break
                a2=input("请输入密码")
                if a2 == "q" :
                   break
                #同样是后续要用的布尔值，我一般都是先用再找个地方放初始值
                in2 = False
                #验证登陆的账号密码是否已经被注册存储在列表中
                for u2 in user_acc:
                    if a1 == u2['ub1'] and a2 == u2['ub2']:
                        print("登陆成功！\n"+a1+"欢迎回来！")
                        #前面两个布尔值，作为登陆状态存在，如果成功则用于后续的退出while true循环的条件
                        in1 = True
                        in2 = True
                        break
                #用布尔值直接判断是否退出循环
                if in2:
                    break
                if not in2:
                    print("账号或密码有误，请重新输入")
        #由于用了两个while true，这里是第二个布尔值用来退出第一个循环
        elif in1:
            break
        #注册选项
        elif ch1 == "2":
            print("==注册==\n按q键返回上一界面")
            #同样无限循环按键退出
            while True:
                #用来判断输入的账号是否符合要求，以下是if else反复循环，因为不同的错误给出的提示不同
                b1=input("请输入您的电子邮箱")
                #查询得知.split的作用，判断前缀是否符合要求，后缀要求固定所以直接寻找即可
                fen = b1.split("@")
                emn = fen[0]
                #判断后缀
                em="@email.szu.edu.cn"
                #后面要用到的布尔值
                rb = False
                rb2 = False
                #和前面一样的思路，提前简单判断来决定是否返回
                if b1 == "q":
                    break
                #循环套循环判断是否符合要求，但是elif和else混用感觉怪怪的
                if em in b1:
                    if len(emn) < 4 or len(emn) > 18:
                        print("账号格式错误")
                        #返回上一个外循环的开始
                        continue
                    elif not emn.isdigit():
                        print("账号格式错误")
                        continue
                    #检查账号是否重复，避免字典由于键重复报错，把列表中的字典的键依次提取出来形成新的临时列表
                    elif b1 in [u1['ub1'] for u1 in user_acc]:
                        print("账号已存在")
                        continue
                    else:
                        print("账号输入成功")
                        rb = True
                else:
                    print("账号格式错误")
                    continue
                #无限循环按键退出，第二个while true，对应第二个布尔值
                while True:
                    b2 = input("请输入您的密码\n按q键返回上一界面")
                    if b2 == "q":
                        break
                    if len(b2) < 8 or len(b2) > 16:
                        print("密码长度需要在8-16之间")
                    else:
                        # 设置初始布尔值，在后面的for循环直接解决，但是数字一开始我忘加了，空格一开始没想到用这种方法，所以很乱
                        da = False
                        xi = False
                        nu = False
                        # 使用for循环检查b1中是否有大小写字母、数字
                        for i2 in b2:
                            #以下isupper、islower、isdigit都是查询得知
                            if i2.isupper():
                                da = True
                            if i2.islower():
                                xi = True
                            if i2.isdigit():
                                nu = True
                        if not da or not xi or not nu:
                            print("密码至少存在一个大写字母、小写字母和数字")
                        else:
                            # 判断b1是否存在空格，写得比较早，因此没有和前面的一起for循环检查
                            kong = ' ' in b2
                            if kong:
                                print("密码中不得包含空格")
                            else:
                                print("密码设置成功")
                                #这个没有用布尔值，直接用break退出了，因为这是最后一个判断
                                while True:
                                    bb2 = input("请再次输入密码以确认\n按q返回上一界面")
                                    if bb2 == 'q':
                                        print("重新设置密码，返回密码输入界面")
                                        break
                                    elif bb2 == b2:
                                        rb2 = True
                                        print("密码设置成功，注册完成")
                                        #在列表中加入字典，虽然那个时候还没学字典
                                        user_acc.append({
                                            'ub1': b1,
                                            'ub2': b2
                                        })
                                        #直接退出
                                        break
                                    else:
                                        print("密码确认失败，请重新输入")
                                        continue
                                if bb2 == 'q':
                                    continue
                    if rb2:
                        break
                #布尔值判断，退出循环
                if rb and rb2:
                    break
        #直接退出程序
        elif ch1 == "3":
            break
        #防止输入其他内容
        else :
            print("无效命令，请重新尝试")



system_log