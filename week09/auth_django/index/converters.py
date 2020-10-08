# 你的自定义过滤器

class IntConverter:
    regex = '[0-9]+'

    # 把 网址 转换成数字
    def to_python(self, value):
        return int(value)
    # 把 数字 转换成网址
    def to_url(self, value):
        return str(value)

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    # 把 网址 转换成数字
    def to_python(self, value):
        return int(value)

    # 把 数字 转换成网址
    def to_url(self, value):
        return '%04d' % value