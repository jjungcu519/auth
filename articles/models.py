from django.db import models
#방법 1
from accounts.models import User
#방법 2
from django.conf import settings
#방법 3
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


    #포린키 연결 방법1: 유저 모델을 직접 참조 (권장x)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    #포린키 연결 방법2: settings의 변수활용
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    #포린키 연결 방법3: get user model
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    #user_id = ?