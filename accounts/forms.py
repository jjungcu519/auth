from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
# 유저 테이블의 정보를 가져와서 장고의 session(카드키)을 create : 일련의 login 처리 과정
class CustomAuthenticationForm(AuthenticationForm):
    pass