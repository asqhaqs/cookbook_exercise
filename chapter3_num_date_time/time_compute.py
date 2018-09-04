# -*- coding:utf-

# 让python2 使用中文编码

from datetime import timedelta

# 表示一个时间间隔
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b

print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds()/3600)

# 表示特定的时间
from datetime import datetime

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))

b = datetime(2012, 12, 21)
d = b -a
print(d.days)

now = datetime.today()
print(now)

# 找出上周五是几号
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date-timedelta(days=days_ago)
    return target_date

print(get_previous_byday('Mon'))

# 找出当月的所有日期
from datetime import date
import calendar

def get_month_range(start_date = None):
    if start_date is None:
        # 快速计算出该月份中第一天的日期
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return(start_date, end_date)
print(get_month_range())

a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day