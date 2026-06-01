# 王弘森-25361149-第二次人工智能编程作业
仓库链接: https://github.com/RegularSugar/homework2-stu_info_manage_system.git
## 1. 任务拆解与 AI 协作策略
&emsp;&emsp;我将整个 “学生信息与考场管理系统” 的开发任务，按照功能模块和实现顺序拆解为 4 个步骤，逐步和 AI 协作完成:<br>
步骤 1：分析需求，考虑文件划分<br>
&emsp;&emsp;因为系统需求多，首先考虑怎么组织功能，自己思考加咨询AI，创建了Student()和ExamSys()类来分别存放学生基本信息和系统功能。<br>
&emsp;&emsp;同时，因为需要将功能分布在三个不同的文件中，先咨询了AI怎么合理分划比较合理<br>
步骤 2：模块化要求开发<br>
&emsp;&emsp;按照不同功能一项一项开发，每完成一步就提交上传一次。完成功能时，先自己想清楚大致思路，然后让AI按照要求写出核心代码，人工审查修缮后采用。<br>
步骤 3：debug<br>
&emsp;&emsp;出现问题后，观察报错行与报错内容，自己解决。不能解决，则将报错情况和代码一并发给AI寻求帮助。<br>
步骤 4：细节优化与规范修正<br>
&emsp;&emsp;针对代码细节和规范性问题，向AI寻求修改建议。<br>
## 2. 核心 Prompt 迭代记录
初代prompt： 我需要一段功能代码,实现：“在ExamSys类的__init__()方法中调用该功能函数，从“人工智能编程语言学生名单.txt”文件中读取学生信息”<br>
产生的问题： 代码格式与“人工智能编程语言学生名单.txt”不匹配<br>
优化后的prompt： 在之前的基础上，发送“人工智能编程语言学生名单.txt”以匹配格式<br>
## 3. Debug 与异常处理记录
&emsp;&emsp;出现FileNotFoundError，应该是没找到文件的原因，咨询AI后，发现是read直接写的是“人工智能编程语言学生名单.txt”，并不是一个完整路径，
同时没有把“人工智能编程语言学生名单.txt”放到与system.py同一文件夹里。考虑到兼容性，如果写一个具体路径，更换设备后仍会出现路径错误，所以把txt文件直接放到了同一个文件夹里，而不修改代码中的路径
## 4. 人工代码审查 (Code Review)
```python
    #打印准考证号
    def generate_admission_tickets(self): 
        os.makedirs("准考证", exist_ok=True) #考虑到可能准考证文件夹已经存在，exist_ok=True可以跳过生成文件夹避免报错。
                                            #同时，由于后面使用open()，无则新建有则打开，使用write()可以覆写
        shuffled = random.sample(self.students, len(self.students)) #为了不改变原始数据，不直接使用shuffle而是用sample()随机无序选n个人
        i = 0 #朴素计数器，用来生成序号
        for stu in shuffled:
            i += 1
            file_name = f"准考证/{i:0>2d}.txt" #此文件名可以下面的open()中实现：在“准考证”问价夹里生成或打开（若已存在）指定格式文件名的文件
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(f"考场座位号:{i}\n")     #写入指定格式的内容
                f.write(f"姓名:{stu.name}\n")
                f.write(f"学号:{stu.id}\n")
                
        print("已生成\"准考证\'文件夹及所有准考证文件\n") #提供合适的人机交互反馈
