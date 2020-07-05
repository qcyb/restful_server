from datetime import datetime, timedelta
from datetime import date
# 第三方库
import pytz
from django.utils import timezone
from django.utils.dateparse import parse_datetime

"""
避免以下写法, 防止 tzinfo=<DstTzInfo 'Asia/Shanghai' LMT+8:06:00 STD> 和 tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD> 的区别:
    dt.replace(tzinfo=tzinfo)
建议写法:
    tzinfo.localize(dt)

UTC 零时区时间:
    dt.utctimetuple()
"""


class Datetime(object):
    LOCAL_TZ = timezone.FixedOffset(8*60)   # 分钟. workaround: https://docs.djangoproject.com/zh-hans/2.2/_modules/django/utils/timezone/
    UTC = pytz.utc

    @staticmethod
    def localtime() -> datetime:
        return timezone.localtime()

    @staticmethod
    def timestamp() -> int:
        return int(timezone.localtime().timestamp())

    @staticmethod
    def replace_timezone(dt: datetime, tzinfo=LOCAL_TZ) -> datetime:
        """
        替换时区, 年月日时分秒都保持不变.
        :param dt:
        :param tzinfo: 指定参数dt的时区
        :return:
        """
        return dt.replace(tzinfo=tzinfo)

    @staticmethod
    def convert_timezone(dt: datetime, tzinfo=LOCAL_TZ) -> datetime:
        """
        转换时区, 年月日时分秒相应转换.
        :param dt:
        :param tzinfo: 指定参数dt的时区
        :return:
        """
        return dt.astimezone(tz=tzinfo)

    @staticmethod
    def from_microsecond(microsecond, tzinfo=LOCAL_TZ) -> datetime:
        """
        微妙转 datetime
        :param microsecond:
        :param tzinfo: 指定参数dt的时区
        :return:
        """
        timestamp = microsecond / 1000000.0
        return datetime.fromtimestamp(timestamp, tzinfo)

    @staticmethod
    def to_microsecond(dt: datetime) -> int:
        """
        datetime 转微妙
        :param dt:
        :return:
        """
        return int(dt.timestamp() * 1000000)

    @staticmethod
    def to_millisecond(dt: datetime) -> int:
        """
        datetime 转毫秒
        :param dt:
        :return:
        """
        return int(dt.timestamp() * 1000)

    @staticmethod
    def to_int_day(dt: date) -> int:
        """
        date 转日期整型. 如: date(2020, 01, 01) -> 20200101
        :param dt:
        :return:
        """
        return int(dt.strftime('%Y%m%d'))

    @staticmethod
    def from_millisecond(millisecond, tzinfo=LOCAL_TZ) -> datetime:
        """
        毫秒转 datetime
        :param millisecond:
        :param tzinfo: 指定参数dt的时区
        :return:
        """
        timestamp = millisecond / 1000.0
        return datetime.fromtimestamp(timestamp, tzinfo)

    @staticmethod
    def from_timestamp(timestamp, tzinfo=LOCAL_TZ) -> datetime:
        return datetime.fromtimestamp(timestamp, tzinfo)

    @staticmethod
    def from_date(d: date, tzinfo=LOCAL_TZ) -> datetime:
        dt = datetime.combine(d, datetime.min.time())
        return Datetime.replace_timezone(dt, tzinfo=tzinfo)

    @staticmethod
    def to_str(dt: datetime, fmt='%Y%m%d'):
        """
        datetime 转换为 string
        :param dt:
        :param fmt: 常用 %Y-%m-%d %H:%M:%S
        :return:
        """
        return dt.strftime(fmt)

    @staticmethod
    def from_str(string: str, fmt='%Y%m%d', tzinfo=LOCAL_TZ):
        """
        string 转成 datetime
        :param string:
        :param fmt: 常用 %Y-%m-%d %H:%M:%S
            %a 星期几的简写
            %A 星期几的全称
            %b 月分的简写
            %B 月份的全称
            %c 标准的日期的时间串
            %C 年份的后两位数字
            %d 十进制表示的每月的第几天
            %D 月/天/年
            %e 在两字符域中，十进制表示的每月的第几天
            %F 年-月-日
            %g 年份的后两位数字，使用基于周的年
            %G 年分，使用基于周的年
            %h 简写的月份名
            %H 24小时制的小时
            %I 12小时制的小时
            %j 十进制表示的每年的第几天
            %m 十进制表示的月份
            %M 十时制表示的分钟数
            %n 新行符
            %p 本地的AM或PM的等价显示
            %r 12小时的时间
            %R 显示小时和分钟：hh:mm
            %S 十进制的秒数
            %t 水平制表符
            %T 显示时分秒：hh:mm:ss
            %u 每周的第几天，星期一为第一天 （值从0到6，星期一为0）
            %U 第年的第几周，把星期日做为第一天（值从0到53）
            %V 每年的第几周，使用基于周的年
            %w 十进制表示的星期几（值从0到6，星期天为0）
            %W 每年的第几周，把星期一做为第一天（值从0到53）
            %x 标准的日期串
            %X 标准的时间串
            %y 不带世纪的十进制年份（值从0到99）
            %Y 带世纪部分的十制年份
            %z，%Z 时区名称，如果不能得到时区名称则返回空字符。
            %% 百分号
        :return:
        """
        dt = datetime.strptime(string, fmt)
        return Datetime.replace_timezone(dt, tzinfo=tzinfo)

    @staticmethod
    def from_iso8601(string: str, tzinfo=LOCAL_TZ):
        dt = parse_datetime(string)
        return Datetime.convert_timezone(dt, tzinfo=tzinfo)

    @staticmethod
    def iter(start_date: date, end_date: date):
        assert isinstance(start_date, date) and isinstance(end_date, date)
        while start_date <= end_date:
            yield start_date
            start_date += timedelta(days=1)
