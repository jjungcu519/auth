## 모델링과 마이그레이션의 비밀(?)
- superuser를 생성하기 위해 makemigrate가 선행되어야하는거 아니냐?
    - 장고가 작성한 모델을 migrate 하여 superuser를 생성할 수 있다.
- models.py에 AbstractUser를 상속해준다.
    - [장고 깃헙](https://github.com/django/django/blob/main/django/contrib/auth/models.py)
    - [Customizing authentication in Django](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/_)
- settings.py에 새로운 유저 모델만든다.
- 새로운 유저 모델 사용하기 위해 SQL 표를 지우고 다시 migrate
- AUTH_USER_MODEL = 'accounts.User' 등록

## 과정
- 로그인 페이지를 만들기 위한 base.html 생성
- url 연동해주기
- forms.py에 장고 USERCREATIONFORM 상속
- RMdkrdndkr 이후 내요ㅐㅇ commit 메세지 참고 