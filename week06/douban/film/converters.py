# 转换器 用于自定义匹配规则

class IntConverter:
    regex = '[0-9]+'  # 匹配的正则方式

    # 网址上的数字，人看是数字，对于机器来说是字符串
    # 所以要先转化成数字，给python 处理
    #处理完，再转成字符串，给网址进行合并

    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return str(value)


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return '%04d' %value