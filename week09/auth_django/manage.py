#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_django.settings')
    # 注册环境变量，加载 'DJANGO_SETTINGS_MODULE', 'auth_django.settings'

    # 关于导入失败 的处理方法
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 如果导入成功，实行下面函数
    # sys.argv 是文件的执行命令， 比如 python manage.py runserver 8080， runserver 8080 就是传进函数的 sys.argv
    execute_from_command_line(sys.argv)

# __name__ 随着环境变化，自动动产生变化
# 如果 是在直接对本文件运行，比如 python manage.py ,  这时的 __name__ = 'main' , main()就会自动运行
# 如果是 import manage.py  ，这时的 __name__ = '使用import的文件名称'，只时候只引入定义，main() 并不会自动运行。
if __name__ == '__main__':
    main()
