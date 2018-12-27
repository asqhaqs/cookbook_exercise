# -*- coding:utf-

# 让python2 使用中文编码


'''
 第 22 条：使用辅助类来维护程序的状态，而非使用字典和数组
'''

# 使用字典来存储学生的成绩


class SimpleGradebook(object):

    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades)/len(grades)


book = SimpleGradebook()
book.add_student('xudong')
book.report_grade('xudong', 61)
book.report_grade('xudong', 72)
book.report_grade('xudong', 99)

print(book.average_grade('xudong'))

# 当需求改变时，例如需要记录学生每次考试的科目成绩以及该成绩对应的权重时，应该将[] 改为 字典{}
# ,并且字典 值为 元组 （成绩， 权重）这样比较麻烦，可以使用类来代替， 避免数据结构过于复杂
# 这里使用 collection中的 namedtuple

import collections

# 定义成绩类的格式
Grade = collections.namedtuple('Grade', ('score', 'weight'))

# 定义表示科目的类，包含一系列的考试成绩
class Subject(object):

    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total/total_weight

# 编写学生类，该类中包含此学生正在学习的各项课程
class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total/count

class GradeBook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


book = GradeBook()
xudong = book.student("xudong")
math = xudong.subject('math')
math.report_grade(80, 0.8)
english = xudong.subject('english')
english.report_grade(90, 0.2)
print(xudong.average_grade())

