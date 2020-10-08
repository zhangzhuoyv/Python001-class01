# manage.py 源代码跟踪

# 同时，__init__ 导入的某些功能也发挥作用：

from collections import OrderedDict, defaultdict
# OrderedDict 有序的字典 ，defaultdict 有默认工厂的字典


import django
from django.apps import apps
from django.conf import settings # 就是 setting.py

from django.core.management.base import (
    BaseCommand, CommandError, CommandParser, handle_default_options,
)


# 假设 我们运行 python manage.py runserver 8080
from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)  #sys.argv =('manage.py', 'runsever 8080')


# 跟踪 execute_from_command_line ，所在路径如下
# week09/auth/lib/python3.7/site-packages/django/core/management/__init__.py

def execute_from_command_line(argv=None):
    """Run a ManagementUtility."""
    utility = ManagementUtility(argv)  # argv = ('manage.py', 'runsever 8080')
    utility.execute()


# 跟踪 ManagementUtility（）---只关注需要的

class ManagementUtility:
    """
    Encapsulate the logic of the django-admin and manage.py utilities.
    """
    def __init__(self, argv=None): #  argv = ('manage.py', 'runsever 8080')
        self.argv = argv or sys.argv[:]

    def execute(self):

        subcommand = self.argv[1] # 1 = runsuner 8080

        settings.INSTALLED_APPS # 源于 from django.conf import settings ， 此处作为 加载 settings.py 里的 install_app

        # 检查 Django配置有没错误的检查
        if subcommand == 'runserver' and '--noreload' not in self.argv:

        self.autocomplete()
        # 对初始的配置进行检查


        # 如果都没异常，就执行下面代码
        self.fetch_command(subcommand).run_from_argv(self.argv)  # subcommand == runserver  self.argv = 8080

        # 以上为了一系列的检查，都是为了进行 fetch_commad(runserver) 这件事，下面跟踪 fetch_commad

        # 先买呢我们来跟踪 fetch_command

    def fetch_command(self, subcommand):

        commands = get_commands() # 命令的名字的列表  理解成把命令拆分成自命令，然后放在列表里
        try:
            app_name = commands[subcommand] # suncommand = runserver

        if isinstance(app_name, BaseCommand): # 判断runserver 是否已经被加载了
            # If the command is already loaded, use it directly.
            klass = app_name
        else:
            # 如果没有加载，就加载 app_name ,和 subcommadn 也就是 runserver
            klass = load_command_class(app_name, subcommand)
        return klass


        # 再继续追踪 load_command_class()

        def load_command_class(app_name, name):

            module = import_module('%s.management.commands.%s' % (app_name, name)) # 导入模块的路径

            return module.Command()


site-packages/django/contrib/staticfiles/management\
/commands/runserver.py
# 这里没有用系统自带的 import ,而是自定义一个 import 函数，好处是可以自定义导入路径。

site-packages/django/core/management/commands/runserver.py run_from_argv

site-packages/django/core/management/base.py

self.execute(*args,**cmd_options)
