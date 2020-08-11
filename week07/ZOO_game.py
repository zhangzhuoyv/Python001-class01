from abc import ABCMeta, abstractmethod


class Zoo(object):
    def __init__(self, name):
        self.name = name


class Animal(metaclass=ABCMeta):
    # 这里子类必须实例化，否则会报错
    @abstractmethod
    def __init__(self, name, kinds, size, character):
        self.name = name
        self.kinds = kinds
        self.size = size
        self.character = character

    # 把判断是否凶猛动物的方法，装饰为属性，返回 体型，种类，性格 三个属性
    @property
    def is_ferocious(self):
        return self.size != '小' and self.kinds == '食肉' and self.character == '凶猛'

    # 输出 返回结果
    # 输出 使用此实例化的类的名字（cat), 名字，体型，性格，是否凶猛动物
    # 如果 描述符 is_ferocious 如果判定为凶猛都懂，则输出凶猛动物，如果不是，则为空
    def __str__(self):
        return (
            f"<{self.__class__.__name__},{self.name},{self.size},{self.character}"f"{'(凶猛动物' if self.is_ferocious else ''}>")

    # 类的专属用法 把 __str__返回的结果打印
    __repr__ = __str__


# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
class Cat(Animal):
    # 静态属性 猫的叫声 必须是 喵喵叫
    sounds = 'miao miao miao'

    def __init__(self, name, kinds, size, character):
        # 继承父类 Animal 的 属性：name,kinds,size,character
        super().__init__(name, kinds, size, character)
        self.suitale_pet = True  # 适合当宠物


class Zoo:
    # 动物园能改名字
    def __init__(self, name):
        self.name = name
        # 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能
        # 不能重复，就用集合 set()
        # 动物种类这个属性不行给人修改，所以用私有属性
        self.__animals = set()

    # 增加动物的方法

    # 传入 要增加的动物名称
    def add_animal(self, animal):
        # 先判定 要增加的动物种类 在动物园内已经存在，如果不存在就添加，如果存在就返回 False
        if animal not in self.__animals:
            self.__animals.add(animal)
            return True
        return False

    # 获取 动物种类下的所有成员
    # 之所以用 any (),而不是 all (),为了取不到值时，返回 False

    def __getattr__(self, item):
        # 把 所有动物种类 逐一 赋予给 i
        # 把 动物种类  的 类名 赋予给 item
        # 返回 所有 动物 的类 的名字 （item)
        return any(i.__class__.__name__ == item for i in self.__animals)


# 程序在这里开始运行

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')

    # 用集合Cat（） 取装载 class Cat 的各种实例 （各种各样的猫）
    cats = (
        Cat('短毛猫', '食肉', '小', '温顺'),
        Cat('雪鞋猫', '食肉', '小', '温顺'),
        Cat('斯芬克猫', '食肉', '小', '温顺'),
        Cat('缅因库嗯猫', '食肉', '大', '温顺'),
        Cat('波斯猫', '食肉', '中', '温顺'),
        Cat('喵喵怪', '食肉', '大', '凶猛'),

    )

    # 添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。

    # 验证 动物园里是否有 猫 这个种类的动物
    print(f"动物园里是否有猫这种动物 ： {getattr(z, 'Cat')}")

    # 验证 动物园里是否有 老鼠 这种动物
    print(f"动物园里是否有老鼠这种动物 ： {getattr(z, 'Mouse')}")

    print('现在往动物园里添加动物')

    # 把 定义好的 猫类的集合，逐一赋予给 cat
    for cat in cats:
        # 类 Zoo 的实例化 z ,使用方法 add_animal 把 cat 传进去
        cat_add = z.add_animal(cat)

        # 验证添加 各种猫 是否成功
        print(f" 添加 {cat} : {'成功' if cat_add else '失败'}")

    print('-' * 40)
    # 下面验证，重复 添加 类，是否会报错

    print('现在尝试重复添加各种猫，看是否会添加失败')

    for cat in cats:
        # 类 Zoo 的实例化 z ,使用方法 add_animal 把 cat 传进去
        cat_add = z.add_animal(cat)

        # 验证添加 各种猫 是否成功
        print(f" 添加 {cat} : {'成功' if cat_add else '失败'}")

    print('-' * 40)

    # 验证动物园里的种类
    print(f"动物园里是否有猫 ：{getattr(z, 'Cat')}")
    print(f"动物园里是否有狗 ：{getattr(z, 'Dog')}")
