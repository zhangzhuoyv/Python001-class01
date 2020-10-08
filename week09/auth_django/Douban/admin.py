from django.contrib import admin

# Register your models here.
from .models import T1
# 在同级的 models.py 引入 模型 T1

admin.site.register(T1)