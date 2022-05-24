from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
# Create your models here.

class AppUserManager(BaseUserManager):
    # 유저 생성 시 create_user 함수가 작동
    def create_user(self,email,password,nickname,**extra_fields):
        # 사용하지 않는 나머지 값들은 **extra_fields로 모조리 받아 옴
        if not email:
            raise ValueError(_('The Phone must be filled with'))
        if '-' in email:
            raise ValueError(_('The Phone must be filled with numeric, not "-"'))

        user = self.model(email=email,nickname=nickname,**extra_fields)

        #password hash 및 유저 save
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,nickname,**extra_fields):
        user = self.model(email=email,nickname=nickname,**extra_fields)

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        # password hash 및 유저 save
        user.set_password(password)
        user.save(using=self._db)
        return user

class AppUser(AbstractUser, PermissionsMixin):
    objects = AppUserManager()
    # 이놈을 만들 때에는 위의 AppUserManager()를 작동해라

    class Meta:
        # 관리자 화면에서 해당 클래스가 아래에 명명한 이름으로 나타난다.
        verbose_name='고객'
        verbose_name_plural="고객들"

    nickname=models.CharField(max_length=10,unique=True,verbose_name='별명')
    username = None
    # username 필드를 없애고, uique한 필드로 수정
    email = models.CharField(max_length=20,unique=True,verbose_name='이메일')

    USERNAME_FIELD = 'email'
    # 각 유저를 구분짓는 USERNAME_FIELD의 값을 email 으로 지정 -> 자동적으로 Require
    REQUIRED_FIELDS = ['nickname']
    # 이전에는 AbstractBaseUser의 default값인 username을 통해 User를 구분했다.
    # 하지만 username=None으로 username필드를 없애고,
    # USERNAME_FIELD = 'email'를 통해 email이 해당 역할을 수행하도록 만들었다!!
    data_joined=models.DateTimeField(verbose_name='data_joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login',auto_now=True)
    #permissions
    is_active =models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    def __str__(self):
        return self.nickname