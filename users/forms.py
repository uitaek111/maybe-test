from django import forms
from django.core.exceptions import ValidationError
from users.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length = 20,    # 길이제한 
        min_length = 2,
        widget = forms.TextInput(
            attrs = {"placeholder":"사용자명 (2자리 이상)"},
        )
    )

    password = forms.CharField(
        min_length = 4,
        widget = forms.PasswordInput(
            attrs = {"placeholder":"비밀번호 (4자리 이상)"},
        )
    )

class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    # username 유효성 검사
    def clean_username(self):
        username = self.cleaned_data["username"]

        if User.objects.filter(username=username).exists():
            return ValidationError(f"입력한 사용자명({username})은 이미 사용 중입니다.")

        return username    

    # password 유효성 검사
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            # password2 필드에 오류를 추가
            self.add_error("password2", "비밀번호와 비밀번호 확인란의 값이 다릅니다.")
        
    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        profile_image = self.cleaned_data["profile_image"]
        short_description = self.cleaned_data["short_description"]

        user = User.objects.create_user(
            username = username,
            password = password1,
            profile_image = profile_image,
            short_description = short_description,
        )

        return user