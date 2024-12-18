from django.db import models
from django.contrib import auth
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db import models
from django.db.models.manager import EmptyManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.contrib.auth.models import (
    PermissionsMixin,AbstractBaseUser, BaseUserManager
)
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from helpers.models import BaseModel



class UserManager(BaseUserManager) :
    use_in_migrations = True


    def _create_user(self, username, email , password , **extra_fields) :
        
        if not username :
            
            raise ValueError('Username must be set')
        
        if not email :
            
            raise ValueError('Email must be set')
        
        email = self.normalize_email (email)
        username = self.model.normalize_username(username)  
        user = self.model (username = username , email = email , **extra_fields)  
        user.set_password(password)
        user.save(using = self._db)
        return user 

    def create_user (self, username , email , password = None , **extra_fields) :
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser' , False)
        return self._create_user( username , email , password, **extra_fields)

    def create_superuser(self, username,email = None , password  = None , **extra_fields) :
        
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' ,True)
        
        if extra_fields.get('is_staff') is not True :
         
            raise  ValueError('Superuser must have is_staff = True' )
       
        if extra_fields.get('is_superuser') is not True :
           
            raise ValueError('Superuser must have is_super_user = True' )
        
        return self._create_user(username , email , password , **extra_fields)
    
        
        
        

class User (PermissionsMixin,AbstractBaseUser,BaseModel) :
    
    username_validator = UnicodeUsernameValidator()
    
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    
    email = models.EmailField( max_length=254 , unique = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_verified = models.BooleanField(default = False)
    date_joined = models.DateTimeField(default  = timezone.now)
    
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def token(self) :
        token = jwt.encode({
            "username" :self.username ,
            "email" : self.email ,
            "exp" :datetime.utcnow() + timedelta(hours = 23)
            
        },settings.SECRET_KEY, algorithm='HS256')
        
        return token
    