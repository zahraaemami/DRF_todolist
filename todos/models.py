from django.db import models
from helpers.models import BaseModel
from authentication.models import User 


class Todo (BaseModel) :
    
    title = models.CharField( max_length=50 ,blank = True , default = '')
    description = models.TextField()
    is_complete = models.BooleanField(default = False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self) :
        return self.title
