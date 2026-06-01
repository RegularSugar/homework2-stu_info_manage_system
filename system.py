from student import Student
import random
import os

class ExamSys:
    def __init__(self):
        self.students = self.load_students()  # 构造函数先加载出学生信息的列表，进行学生信息初始化

    # 系统功能菜单运行控制
    def run(self):
        welcome_message = '===== 学生信息与考场管理系统 ===== \n 1. 查询学生信息\n 2. 随机点名\n 3. 生成考场安排表\n 4. 生成准考证文件\n+--------------------------------------------------------------------------\n 0. 退出系统\n 输入功能编号：'
        x = int(input(welcome_message))
        while x not in [1, 2, 3, 4, 0] :
            print("功能编号不存在，请正确输入功能编号（0~4）")
            x = int(input('重新输入功能编号：'))
        if x == 1:
            self.find_student()
        elif x == 2:
            self.random_roll_call()
        elif x == 3:
            self.generate_exam_arrangement()
        elif x == 4:
            self.generate_admission_tickets()
        return

    #学生信息初始化
    @staticmethod
    def load_students():
        students = []
        try:
            with open("人工智能编程语言学生名单.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                # 跳过第一行
                for line in lines[1:]:
                    line = line.strip()
                    if not line:
                        continue
                    # 按照 Tab 分割
                    parts = line.split("\t")
                    name = parts[1].strip()
                    gender = parts[2].strip()
                    clazz = parts[3].strip()
                    id1 = parts[4].strip()
                    department = parts[5].strip()
                    students.append(Student(name, gender, clazz, id1, department))
        except FileNotFoundError:
            print("未找到学生名单文件！")
        return students

    # 信息查找和定位(按学号查询)
    def find_student(self):
        stu_id = input("请输入学号：").strip()
        for stu in self.students:#按学号依次查找学生
            if stu.id == stu_id:
                print(f"找到学生：\n姓名   性别  班级   学号	    学院\n{stu.name}   {stu.gender}    {stu.clazz}     {stu.id}    {stu.department}  ")
                return
        print("未找到该学号对应的学生，请检查输入是否正确。")

    #随机点名
    def random_roll_call(self):
        try:
            n = int(input("请输入点名人数："))
            total = len(self.students)
            #数字问题的处理
            if n <= 0:
                print("错误：点名人数必须大于 0！")
                self.random_roll_call()
            elif n > total:
                print(f"错误：超过了总人数！")
                self.random_roll_call()
            #合法输入
            else:
                selected = random.sample(self.students, n)#按前面输入的人数随机抽人
                print("本次随机点名结果：")
                i = 0
                for stu in selected:
                    i += 1
                    print(f"{i}.{stu.name} {stu.id}")
        #处理非数字问题
        except ValueError:
            print("错误：请输入有效数字！")
            self.random_roll_call()

    #生成考场安排表
    def generate_exam_arrangement(self):
        shuffled = random.sample(self.students,len(self.students))#随机打乱安排座位
        with open("考场安排表.txt", "w", encoding="utf-8") as f:
            i = 0
            for stu in shuffled:
                i += 1
                f.write(f'{i},{stu.name},{stu.id}\n')
        print("成功生成考场安排表！")

    #打印准考证号
    def generate_admission_tickets(self):
        os.makedirs("准考证", exist_ok=True) #已存在文件夹则跳过
        shuffled = random.sample(self.students, len(self.students))
        i=0
        for stu in shuffled:
            i += 1
            file_name = f"准考证/{i:0>2d}.txt"
            with open(file_name, "w", encoding="utf-8") as f:#写入 或者覆写（如果已经存在）
                f.write(f"考场座位号:{i}\n")
                f.write(f"姓名:{stu.name}\n")
                f.write(f"学号:{stu.id}\n")

        print("已生成\"准考证\"文件夹及所有准考证文件\n")
