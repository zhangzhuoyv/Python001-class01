"""
Django settings for auth_django project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# 项目路径：
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 密钥
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7vf105emfoofjqd*h)_=c(l_vu9cwwxqi*mozce)_+xn-)4nyj'


# 调试模式
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 域名访问权限
ALLOWED_HOSTS = []

# app注册列表
# Application definition
INSTALLED_APPS = [
    # 内置后台管理系统
    'django.contrib.admin',
    # 内置后台用户认证系统
    'django.contrib.auth',
    # 所有 model 元数据
    'django.contrib.contenttypes',
    # 会话 表示当前访问网站的用户身份
    'django.contrib.sessions',
    # 消息提示
    'django.contrib.messages',
    # 静态资源路径
    'django.contrib.staticfiles',
    # 下面开始可以注册自己的app
    'index',
    'Douban',
]

# 中间件是 request 和 response 对象之间的钩子
# request 时，从上到下读取， response 从下到上返回
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 路由匹配功能 URLconf, 也就是 项目根目录下的 url.py
ROOT_URLCONF = 'auth_django.urls'

# 模版设置
TEMPLATES = [
    {
        # 定义模版引擎
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 设置模版路径
        'DIRS': [],
        # 是否在 app 里查找模版文件
        'APP_DIRS': True,
        # 用于 requestcontext 上下文的调用函数
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI 的配置
WSGI_APPLICATION = 'auth_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#### 数据库配置，默认是sqlite，Django2.2使用mysqlclient或pymysql模块连接MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# export PATH=$PATH:/usr/local/mysql/bin
# OSError: mysql_config not found
# pip install mysqlclient
# pip install pymysql

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db1',
        'USER': 'root',
        'PASSWORD': '195917aa',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
    # 生产环境可能要链接第二个数据库
    # 'db2': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'mydatabase',
    #     'USER': 'mydatabaseuser',
    #     'PASSWORD': 'mypassword',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3307',
    # }
}







# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# 密码认证功能
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# 语言编码
LANGUAGE_CODE = 'en-us'
# 时区
TIME_ZONE = 'UTC'

# 国际化相关配置
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# 静态文静目录
STATIC_URL = '/static/'
