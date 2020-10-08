from  django import forms

# 基础表单
class loginForm(forms.Form):
    username=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput,min_length=8) #密码最小长度为6位

