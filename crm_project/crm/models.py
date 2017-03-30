from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 课程班选择
course_type_choices = (('online', u'网络版'),
                       ('offline_weekend', u'面授班(周末班)'),
                       ('offline_fulltime', u'面授班(脱产)'),
                       )

'''
学校
'''


class School(models.Model):
    # 学校名字 唯一
    name = models.CharField(max_length=128, unique=True)
    # 所在城市
    city = models.CharField(max_length=64)
    # 学校地址
    addr = models.CharField(max_length=128)

    def __str__(self):
        return self.name


'''
用户表
'''


class UserProfile(models.Model):
    # 关联User 一对一
    user = models.OneToOneField(User)
    # 学生
    name = models.CharField(max_length=64)
    # 学校
    school = models.ForeignKey('School')

    def __str__(self):
        return self.name


'''
客户表
'''


class Customer(models.Model):
    # 客户QQ
    qq = models.CharField(max_length=64, unique=True)
    # 客户姓名 可为空
    name = models.CharField(max_length=32, blank=True, null=True)
    # blank=True admin层面可为空, null=True 数据库方面
    phone = models.BigIntegerField(blank=True, null=True)
    # 咨询课程
    course = models.ForeignKey('Course')

    # 咨询类型选择 admin
    course_type = models.CharField(max_length=64, choices=course_type_choices, default="offline_weekend")
    # 咨询结果
    consult_memo = models.TextField()
    # 来源
    source_type_choices = (
        ('qq', u'qq群'),
        ('referral', u'内部转介绍'),
        ('51cto', u'51cto'),
        ('agent', u'招生代理'),
        ('others', u'其他'),
    )
    # 来源类型选择
    source_type = models.CharField(max_length=64, choices=course_type_choices)
    referral_from = models.ForeignKey('self', blank=True, null=True, related_name='referraled_who')
    status_choices = (('signed', u'已报名'),
                      ('unregistered', u'未报名'),
                      ('graduated', u'已毕业'),
                      ('drop-off', u'退学'),
                      )

    # 状态
    status = models.CharField(max_length=64, choices=status_choices)
    # 课程顾问
    consultant = models.ForeignKey('UserProfile', verbose_name=u'课程顾问')

    #
    class_lis = models.ManyToManyField('ClassList', blank=True)
    # 自动创建日期 在admin上显示中文
    date = models.DateField(u'咨询日期', auto_now_add=True)

    def __str__(self):
        return '%s(%s)' % (self.qq, self.name)


class CustomerTrackRecord(models.Model):
    customer = models.ForeignKey('Customer')
    # 跟踪
    track_record = models.TextField(u'跟踪记录')
    # 追踪日期
    track_date = models.DateField(auto_now_add=True)
    # 追踪人
    follower = models.ForeignKey('UserProfile')

    # 追踪状态
    status_choices = ((1, u'近期无报名计划'),
                      (2, u'2个月内报名'),
                      (3, u'1个月内报名'),
                      (4, u'2周内报名'),
                      (5, u'1周内报名'),
                      (6, u'2天内报名'),
                      (7, u'已报名'))

    status = models.IntegerField(u'状态', choices=status_choices, help_text=u'客户选择的')

    def __str__(self):
        return self.custorm


'''
课程
'''


class Course(models.Model):
    # 课程名字
    name = models.CharField(max_length=64, unique=True)
    # 课程价格
    online_price = models.IntegerField()
    # 面授价格
    offline_price = models.IntegerField()

    # 课程介绍
    introduction = models.TextField()

    def __str__(self):
        return self.name


'''
班级

'''


class ClassList(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')

    semester = models.IntegerField(verbose_name=u'学期')
    # 讲师
    teachers = models.ManyToManyField(UserProfile)
    # 咨询类型选择 admin
    course_type = models.CharField(max_length=64, choices=course_type_choices, default="offline_weekend")

    # 开课时间
    start_date = models.DateField()
    # 结业时间
    graduate_date = models.DateField()

    def __str__(self):
        return '%s(%s)(%s)' % (self.course.name, self.course_type, self.semester)

    class Meta:
        unique_together = ('course', 'semester', 'course_type')


'''
课程记录
'''


class CourseRecord(models.Model):
    class_obj = models.ForeignKey('ClassList')
    # 课程数量
    day_num = models.IntegerField(u'第几节课')
    # 上课时间
    course_date = models.DateField(auto_now_add=True, verbose_name=u'上课时间')
    # 讲师
    teacher = models.ForeignKey('UserProfile')
    # 学生
    students = models.ManyToManyField('Customer')

    def __str__(self):
        return '%s, %s' % (self.class_obj, self.day_num)

    class Meta:
        unique_together = ('class_obj', 'day_num')


class StudyRecord(models.Model):
    course_record = models.ForeignKey('CourseRecord')

    # 关联 客户表
    student = models.ForeignKey('Customer')
    # 上课状态选择
    record_choices = (('checked', u'已签到'),
                      ('late', u'迟到'),
                      ('noshow', u'缺勤'),
                      ('leave_early', u'早退'),
                      )
    # 上课状态
    record = models.CharField(u'状态', choices=record_choices, max_length=64)

    # 成绩选择
    score_choices = ((100, 'A+'),
                     (90, 'A'),
                     (85, 'B+'),
                     (80, 'B'),
                     (75, 'B-'),
                     (60, 'C+'),
                     (50, 'C'),
                     (40, 'C-'),
                     (0, 'D'),
                     (-1, 'N/A'),
                     (-100, 'COPY'),
                     (-1000, 'FALL'),
                     )
    # 成绩
    score = models.IntegerField(u'本节成绩', choices=score_choices, default=-1)
    # 日期
    date = models.DateTimeField(auto_now_add=True)
    # 备注
    note = models.CharField(u'备注', max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s, %s, %s' % (self.course_record, self.student, self.record)
